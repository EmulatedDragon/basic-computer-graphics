import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D cube")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100

centerpoint = [WIDTH/2, HEIGHT/2]  # x, y

anglex = angley = anglez = angle = 0

points = []

flag = 4

# all the cube vertices
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

points.append(np.matrix([1, 0, 0]))
points.append(np.matrix([0, 1, 0]))
points.append(np.matrix([0, 0, 1]))
points.append(np.matrix([0, 0, 0]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


projected_points = [
    [n, n] for n in range(len(points))
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
    if flag == 0:
        anglex += 0.1
    if flag == 1:
        angley += 0.1
    if flag == 2:
        anglez += 0.1

    rotation_z = np.matrix([
        [cos(anglez), -sin(anglez), 0],
        [sin(anglez), cos(anglez), 0],
        [0, 0, 1],
    ])

    rotation_y = np.matrix([
        [cos(angley), 0, sin(angley)],
        [0, 1, 0],
        [-sin(angley), 0, cos(angley)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(anglex), -sin(anglex)],
        [0, sin(anglex), cos(anglex)],
    ])
    screen.fill(WHITE)
    # drawining stuff

    i = 0
    for point in points:
        ultrot = np.dot(rotation_z, rotation_y)
        ultrot = np.dot(ultrot, rotation_x)
        rotated2d = np.dot(ultrot, point.reshape((3, 1)))

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + centerpoint[0]
        y = int(projected2d[1][0] * scale) + centerpoint[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, BLACK, (x, y), 3)
        i += 1

    for p in range(4):
        connect_points(p, (p+1) % 4, projected_points, BLACK)
        connect_points(p+4, ((p+1) % 4) + 4, projected_points, BLACK)
        connect_points(p, (p+4), projected_points, BLACK)
    connect_points(8, 11, projected_points, RED)
    connect_points(9, 11, projected_points, GREEN)
    connect_points(10, 11, projected_points, BLUE)
    pygame.display.update()
