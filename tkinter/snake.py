from tkinter import *
import random

game_width = 1000
game_height = 700
speed = 80
spaace_size = 50
body_parts = 5
snake_color = "#00ff00"
food_color = '#ff0000'
bg_color = "#000000"

class Snake:
    def __init__(self):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0, body_parts):
            self.coordinates.append([0,0])
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + spaace_size, y + spaace_size, fill=snake_color, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (game_width/spaace_size)-1) * spaace_size
        y = random.randint(0, (game_height / spaace_size)-1) * spaace_size

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + spaace_size, y + spaace_size, fill = food_color, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= spaace_size
    elif direction == "down":
        y += spaace_size
    elif direction == "left":
        x -= spaace_size
    elif direction == "right":
        x += spaace_size

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + spaace_size, y + spaace_size, fill=snake_color)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        global body_parts
        score += 1
        body_parts += 1

        label.config(text="Score: {}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    
    if check_collisions(snake):
        game_over()
    
    else:
        window.after(speed, next_turn, snake, food)

def change_direction(new_direction):
    global direction 

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= game_width:
        print("game over") # testing purpose
        return True
    elif y < 0 or y >= game_height:
        print("game over") # testing purpose
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1:]:
            print("game over") # testing purpose
            return True


def game_over():
    global bg_color
    bg_color = "#000000"
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('Courier New', 70), text="Game Over!", fill="red", tag="gameover")

window = Tk()
window.title("Snake")



score = 0
direction = 'down'

label = Label(window, text='Score:{}'.format(score), font=('Tahoma', 48))
label.pack()

canvas = Canvas(window, bg=bg_color, height=game_height, width=game_width)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenwidth()

x = int(screen_width / 2) - (window_width/2)
y = int(screen_height / 2) - (window_height/2)

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Right>', lambda event: change_direction('right'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
