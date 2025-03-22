
![tests](https://github.com/software-students-spring2025/3-python-package-snake-charmers-on-a-plane/actions/workflows/build.yaml/badge.svg)

# Python Package Exercise

## Description
Have you ever needed to waste more time? Have no fear, random snake is here! With our amazing package, you can play with a little snake that doesn't like listening to you, and try your best to hang out with it as long as possible.

This package will open up a window where you can set the snake's speed and color. You can also summon an inputted amount of apples that the snake can eat, and attempt to command the snake to move around (it may or may not listen). 

## PyPI link
https://pypi.org/project/snakecharmers/0.1.1/

## Function documentation and examples
### move_random(space_key)
This function performs the random movement of the snake for any press of the user's space key, and ensures that you'll be at least mildly frustrated while playing the game. 

- Input: space key pressed
- Output: none

### spawn_apples(apple_num)
This function spawns a user-chosen number of apples. Once all apples have been eaten, or if the snake hits the window boundary, the game is over. 

- Input: number from 1 - 10
- Output: none

### speed(speed_number)
This function configures the speed of the snake, from 0 - 100. The user inputs their desired speed before the game starts.

- Input: number from 0 - 100, inclusive
- Output: none

### color(color_name)
This function configures the color of the snake. If the user does not input a valid color name at the start of the game, the snake's color is randomly picked. 

- Input: name of color (ex. red, lightblue, purple, any_string)
- Output: none

### Demonstration of usage

[Link to Example File](https://github.com/software-students-spring2025/3-python-package-snake-charmers-on-a-plane/example.md)

## Instructions for Contribution to snakecharmers
1. To contribute to the project, first clone our repository:
```
git clone https://github.com/software-students-spring2025/3-python-package-snake-charmers-on-a-plane.git
```

2. Navigate to the repository:
```
cd 3-python-package-snake-charmers-on-a-plane
```

3. Install pipenv, pytest, and create a virtual environment:
```
pip install pipenv
pipenv install pytest
```

4. Activate the virtual environment:
```
pipenv shell
```

5. Make your contributions!

6. After removing any ```*.egg-info``` and ```dist```  directories, upload your contributions to PyPI with:
```
pip install build twine
python -m build
twine upload dist/*
```

## Team Members
Samantha Lin: https://github.com/sal2948

Kurt Lukowitsch: https://github.com/kl3641

Eli Sun: https://github.com/IDislikeName

Ray Ochotta: https://github.com/SnowyOchole

## Installation and setup

To set up and start the game:
1. Install pipenv, if you do not have pipenv installed:
```
pip install pipenv
```
2. Activate virtual environment:
```
pipenv shell
```
3. Install snakecharmers
```
pipenv install snakecharmers
```
4. Navigate to the package directory, then run this command:
```
PYTHONPATH=src python -m snakecharmerpackage
```
5. Have fun with your belligerent snake!
