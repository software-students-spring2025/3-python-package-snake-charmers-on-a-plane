import pytest
import tkinter as tk
from src.snakecharmerpackage import random_snake
from src.snakecharmerpackage import settings

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



