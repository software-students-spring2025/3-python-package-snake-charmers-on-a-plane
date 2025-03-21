import pytest
import tkinter as tk
import sys 
sys.path.append("..")
from snakecharmerpackage import random_snake

snake = random_snake.RandomSnake(tk.Tk())

class Test:
    def test_initial_setup(self):
        '''
        Make sure default pre-game settings are correct.
        '''
        assert snake.master.settings["speed"] == 50, f"Expected initialized speed to be 50, was {snake.master.settings.get('speed')} instead"
        assert snake.master.color_settings["color"] == "yellow", f"Expected initialized color to be yellow, was {snake.master.color_settings['color']} instead"

    def test_start_game(self):
        '''
        Make sure initial snake settings are correct at start of game.
        '''
        snake.start_game()
        assert snake.snake_positions == [(250, 250), (240, 250), (230, 250)], f"Expected snake position = [(250, 250), (240, 250), (230, 250)], was {snake.snake_positions} instead"
        assert snake.direction == "none", f"Expected snake direction to be 'right', was {snake.direction} instead"

    def test_game_speed(self):
        '''
        Verifies game speed.
        '''
        assert snake.game_speed == int((1000 / snake.master.settings["speed"]) * 10), f"Expected game speed to be proportional to user-set speed, was {snake.game_speed} instead"

    def test_color(self):
        '''
        Verifies user's color.
        ''' 
        assert snake.color == snake.master.color_settings["color"], f"Expected game color to be same as set color, was {snake.color} instead"

    def test_movement(self):
        '''
        Makes sure that snake is moving properly.
        '''
        
