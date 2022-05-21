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

arm_length = 100
position = [0, 0]
omega = 0
theta = 0
alpha = 0
masses = 10
tau = 0
G = [0, 1]
force = [0, 0]
tension = 0

arm_length1 = 100
position1 = [0, 0]
omega1 = 0
theta1 = 0
alpha1 = 0
masses1 = 10
tau1 = 0
force1 = [0, 0]
tension2 = 0

centerpoint = [WIDTH/2, HEIGHT/2]  # x, y


def sign(x):
    if x < 0:
        return -1
    else:
        return 1


def connect_points(i, j, a, b, color):
    pygame.draw.line(
        screen, color, (i, j), (a, b))


clock = pygame.time.Clock()

screen.fill(WHITE)

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

    force[0] = 0+(tension2*np.cos((theta1/180)*2*pi))
    force[1] = masses*G[1]+(tension2*np.sin((theta1/180)*2*pi))
    radial_force = (force[1]*np.cos((theta/180)*2*pi) +
                    force[0]*np.sin((theta/180)*2*pi))
    tau = (force[1]*np.cos((theta/180)*2*pi)+force[0]
           * np.sin((theta/180)*2*pi))*arm_length*0.3
    tension = (force[0]*np.cos((theta/180)*2*pi) +
               force[1]*np.sin((theta/180)*2*pi))
    alpha = tau/(masses*(arm_length ^ 2))
    omega += alpha
    theta += omega
    position[0] = arm_length*np.cos((theta/180)*2*pi)
    position[1] = arm_length*np.sin((theta/180)*2*pi)
    temp = [position[0]+centerpoint[0], position[1]+centerpoint[1]]
    x = int(temp[0])
    y = int(temp[1])

    force1[0] = 0+(tension*np.cos((theta/180)*2*pi)) - \
        (radial_force*np.sin((theta/180)*2*pi))
    force1[1] = masses1*G[1]+(tension*np.sin((theta/180)*2*pi)) - \
        (radial_force*np.cos((theta/180)*2*pi))
    tau1 = (force1[1]*np.cos((theta1/180)*2*pi)+force1[0]
            * np.sin((theta1/180)*2*pi))*arm_length1*0.3
    tension2 = (force1[0]*np.cos((theta1/180)*2*pi) +
                force1[1]*np.sin((theta1/180)*2*pi))
    alpha1 = tau1/(masses1*(arm_length1 ^ 2))
    omega1 += alpha1
    theta1 += omega1
    position1[0] = position[0]+(arm_length1*np.cos((theta1/180)*2*pi))
    position1[1] = position[1]+(arm_length1*np.sin((theta1/180)*2*pi))
    temp1 = [position1[0]+centerpoint[0], position1[1]+centerpoint[1]]
    x1 = int(temp1[0])
    y1 = int(temp1[1])

    pygame.draw.circle(screen, BLACK, (centerpoint[0], centerpoint[1]), 1)
    pygame.draw.circle(screen, BLACK, (x, y), 3+(masses//3))
    pygame.draw.circle(screen, BLACK, (x1, y1), 3+(masses1//3))
    connect_points(x, y, centerpoint[0], centerpoint[1], BLACK)
    connect_points(x, y, x1, y1, BLACK)
    pygame.display.update()
