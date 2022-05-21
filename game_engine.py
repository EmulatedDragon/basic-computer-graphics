import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 1500, 800
pygame.display.set_caption("finite projection view")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100

camera = np.array([0.0, 0.0, -20.0])

camera_plane = np.array([0.0, 0.0, -10.0])

viewangle = 0

moveflag = 0

centerpoint = [WIDTH/2, HEIGHT/2]  # x, y

points = []

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

# all the cube vertices


def points_on_graph():
    points.append(np.matrix([-1, -1, 1]))
    points.append(np.matrix([1, -1, 1]))
    points.append(np.matrix([1,  1, 1]))
    points.append(np.matrix([-1, 1, 1]))
    points.append(np.matrix([-1, -1, -1]))
    points.append(np.matrix([1, -1, -1]))
    points.append(np.matrix([1, 1, -1]))
    points.append(np.matrix([-1, 1, -1]))

    points.append(np.matrix([10, 0, 0]))
    points.append(np.matrix([0, 10, 0]))
    points.append(np.matrix([0, 0, 10]))
    points.append(np.matrix([0, 0, 0]))


points_on_graph()

projected_points = [
    [n, n] for n in range(len(points))
]


def connect_points(i, j, points, color):
    pygame.draw.line(
        screen, color, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


clock = pygame.time.Clock()
while True:

    clock.tick(60)

    # taking input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_d:
                moveflag = 1
            if event.key == pygame.K_a:
                moveflag = 2
            if event.key == pygame.K_w:
                moveflag = 3
            if event.key == pygame.K_s:
                moveflag = 4
            if event.key == pygame.K_e:
                moveflag = 5
            if event.key == pygame.K_q:
                moveflag = 6
        if event.type == pygame.KEYUP:
            moveflag = 0

    XUX = sqrt(((camera_plane[2]-camera[2])**2) /
               (((camera_plane[2]-camera[2])**2)+((camera_plane[0]-camera[0])**2)))
    ZUX = sqrt(((camera_plane[0]-camera[0])**2) /
               (((camera_plane[2]-camera[2])**2)+((camera_plane[0]-camera[0])**2)))

    def findsign(x):
        if x < 0:
            return -1
        else:
            return 1
    if moveflag == 1:
        camera[0] += XUX*0.2
        camera[2] += ZUX*0.2
        camera_plane[0] += XUX*0.2
        camera_plane[2] += ZUX*0.2
    elif moveflag == 2:
        camera[0] -= XUX*0.2
        camera[2] -= ZUX*0.2
        camera_plane[0] -= XUX*0.2
        camera_plane[2] -= ZUX*0.2
    elif moveflag == 3:
        camera += 0.2*(camera_plane-camera)/10
        camera_plane += 0.2*(camera_plane-camera)/10
    elif moveflag == 4:
        camera -= 0.2*(camera_plane-camera)/10
        camera_plane -= 0.2*(camera_plane-camera)/10
    elif moveflag == 5:
        viewangle += 0.2*(5/360)*2*np.pi
        camera_plane[0] = camera[0]+5*np.sin(viewangle)
        camera_plane[2] = camera[2]+5*np.cos(viewangle)
    elif moveflag == 6:
        viewangle -= 0.2*(5/360)*2*np.pi
        camera_plane[0] = camera[0]+5*np.sin(viewangle)
        camera_plane[2] = camera[2]+5*np.cos(viewangle)
    else:
        pass
    screen.fill(WHITE)
    # drawining stuff
    i = 0
    is_visible = 1
    for point in points:

        slope_ray = np.array(point-camera)
        normal_plane = np.array(camera_plane-camera)
        t = np.sum(normal_plane*normal_plane)
        t = t/(np.sum(slope_ray*normal_plane))
        i_point = np.array(camera+(slope_ray*t))
        temp = ((i_point[0][0]-camera_plane[0]) /
                XUX) if XUX != 0 else ((i_point[0][2]-camera_plane[2])/ZUX)
        x = int(temp * scale) + centerpoint[0]
        y = int((i_point[0][1]-camera_plane[1]) * scale) + centerpoint[1]
        projected_points[i] = [x, y]
        if is_visible > abs(t):
            is_visible = t
        i += 1
    if 0 <= is_visible <= 1:
        for p in projected_points:
            pygame.draw.circle(screen, BLACK, (p[0], p[1]), 3)
        connect_points(0, 1, projected_points, BLACK)
        connect_points(4, 5, projected_points, BLACK)
        connect_points(0, 4, projected_points, BLACK)
        connect_points(1, 2, projected_points, BLACK)
        connect_points(5, 6, projected_points, BLACK)
        connect_points(1, 5, projected_points, BLACK)
        connect_points(2, 3, projected_points, BLACK)
        connect_points(6, 7, projected_points, BLACK)
        connect_points(2, 6, projected_points, BLACK)
        connect_points(3, 0, projected_points, BLACK)
        connect_points(7, 4, projected_points, BLACK)
        connect_points(3, 7, projected_points, BLACK)
        connect_points(8, 11, projected_points, RED)
        connect_points(9, 11, projected_points, GREEN)
        connect_points(10, 11, projected_points, BLUE)
    pygame.display.update()
