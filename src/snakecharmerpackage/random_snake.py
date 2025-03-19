import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import random
from settings import Settings

move_size = 10 # pixels

# includes window, since I need window to see snake movement
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
        self.wait_for_settings()

        # initialize
        initial_x, initial_y = random.randint(100, 400), random.randint(100, 400) # spawn within center area
        self.snake_positions = [(initial_x, initial_y), (initial_x - 20, initial_y), (initial_x - 40, initial_y)] # positions of three segments
        self.load_asset()
        self.create_snake()
        
        # set up game loop
        self.direction = "right"
        self.bind_all("<Key>", self.move_random) # listens for any key press
        self.score = 0
        
        self.pack()

        self.after(100, self.perform_actions)

    def load_asset(self):
        '''
        Loads snake segment asset.
        '''
        self.snake_img = Image.open("snake.png")
        self.snake_body = ImageTk.PhotoImage(self.snake_img)

    def create_snake(self):
        '''
        Creates snake segment asset.
        '''
        for x, y in self.snake_positions:
            self.create_image(x, y, image=self.snake_body, tag="snake") # tag works similarly to class in css

    def draw(self):
        self.delete("snake")
        for x, y in self.snake_positions:
            self.create_rectangle(x, y, x + 10, y + 10, fill="yellow", tag="snake")


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

        # I don't think this loop is necessary anymore
        '''snake_segments = self.find_withtag("snake") # list
        for segment, pos in zip(snake_segments, self.snake_positions):
            self.coords(segment, pos) # update positions'''

        self.draw()

    def move_random(self, event):
        ''' Randomizes the snake's movement. '''
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
        self.start_game()

    def speed(self, val):
        self.game_speed = int((1000 / val) * 10)
    
    def perform_actions(self):
        ''' Performs game loop's actions. '''
        if self.check_collisions(): 
            self.end_game()
        self.move_snake()
        self.after(self.game_speed, self.perform_actions) # move snake every 100 ms

    def check_collisions(self):
        ''' Returns a bool that checks for collisions. '''
        head_x, head_y = self.snake_positions[0]

        # borders of play and self-collision
        return (head_x not in range(20, 480) or head_y not in range(20,480) or (head_x, head_y) in self.snake_positions[1:])

    def start_game(self):
        self.snake_positions = [(250, 250), (230, 250), (210, 250)]
        self.load_asset()
        self.create_snake()
        self.direction = "right"
        self.bind_all("<Key>", self.move_random)
        self.pack()
        self.after(self.game_speed, self.perform_actions)
    
    def end_game(self):
        ''' Defines the end of the game. '''
        self.delete(tk.ALL)
        self.create_text(250, 250, text="Game over!\nMay the RNG gods bestow\nfavor upon you next time.", fill="white", font=("", 20))

#This is now done in main
'''# create game window
root = tk.Tk()
root.title("random snake!")
root.tk.call("tk", "scaling", 4.0)

# start game
snake = RandomSnake()
root.mainloop()'''
