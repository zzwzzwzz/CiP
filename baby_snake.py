from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, 'blue')
    goal = canvas.create_rectangle(360, 360, 360+SIZE, 360+SIZE, 'red')

    points = 0 
    
    # Animation loop
    while True:
        key = canvas.get_last_key_press()

        if key == 'ArrowLeft':
            canvas.move(player, -SIZE, 0)
        if key == 'ArrowRight':
            canvas.move(player, SIZE, 0)
        if key == 'ArrowUp':
            canvas.move(player, 0, -SIZE)
        if key == 'ArrowDown':
            canvas.move(player, 0, SIZE)

        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)

        if player_x < 0 or player_x >= CANVAS_WIDTH or player_y < 0 or player_y >= CANVAS_HEIGHT:
            print("Game Over!")
            break

        if player_hits_goal(canvas, player, goal):
            points += 1  # Increment points when player hits goal
            print("Points:", points) 
            move_goal(canvas, goal)

        time.sleep(DELAY)

def player_hits_goal(canvas, player, goal):
    player_x1 = canvas.get_left_x(player)
    player_y1 = canvas.get_top_y(player)
    player_x2 = player_x1 + SIZE
    player_y2 = player_y1 + SIZE

    goal_x1 = canvas.get_left_x(goal)
    goal_y1 = canvas.get_top_y(goal)
    goal_x2 = goal_x1 + SIZE
    goal_y2 = goal_y1 + SIZE

    return (player_x1 < goal_x2 and player_x2 > goal_x1 and player_y1 < goal_y2 and player_y2 > goal_y1)

def move_goal(canvas, goal):
    new_x = random.randint(0, (CANVAS_WIDTH - SIZE) // SIZE) * SIZE
    new_y = random.randint(0, (CANVAS_HEIGHT - SIZE) // SIZE) * SIZE

    canvas.move(goal, new_x - canvas.get_left_x(goal), new_y - canvas.get_top_y(goal))

if __name__ == '__main__':
    main()