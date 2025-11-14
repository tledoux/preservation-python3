import asyncio
import ctypes
import gettext
import locale
import os
import platform
import pygame
import random
import sys
from snake import Direction, Snake

__appname__ = "Preservation Python"
__version__ = "1.1.0"


def resource_path(relative_path: str):
    """To handle external resources within exe package"""
    bundle_dir = os.path.abspath(os.path.dirname(__file__))
    path_to_data = os.path.join(bundle_dir, relative_path)
    return path_to_data


def running_in_browser():
    return sys.platform == "emscripten"


def running_in_windows():
    return sys.platform == "win32"


# Initialize gettext
__domain__ = "preservation"
__locale_dir__ = "translations"
# Set up message catalog access for translations
# Retrieve the current locale

if running_in_browser():
    current_locale = platform.window.navigator.language  # type: ignore
    platform.console.log(f"Detected browser locale: {current_locale}")  # type: ignore
elif running_in_windows():
    # getlocale doesn't work properly on Windows, so we use ctypes to get the locale
    kernel32 = ctypes.windll.kernel32
    current_locale = locale.windows_locale.get(kernel32.GetUserDefaultLangID(), "en_US")
    assert current_locale is not None, "Could not determine the current locale."
    print(f"Found locale in Windows: {current_locale}")
else:
    current_locale = locale.getlocale()[0]
    assert current_locale is not None, "Could not determine the current locale."
    print(f"Found locale: {current_locale}")
if "_" in current_locale:
    # Only extract the language, not the country
    current_locale = current_locale.split("_")[0]
if "-" in current_locale:
    # Only extract the language, not the country
    current_locale = current_locale.split("-")[0]
# Load the appropriate translation based on the current locale
lang = gettext.translation(
    __domain__,
    localedir=resource_path(__locale_dir__),
    languages=[current_locale, "en"],
    fallback=True,
)
# lang.install()
_ = lang.gettext
# print(f"Loaded translation for locale: {current_locale}")

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (128, 0, 128)
red_background = (255, 0, 0)
white_background = (255, 255, 255)

# Define screen dimensions
screen_width, screen_height = 1200, 800
block_size = 40
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(_("Preservation Python, Adapted from Snake Game by Edureka"))
prefix_score = _("Your Score: ")
bottom_message = ""
clock = pygame.time.Clock()


nb_items_for_ingest = 20

display_message_time = 3000  # milliseconds = 3 seconds
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("timesnewroman", 20)
bottom_font = pygame.font.SysFont("couriernew", 30)


# Load and scale the images for the food items
def load_and_scale_image(image_name):
    img = pygame.image.load(resource_path(f"images/{image_name}")).convert_alpha()
    img = pygame.transform.scale(img, (block_size, block_size))
    return img


# Define a enumeration for food types
class FoodType:
    INCREASE = 1
    DECREASE = 2


snake_parts = {
    "head": load_and_scale_image("snake_head.png"),
    "body": load_and_scale_image("snake_body.png"),
    "turn": load_and_scale_image("snake_turn.png"),
    "tail": load_and_scale_image("snake_tail.png"),
}

# Initial set of images for food that increases the score
food_increase_images_1 = [
    (load_and_scale_image("accessrights.png"), _("Access rights")),
    (load_and_scale_image("checksum.png"), _("Checksum")),
    (load_and_scale_image("context.png"), _("Context information")),
    (load_and_scale_image("dataobject.png"), _("Data object")),
    (load_and_scale_image("metadata.png"), _("Metadata")),
]

# New set of images after score reaches 'nb_items_for_ingest'
food_increase_images_2 = [
    (load_and_scale_image("backup.png"), _("Backup")),
    (load_and_scale_image("emulation.png"), _("Emulation")),
    (load_and_scale_image("migration.png"), _("Migration")),
    (load_and_scale_image("refresh.png"), _("Refresh")),
    (load_and_scale_image("techwatch.png"), _("Tech watch")),
]

