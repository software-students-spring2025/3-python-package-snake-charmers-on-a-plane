import tkinter as tk
from PIL import ImageColor
from tkinter import ttk
import random
from snakecharmerpackage.settings import Settings

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
        self.master = master
        self.master.settings = {"speed": 50}
        self.master.color_settings = {"color": "yellow"}
        self.wait_for_settings()
        
        self.pack()

        self.after(100, self.perform_actions)

    def draw(self):
        self.delete("snake")
        for x, y in self.snake_positions:
            self.create_rectangle(x, y, x + 10, y + 10, fill=self.color, tag="snake")

    def spawn_apples(self,num):
        for i in range(num):
            x = random.randint(0, 49)*10
            y = random.randint(0,49)*10
            apple = self.create_oval(x, y, x+10, y+10, fill='red')
            self.apples.append(apple)
            self.apple_positions.append((x,y))
        self.new_window.destroy()
        
    def check_apple(self):
        head_x, head_y = self.snake_positions[0]
        for i, (apple_x, apple_y) in enumerate(self.apple_positions):
            if apple_x <= head_x < apple_x + 10 and apple_y <= head_y < apple_y + 10: # previously 15 each
                self.delete(self.apples.pop(i))
                self.apple_positions.pop(i)
                self.score += 10
                score = self.find_withtag("score")
                self.itemconfigure(score, text=f"Score: {self.score}", tag="score")
                
                # if player gets all apples
                if self.score == (int(self.n.get()) * 10):
                    self.end_game()
                return True
        return False

    def move_snake(self):
        '''
        Defines movement for the snake.
        '''
        head_x, head_y = self.snake_positions[0]

        if self.direction == "none":
            self.draw()
            return 

        if self.direction == "left":
            new_head_pos = (head_x - move_size, head_y)
        elif self.direction == "right":
            new_head_pos = (head_x + move_size, head_y)
        elif self.direction == "down":
            new_head_pos = (head_x, head_y + move_size)
        elif self.direction == "up":
            new_head_pos = (head_x, head_y - move_size)

        if self.check_apple():
            self.snake_positions.insert(0,new_head_pos)
        else:
            # replace head with body
            self.snake_positions = [new_head_pos] + self.snake_positions[:-1]

        self.draw()

    def move_random(self, event):
        ''' 
        Randomizes the snake's movement. 
        '''
        all_directions = ["up", "down", "left", "right"]
        opposites = ({"up", "down"}, {"left", "right"})

        print("Current snake direction:", self.direction)

        if self.direction != "none":
            all_directions.remove(self.direction)
            random_direction = random.choice(all_directions)
            if {random_direction, self.direction} in opposites:
                all_directions.remove(random_direction)
                random_direction = random.choice(all_directions) # make next direction != current direction
                all_directions.append(random_direction)

            all_directions.append(self.direction)
        else:
            random_direction = random.choice(all_directions)

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
        return (head_x not in range(10, 490) or head_y not in range(10,490) or (head_x, head_y) in self.snake_positions[1:])

    def apple_window(self):
        self.n = tk.StringVar() 
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Apples")
        self.new_window.geometry("300x200")
        # Speed
        ttk.Label(self.new_window, text="Enter apples to spawn (1-10):").pack(pady=5)
        apple_entry = ttk.Entry(self.new_window, textvariable=self.n)
        #self.apple_num = int(self.n.get()) # for tracking score
        apple_entry.pack()
        # button
        start_button = tk.Button(self.new_window, text="Spawn", command=lambda: self.spawn_apples(int(self.n.get())), bg="lightgray", fg="black")
        start_button.pack(pady=10)

    def start_game(self):

        self.snake_positions = [(250, 250), (240, 250), (230, 250)]
        self.direction = "none"  # so the snake doesn't move until the player presses space
        self.bind_all("<space>", self.move_random)
        self.apples = []
        self.apple_positions = []
        self.score = 0
        self.color = self.color
        self.apple_window()
        self.create_text(35, 12, text=f"Score: {self.score}", tag="score", fill="white", font=(10))
        self.create_text(
            250, 230,
            text="Press Space to randomly slither around!",
            fill="white",
            font=("", 15))
        self.pack()
        self.after(self.game_speed, self.perform_actions)

    def end_game(self):
        '''Ends the game and displays the Game Over screen.'''
        self.delete(self.find_withtag("snake"))
        self.delete(tk.ALL)  # Clear canvas
        self.create_text(
            250, 250,
            text="Game over!\nMay the RNG gods bestow\nfavor upon you next time.",
            fill="white",
            font=("", 20),
            tag="game_over")
        self.after_cancel(self.perform_actions)
