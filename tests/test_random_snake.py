import pytest
import tkinter as tk
from unittest.mock import patch
import sys 
import os
sys.path.append("..")
#from src.snakecharmerpackage import settings
from src.snakecharmerpackage.random_snake import RandomSnake

@pytest.fixture(scope="module")
def snake_game():
    """Creates a fresh instance of RandomSnake for testing."""
    #with patch("tkinter.Tk.mainloop"):
    root = tk.Tk()
    game = RandomSnake(root)
    
    """game.create_rectangle = lambda *args, **kwargs: None
    game.create_oval = lambda *args, **kwargs: None
    game.create_text = lambda *args, **kwargs: None
    game.delete = lambda *args, **kwargs: None"""

    #game.update()
    game.wait_for_settings()

    yield game
    root.destroy()


"""def test_start_button_click(snake_game):
    #Make sure start button is working.
    start_button = snake_game.settings_window.start_button
    #assert snake_game.settings_window.start_button is not None
    #print(snake_game.settings_window.start_button)
    #start_button.invoke()

    assert start_button["text"] == "Start" """
    

def test_initial_speed(snake_game):
    """Make sure set pre-game speed is correct."""
    assert snake_game.speed_num == snake_game.master.settings["speed"]

def test_initial_color(snake_game):
    """Make sure set pre-game color is correct."""
    assert snake_game.master.color_settings["color"] == snake_game.color


def test_start_game(snake_game):
    """Ensure initial snake settings are correct at start of game."""
    assert snake_game.snake_positions == [(250, 250), (240, 250), (230, 250)]
    assert snake_game.direction == "none"


def test_game_speed(snake_game):
    """Verify game speed calculation."""
    #snake_game.speed_num = 90
    #snake_game.speed(snake_game.speed_num)
    expected_speed = int((1000 / snake_game.master.settings["speed"]) * 10)
    assert snake_game.game_speed == expected_speed


@pytest.mark.parametrize("valid_color", ["red", "purple", "green", "#FF5733"])
def test_valid_color(valid_color, snake_game):
    """Check that valid colors are applied correctly."""
    snake_game.master.color_settings["color"] = valid_color
    snake_game.wait_for_settings()

    assert snake_game.color == valid_color


def test_invalid_color(snake_game):
    """Invalid color should result in a randomized hex color."""
    snake_game.master.color_settings["color"] = "notacolor"
    snake_game.wait_for_settings()
    assert snake_game.color.startswith("#") and len(snake_game.color) == 7


def test_movement(snake_game):
    """Check that snake moves correctly in each direction."""
    move_size = 10
    start = (250, 250)

    directions = {
        "left": (start[0] - move_size, start[1]),
        "right": (start[0] + move_size, start[1]),
        "up": (start[0], start[1] - move_size),
        "down": (start[0], start[1] + move_size)
    }

    for direction, expected_pos in directions.items():
        snake_game.snake_positions = [start]
        snake_game.direction = direction
        snake_game.move_snake()
        assert snake_game.snake_positions[0] == expected_pos

def test_apple_spawning(snake_game):
    """Verify apples are correctly spawned within bounds."""
    snake_game.spawn_apples(5)
    assert len(snake_game.apples) == 5
    for x, y in snake_game.apple_positions:
        assert 0 <= x <= 490 and 0 <= y <= 490


def test_game_over(snake_game):
    """Trigger a collision and check for game over display."""
    snake_game.snake_positions[0] = (5, 5)  # Out of bounds
    collision = snake_game.check_collisions()
    assert collision is True  # if yes, then game ended
    """snake_game.perform_actions()
    assert snake_game.check_collisions()
    snake_game.end_game()
    assert snake_game.find_withtag("game_over")"""