# Images for food that decreases the score
food_decrease_images = [
    (load_and_scale_image("brokenhardware.png"), _("Broken hardware")),
    (load_and_scale_image("delete.png"), _("Accidental deletion")),
    (load_and_scale_image("legal.png"), _("Legal issues")),
    (load_and_scale_image("obsolete.png"), _("Obsolescence")),
    (load_and_scale_image("orgcommitment.png"), _("Lack of organizational commitment")),
    (load_and_scale_image("softwarebug.png"), _("Software bugs")),
    (load_and_scale_image("virus.png"), _("Virus attack")),
]


# Timer for spawning new food
food_timer = pygame.time.get_ticks()  # Initialize timer
last_food_type = FoodType.INCREASE  # Track the last food type

# List to store food items
food_items = []


# Function to display messages
def message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 3, screen_height / 3 + y_displace])


def verify_new_food_position(new_x, new_y):
    """Ensure new food does not spawn on other food items."""
    for food_x, food_y, _, _, _ in food_items:
        if new_x == food_x and new_y == food_y:
            return False
    return True


def food_random_position():
    """Generate a random position for food."""
    valid_position = False
    while not valid_position:
        food_x = (
            round(random.randrange(0, screen_width - block_size) / block_size)
            * block_size
        )
        food_y = (
            round(random.randrange(0, screen_height - block_size) / block_size)
            * block_size
        )
        valid_position = verify_new_food_position(food_x, food_y)
    return food_x, food_y


# Function to spawn food
def spawn_food(food_type=None, current_food_increase_images=None):
    global last_food_type
    if food_type is None:
        food_x, food_y = food_random_position()
        if last_food_type == FoodType.INCREASE:
            food_type = FoodType.DECREASE
        else:
            food_type = FoodType.INCREASE
        last_food_type = food_type
    else:
        food_x, food_y = food_random_position()
        last_food_type = food_type

    # Choose a specific image based on the food type
    if food_type == FoodType.INCREASE and current_food_increase_images is not None:
        image, food_text = random.choice(current_food_increase_images)
    else:
        image, food_text = random.choice(food_decrease_images)

    food_items.append((food_x, food_y, food_type, image, food_text))


async def show_game_start_screen():
    """
    Display the game start screen with instructions.
    Returns True if the game should start, False if it should exit.
    """
    game_start = False
    while not game_start:
        screen.fill(blue)
        message(_("Welcome to Preservation Python!"), white, -200)
        message(_("Collect preservation information."), white, -100)
        message(_("Avoid data loss and obsolescence."), white)
        message(_("Maintain accessibility!"), white, 100)
        message(_("Use the arrow keys or W,A,S,D to move."), yellow, 200)
        message(_("Press the SPACEBAR to start"), green, 250)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True

        clock.tick(15)  # Control the frame rate of the instructions screen
        await asyncio.sleep(0)
    return True


