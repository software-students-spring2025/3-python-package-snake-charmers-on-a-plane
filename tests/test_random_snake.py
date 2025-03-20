import pytest
import tkinter as tk
from src.snakecharmerpackage import random_snake, settings
from src.snakecharmerpackage.random_snake import RandomSnake

snake = random_snake.RandomSnake(tk.Tk())

class Test:
    def test_initial_stats(self):
        '''
        Verify correct settings at initialization.
        '''
        assert snake.master.settings['speed'] == 50, f"Expected speed = 50 at initialization, was {snake.master.settings['speed']} instead"

    def test_start_game(self):
        '''
        Make sure initial snake settings are correct at start of game.
        '''
        snake.start_game()
        assert snake.snake_positions == [(250, 250), (240, 250), (230, 250)], f"Expected snake position = [(250, 250), (240, 250), (230, 250)], was {snake.snake_positions} instead"
        assert snake.direction == "right", f"Expected snake direction to be 'right', was {snake.direction} instead"

    def test_speed(self):
        '''
        Verfifies game speed.
        '''
        assert snake.game_speed == int((1000 / snake.master.settings["speed"]) * 10), f"Expected game speed to be proportional to user-set speed, was {snake.game_speed} instead"

    def test_valid_color(self):
        '''
        Verifies that a valid color selection is correctly applied
        '''
        valid_colors = ["red", "purple", "green", "#FF5733"]
        for color in valid_colors:
            snake.master.color_settings["color"] = color
            snake.wait_for_settings()
            assert snake.color == snake.master.color_settings["color"], f"Expected color {color}, got {snake.color} instead"

    def test_invalid_color(self):
        '''
        Verifies that an invalid color causes a random color to be generated
        '''
        invalid_color = "lqbrfiuqbefu"
        snake.master.color_settings["color"] = invalid_color
        snake.wait_for_settings()
        assert snake.color.startswith("#") and len(snake.color) == 7, f"Invalid color handling failed, got {snake.color}"

    def test_movement(self):
        '''
        Verifies that the snake correctly moves in each direction.
        '''
        test_root = tk.Tk()
        snake = RandomSnake(test_root, testing=True)
        move_size = 10

        snake.snake_positions = [(250, 250)]
        initial = snake.snake_positions[0]
        snake.direction = "left"
        snake.move_snake()
        assert snake.snake_positions[0] == (initial[0] - move_size, initial[1])
        snake.snake_positions = [(250, 250)]
        initial = snake.snake_positions[0]
        snake.direction = "right"
        snake.move_snake()
        assert snake.snake_positions[0] == (initial[0] + move_size, initial[1])
        snake.snake_positions = [(250, 250)]
        initial = snake.snake_positions[0]
        snake.direction = "up"
        snake.move_snake()
        assert snake.snake_positions[0] == (initial[0], initial[1] - move_size)
        snake.snake_positions = [(250, 250)]
        initial = snake.snake_positions[0]
        snake.direction = "down"
        snake.move_snake()
        assert snake.snake_positions[0] == (initial[0], initial[1] + move_size)

    def test_game_over(self):
        '''
        Verfies game over screen is displayed after a wall is touched
        '''
        snake.snake_positions = [(10, 10)]
        snake.perform_actions()
        assert not snake.after(snake.game_speed, snake.perform_actions), "Game failed to stop after collision!"



