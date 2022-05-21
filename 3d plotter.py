import pygame
import numpy as np
from math import *
pygame.font.init()

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

axes = []

inputpoints=[]

string_input = ""

# all the cube vertices
# axes
axes.append(np.matrix([10, 0, 0]))
axes.append(np.matrix([0, 10, 0]))
axes.append(np.matrix([0, 0, 10]))
axes.append(np.matrix([0, 0, 0]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


projected_points = []

t_axes = [
    [n, n] for n in range(len(axes))
]


def connect_points(i, j, points, color):
    pygame.draw.line(
        screen, color, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


font = pygame.font.SysFont('Comic Sans MS', 15)
string_topmost = font.render(
    """give the point which you want to plot in the terminal""", False, (0, 0, 0))
string_instuctions = font.render(
    """use w,s,a,d,q,e to navigate and to give an input point then press r to start and R to end""", False, (0, 0, 0))

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
                    anglex += 15*(2*np.pi/360)
                elif event.key == pygame.K_s:
                    anglex -= 15*(2*np.pi/360)
                elif event.key == pygame.K_d:
                    angley += 15*(2*np.pi/360)
                elif event.key == pygame.K_a:
                    angley -= 15*(2*np.pi/360)
                elif event.key == pygame.K_e:
                    anglez += 15*(2*np.pi/360)
                elif event.key == pygame.K_q:
                    anglez -= 15*(2*np.pi/360)
                elif event.key == pygame.K_r:
                    string_input=[int(x) for x in input().split()]
                    points.append(np.matrix(string_input))
                        
    # update stuff

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

        np.append(projected2d,(np.dot(projection_matrix, rotated2d)),axis=0)

        x = int(projected2d[0][0] * scale) + centerpoint[0]
        y = int(projected2d[1][0] * scale) + centerpoint[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, BLACK, (x, y), 3)
        i += 1
    # drawing axes
    i = 0
    for point in axes:
        ultrot = np.dot(rotation_z, rotation_y)
        ultrot = np.dot(ultrot, rotation_x)
        rotated2d = np.dot(ultrot, point.reshape((3, 1)))

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + centerpoint[0]
        y = int(projected2d[1][0] * scale) + centerpoint[1]

        t_axes[i] = [x, y]
        pygame.draw.circle(screen, BLACK, (x, y), 3)
        i += 1

    connect_points(0, 3, t_axes, RED)
    connect_points(1, 3, t_axes, GREEN)
    connect_points(2, 3, t_axes, BLUE)

    screen.blit(string_topmost, (0, 0))
    screen.blit(string_instuctions, (0, 15))

    pygame.display.update()
