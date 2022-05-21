from turtle import pos
import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("gravitation")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100

velocity = []
velocity.append(np.matrix([0, 5]))
velocity.append(np.matrix([0, 0]))
velocity.append(np.matrix([-5, 0]))
velocity.append(np.matrix([0, -5]))
velocity.append(np.matrix([5, 0]))
velocity.append(np.matrix([5, 0]))
velocity.append(np.matrix([5, 0]))
velocity.append(np.matrix([5, 0]))
velocity.append(np.matrix([5, 0]))

position = []
position.append(np.matrix([50, 0]))
position.append(np.matrix([0, 0]))
position.append(np.matrix([0, 50]))
position.append(np.matrix([-50, 0]))
position.append(np.matrix([0, -50]))
position.append(np.matrix([0, -50]))
position.append(np.matrix([0, -50]))
position.append(np.matrix([0, -50]))
position.append(np.matrix([0, -50]))

acceleration = []
acceleration.append(np.matrix([0, 0]))
acceleration.append(np.matrix([0, 0]))
acceleration.append(np.matrix([0, 0]))
acceleration.append(np.matrix([0, 0]))
acceleration.append(np.matrix([0, 0]))
acceleration.append(np.matrix([0, 0]))
acceleration.append(np.matrix([0, 0]))
acceleration.append(np.matrix([0, 0]))
acceleration.append(np.matrix([0, 0]))

masses = []
masses.append(1)
masses.append(2)
masses.append(3)
masses.append(4)
masses.append(5)
masses.append(6)
masses.append(7)
masses.append(8)
masses.append(9)

G = 10

centerpoint = [WIDTH/2, HEIGHT/2]  # x, y

points = []

flag = 4

projected_points = [
    [n, n] for n in range(np.size(masses))
]


def connect_points(i, j, points, color):
    pygame.draw.line(
        screen, color, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


clock = pygame.time.Clock()

while True:

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    flag = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    flag = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    flag = 2
    # update stuff
    screen.fill(WHITE)
    # drawining stuff
    i = 0
    while i < np.size(masses):
        force = [0, 0]
        j = 0
        while j < np.size(masses):
            if np.sum(position[j]-position[i]) != 0:
                p = position[j]-position[i]
                a = (G)*(masses[i])*(masses[j])/(np.sum(np.multiply(p, p)))
                force += ((a/(sqrt(np.sum(np.multiply(p, p)))))*p)
            j += 1
        acceleration[i] = force/masses[i]
        velocity[i] = np.add(velocity[i], acceleration[i])
        i += 1
    for i in range(np.size(masses)):
        position[i] = np.add(velocity[i], position[i])
        temp = position[i]+[centerpoint]
        x = int(temp[0, 0])
        y = int(temp[0, 1])
        projected_points[i] = [x, y]
        pygame.draw.circle(screen, BLACK, (x, y), 3+(masses[i]//3))

    pygame.display.update()