async def show_game_over_screen(score):
    """
    Display the game over screen with options to restart or quit.
    Returns True if the game should be restarted, False if it should exit.
    """
    game_over_screen = True
    return_value = False
    while game_over_screen:
        screen.fill(blue)
        message(_("Preservation Failure! The digital object is lost."), red, -100)
        message(prefix_score + str(score), red, -50)
        message(_("Press R to Play Again or Q to Quit"), green, 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_screen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over_screen = False
                    return False
                if event.key == pygame.K_r:
                    game_over_screen = False
                    return_value = True

        clock.tick(15)  # Control the frame rate of the game over screen
        await asyncio.sleep(0)
    return return_value


def show_ingest_complete_message(ingest_message_start_time):
    """
    Display the "Ingest complete" message for 3 seconds.
    """
    if pygame.time.get_ticks() - ingest_message_start_time < display_message_time:
        msg = _("Ingest complete. Keep it accessible!")
        mesg = font_style.render(msg, True, green)
        screen.blit(mesg, [screen_width - mesg.get_width() - 20, 20])
        return True
    else:
        # Stop displaying the message after 3 seconds
        return False


def draw_food_items():
    """
    Draw all food items on the screen."""
    for food_x, food_y, food_type, image, _ in food_items:
        if food_type == FoodType.INCREASE:
            pygame.draw.rect(
                screen, white_background, [food_x, food_y, block_size, block_size]
            )
        else:
            pygame.draw.rect(
                screen, red_background, [food_x, food_y, block_size, block_size]
            )
        # Draw the image on top of the background
        screen.blit(image, (food_x, food_y))


def show_bottom(bottom_message_start_time):
    """
    Display the bottom message on the screen."""
    global bottom_message
    if bottom_message and len(bottom_message) > 0:
        if pygame.time.get_ticks() - bottom_message_start_time < display_message_time:
            mesg = bottom_font.render(bottom_message, True, purple)
            width = mesg.get_width()
            screen.blit(mesg, [(screen_width - width) // 2, screen_height - 30])
        else:
            # Clear the message after 3 seconds
            bottom_message = ""


# Main game loop
async def gameLoop(dis_width, dis_height, food_timer):
    """
    Main game loop.

    Returns True if the game should be restarted, False if it should exit.
    """
    global bottom_message

    game_over = False
    game_close = False

    direction = Direction.STILL

    snake = Snake(dis_width / 2, dis_height / 2, snake_parts, blue)  # yellow)

    # Start with the initial set of images
    current_food_increase_images = food_increase_images_1
    # Track whether "Ingest complete" message should be displayed
    display_ingest_message = False
    # Store the time when the message is displayed
    ingest_message_start_time = 0
    bottom_message_start_time = 0
    # Spawn initial food item that FoodType.INCREASEs score
    spawn_food(FoodType.INCREASE, current_food_increase_images)

    # Instructions screen before the game starts
    if not await show_game_start_screen():
        return False

    # Main game loop
    while not game_over:
        if game_close:
            return await show_game_over_screen(snake.score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                direction = snake.handle(event)
        snake.move(direction)
        # Check for boundary collisions
        if snake.out_of_bounds(dis_width, dis_height):
            game_close = True
            continue  # Skip the rest of the loop to avoid drawing out of bounds
        screen.fill(blue)

        # Check if score is greater than or equal to 'nb_items_for_ingest' to switch images
        if (
            snake.length - 1 >= nb_items_for_ingest
            and current_food_increase_images != food_increase_images_2
        ):
            current_food_increase_images = food_increase_images_2
            # Trigger the display of the "Ingest complete" message
            display_ingest_message = True
            # Record the time the message is shown
            ingest_message_start_time = pygame.time.get_ticks()

        # Display "Ingest complete" message for 3 seconds
        if display_ingest_message:
            display_ingest_message = show_ingest_complete_message(
                ingest_message_start_time
            )

        # Check timer to spawn new food every 10 seconds
        if (
            pygame.time.get_ticks() - food_timer > 10000
        ):  # 10,000 milliseconds = 10 seconds
            # Spawn a food item that decreases score
            spawn_food(FoodType.DECREASE)
            food_timer = pygame.time.get_ticks()  # Reset timer

        snake.update()
        if snake.self_collision():
            game_close = True
            continue  # Skip the rest of the loop if game is over

        snake.draw(screen)
        # Update the score display
        snake.show_score(screen, score_font, prefix_score, yellow)

        # Draw all food items
        draw_food_items()

        # Check collision with each food item
        for i, (food_x, food_y, food_type, _, food_text) in enumerate(food_items):
            if snake.collide(food_x, food_y):
                if food_type == FoodType.INCREASE:
                    bottom_message = food_text
                    bottom_message_start_time = pygame.time.get_ticks()
                    snake.grow()  # Increase the snake's length
                    spawn_food(
                        FoodType.INCREASE, current_food_increase_images
                    )  # Spawn new food item
                elif food_type == FoodType.DECREASE:
                    bottom_message = food_text
                    bottom_message_start_time = pygame.time.get_ticks()
                    if snake.shrink():
                        game_close = True
                del food_items[i]  # Remove the food item after collision
                break

        # Ensure the score updates immediately after eating
        snake.show_score(screen, score_font, prefix_score, yellow)
        show_bottom(bottom_message_start_time)
        pygame.display.update()

        clock.tick(Snake.SPEED)
        await asyncio.sleep(0)
    return False


async def main():
    global food_items
    # Start the game loop
    while True:
        food_items = []  # Reset food items for each game loop
        if not await gameLoop(screen_width, screen_height, food_timer):
            if not running_in_browser():
                pygame.quit()
            return


asyncio.run(main())
