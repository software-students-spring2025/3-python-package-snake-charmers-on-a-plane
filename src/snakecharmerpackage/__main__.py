from random_snake import RandomSnake
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Random Snake")
    snake = RandomSnake(root)
    root.mainloop()
