import tkinter as tk
from PIL import Image, ImageTk, ImageColor
from tkinter import ttk
import random
from src.snakecharmerpackage.settings import Settings

move_size = 10 # pixels

class RandomSnake(tk.Canvas): # self is Canvas object
    '''
    A small snake game, where any key press randomizes the 
    direction that your snake heads in.
    '''

    def __init__(self, master):
        # set up Canvas (container for all objects)
        super().__init__(
            master, width=500, height=500, background="darkgreen", highlightthickness=0
        )
        mainframe = ttk.Frame(self, padding="3 3 12 12")

        self.master = master
        self.master.settings = {"speed": 50}
        self.master.color_settings = {"color": "yellow"}
        self.wait_for_settings()

    def draw(self):
        self.delete("snake")
        for x, y in self.snake_positions:
            self.create_rectangle(x, y, x + 10, y + 10, fill=self.color, tag="snake")

    def move_snake(self):
        '''
        Defines movement for the snake.
        '''
        head_x, head_y = self.snake_positions[0]

        if self.direction == "left":
            new_head_pos = (head_x - move_size, head_y)
        elif self.direction == "right":
            new_head_pos = (head_x + move_size, head_y)
        elif self.direction == "down":
            new_head_pos = (head_x, head_y + move_size)
        elif self.direction == "up":
            new_head_pos = (head_x, head_y - move_size)

        # replace head with body
        self.snake_positions = [new_head_pos] + self.snake_positions[:-1]

        self.draw()

    def move_random(self, event):
        ''' 
        Randomizes the snake's movement. 
        '''
        all_directions = ["up", "down", "left", "right"]
        opposites = ({"up", "down"}, {"left", "right"})

        # make next direction != current direction
        all_directions.remove(self.direction)
        random_direction = random.choice(all_directions)
        all_directions.append(self.direction)

        if ( 
            random_direction in all_directions 
            and {random_direction, self.direction} not in opposites # make sure snake doesn't collide with itself
        ):
            self.direction = random_direction

    def wait_for_settings(self):
        settings_window = Settings(self.master)
        self.master.wait_window(settings_window)
        self.speed(self.master.settings["speed"])
        try: #if input is a valid color, then all clear!
            ImageColor.getrgb(self.master.color_settings["color"])#check if valid
            self.color = self.master.color_settings["color"]#set!
        except: #else, randomize!
            #sorry for how gross and long this is, but needs must
            self.color = "#" + '{:02x}'.format(random.randint(0, 255)) + '{:02x}'.format(random.randint(0, 255)) + '{:02x}'.format(random.randint(0, 255))
        
        self.start_game()

    def speed(self, val):
        self.game_speed = int((1000 / val) * 10)

    #color change section
    def color(self, val):
        self.color = "yellow"
    
    def perform_actions(self):
        ''' 
        Performs game loop's actions. 
        '''
        if self.check_collisions(): 
            self.end_game()
            return
        self.move_snake()
        self.after(self.game_speed, self.perform_actions) # move snake according to speed setting

    def check_collisions(self):
        ''' 
        Returns a bool that checks for collisions. 
        '''
        head_x, head_y = self.snake_positions[0]

        # borders of play and self-collision
        return (head_x not in range(20, 480) or head_y not in range(20,480) or (head_x, head_y) in self.snake_positions[1:])

    def start_game(self):
        self.snake_positions = [(250, 250), (240, 250), (230, 250)]
        self.direction = "right"
        self.bind_all("<Key>", self.move_random)
        self.pack()
        self.after(self.game_speed, self.perform_actions)
    
    def end_game(self):
        ''' 
        Defines the end of the game. 
        '''
        self.delete(self.find_withtag("snake")) # not working, snake is still there at end of game
        self.delete(tk.ALL)
        self.create_text(250, 250, text="Game over!\nMay the RNG gods bestow\nfavor upon you next time.", fill="white", font=("", 20))

