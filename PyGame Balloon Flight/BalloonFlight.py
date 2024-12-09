# -*- coding: utf-8 -*-
"""
Created on Tue Dec 3 15:40:21 2024

@author: Armando
"""

import pgzrun
from pgzero.builtins import Actor
from random import randint


WIDTH = 800
HEIGHT = 600


balloon = Actor("balloon", (400, 300))

bird = Actor("bird-up", (randint(800, 1600), randint(10, 200)))
bird2 = Actor("bird-up", (randint(800, 1600), randint(10, 200)))

house = Actor("house", (randint(800, 1600), 460))
house2 = Actor("house", (randint(800, 1600), 460))

tree = Actor("tree", (randint(800, 1600), 450))
tree2 = Actor("tree", (randint(800, 1600), 450))


bird_up = True
bird2_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
life = 100


filename = r"C:\Users\Armando\Desktop\PyGame Balloon Flight\BallonFlightHighScore.txt"
scores = []


def update_high_scores():
    """Update high scores in the file."""
    global score, scores
    try:
        with open(filename, "r") as file:
            scores = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        scores = []

    scores.append(score)
    scores = sorted(scores, reverse=True)[:5]

    with open(filename, "w") as file:
        for high_score in scores:
            file.write(f"{high_score}\n")


def display_high_scores():
    """Display the high scores on the screen."""
    screen.draw.text("GAME OVER", (300, 100), color="red", fontsize=50)
    screen.draw.text("HIGH SCORES", (300, 150), color="black", fontsize=40)
    y = 200
    for position, high_score in enumerate(scores, start=1):
        screen.draw.text(f"{position}. {high_score}", (300, y), color="black", fontsize=30)
        y += 40


def draw():
    """Draw game elements."""
    screen.blit("background", (0, 0))
    if not game_over:
        balloon.draw()
        bird.draw()
        bird2.draw()
        house.draw()
        tree.draw()
        house2.draw()
        tree2.draw()
        screen.draw.text(f"HP: {life}", (375, 5), color="black", fontsize=30)
        screen.draw.text(f"Score: {score}", (650, 5), color="black", fontsize=30)
    else:
        display_high_scores()


def on_mouse_down():
    """Handle mouse button press."""
    global up
    up = True
    balloon.y -= 50


def on_mouse_up():
    """Handle mouse button release."""
    global up
    up = False


def flap():
    """Toggle bird animation."""
    global bird_up, bird2_up
    bird.image = "bird-down" if bird_up else "bird-up"
    bird_up = not bird_up
    bird2.image = "bird-down" if bird2_up else "bird-up"
    bird2_up = not bird2_up


def update():
    global game_over, score, number_of_updates, life

    if not game_over:
      
        if not up:
            balloon.y += 1

       
        if bird.x > 0:
            bird.x -= 4
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1

        if bird2.x > 0:
            bird2.x -= 8
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird2.x = randint(800, 1600)
            bird2.y = randint(10, 200)
            score += 1

        
        if house.right > 0:
            house.x -= 2
        else:
            house.x = randint(800, 1600)
            score += 1

        if house2.right > 0:
            house2.x -= 2
        else:
            house2.x = randint(800, 1600)
            score += 1

        
        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            score += 1

        if tree2.right > 0:
            tree2.x -= 2
        else:
            tree2.x = randint(800, 1600)
            score += 1

        
        if balloon.top < 0 or balloon.bottom > 560:
            life -= 1

            if life == 0:
                game_over = True
                update_high_scores()

    
        if balloon.collidepoint(bird.x, bird.y) or \
           balloon.collidepoint(bird2.x, bird2.y) or \
           balloon.collidepoint(house.x, house.y) or \
           balloon.collidepoint(tree.x, tree.y) or \
           balloon.collidepoint(house2.x, house2.y) or \
           balloon.collidepoint(tree2.x, tree2.y):
            life -= 1
            if life == 0:
                game_over = True
                update_high_scores()


pgzrun.go()
