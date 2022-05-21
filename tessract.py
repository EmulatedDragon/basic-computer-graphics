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

scale = 10

centerpoint = [WIDTH/2, HEIGHT/2]  # x, y

anglex = angley = anglez = angle = 0

points = []

flag = 4

tesfold = np.zeros((20, 3))

# all the cube vertices
# 0 inside cube
points.append(np.matrix([-10, -10, 10]))
points.append(np.matrix([10, -10, 10]))
points.append(np.matrix([10,  10, 10]))
points.append(np.matrix([-10, 10, 10]))
points.append(np.matrix([-10, -10, -10]))
points.append(np.matrix([10, -10, -10]))
points.append(np.matrix([10, 10, -10]))
points.append(np.matrix([-10, 10, -10]))
# 3 axes and origin   8
points.append(np.matrix([10, 0, 0]))
points.append(np.matrix([0, 10, 0]))
points.append(np.matrix([0, 0, 10]))
points.append(np.matrix([0, 0, 0]))
# outside cube 12
points.append(np.matrix([-20, -20, 20]))
points.append(np.matrix([20, -20, 20]))
points.append(np.matrix([20,  20, 20]))
points.append(np.matrix([-20, 20, 20]))
points.append(np.matrix([-20, -20, -20]))
points.append(np.matrix([20, -20, -20]))
points.append(np.matrix([20, 20, -20]))
points.append(np.matrix([-20, 20, -20]))


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
    # Tessract fold

    def sign(x):
        if x >= 0:
            return 1
        else:
            return -1
    a = b = c = 0.0
    i = 0
    for point in points[:8]:
        a = point[0, 0]
        b = point[0, 1]
        c = point[0, 2]
        if b == 10 and abs(a) == 10 and abs(c) == 10:
            tesfold[i][0] = 1*sign(a)
            tesfold[i][1] = 1
            tesfold[i][2] = 1*sign(c)
        elif b == 20 and abs(a) == 20 and abs(c) == 20:
            tesfold[i][0] = 0
            tesfold[i][1] = -2
            tesfold[i][2] = 0
        elif b == -20 and abs(a) == 20 and abs(c) == 20:
            tesfold[i][0] = 1*(-1)*sign(a)
            tesfold[i][1] = 1
            tesfold[i][2] = 1*(-1)*sign(c)
        elif b == -10 and abs(a) == 10 and abs(c) == 10:
            tesfold[i][0] = 0
            tesfold[i][1] = 1
            tesfold[i][2] = 0
        else:
            pass
        point[0, 0] += tesfold[i][0]
        point[0, 1] += tesfold[i][1]
        point[0, 2] += tesfold[i][2]
        i += 1
    j = 12
    for point in points[12:]:
        a = point[0, 0]
        b = point[0, 1]
        c = point[0, 2]
        if b == 10 and abs(a) == 10 and abs(c) == 10:
            tesfold[j][0] = 1*sign(a)
            tesfold[j][1] = 1
            tesfold[j][2] = 1*sign(c)
        elif b == 20 and abs(a) == 20 and abs(c) == 20:
            tesfold[j][0] = 0
            tesfold[j][1] = -2
            tesfold[j][2] = 0
        elif b == -20 and abs(a) == 20 and abs(c) == 20:
            tesfold[j][0] = 1*(-1)*sign(a)
            tesfold[j][1] = 1
            tesfold[j][2] = 1*(-1)*sign(c)
        elif b == -10 and abs(a) == 10 and abs(c) == 10:
            tesfold[j][0] = 0
            tesfold[j][1] = 1
            tesfold[j][2] = 0
        else:
            pass
        point[0, 0] += tesfold[j][0]
        point[0, 1] += tesfold[j][1]
        point[0, 2] += tesfold[j][2]
        j += 1

    # update values of rotation
    anglex = 0.2
    angley += 0.04
    anglez = 0

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
    # drawing points

    i = 0
    for point in points:
        ultrot = np.dot(rotation_x, rotation_y)
        ultrot = np.dot(ultrot, rotation_z)
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
    for p in range(4):
        connect_points(p+12, (p+1) % 4+12, projected_points, BLACK)
        connect_points(p+4+12, ((p+1) % 4) + 4+12, projected_points, BLACK)
        connect_points(p+12, (p+4)+12, projected_points, BLACK)
    for p in range(8):
        connect_points(p, p+12, projected_points, BLACK)
    pygame.display.update()
