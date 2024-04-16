
# Reference: Linear Algebra with Applications by Jeffery Holt, p. 103

import numpy as np
import matplotlib.pyplot as plt
import time

# Function that generates the point data to drive a rotation animation
def genPoints(theta, start_points, anim_num_frames = 60):

    dtheta = theta / (anim_num_frames - 1)

    drot_matrix = np.array([[np.cos(dtheta), -np.sin(dtheta)],
                            [np.sin(dtheta),  np.cos(dtheta)]])

    prev_frame = start_points
    anim_frames = start_points

    for i in range(1, anim_num_frames):
        new_frame = np.linalg.multi_dot([drot_matrix, prev_frame])
        anim_frames = np.vstack([anim_frames, new_frame])
        prev_frame = new_frame

    return anim_frames

def animatePoints(frames):
    
    num_frames = (int)(frames.shape[0] / 2)

    plt.ion()
    figure, ax = plt.subplots(figsize=(6, 6))
    
    plt_size = 0

    for i in range(frames.shape[1]):

        x = frames[0][i]
        y = frames[1][i]
        norm = np.sqrt(x ** 2 + y ** 2)

        if (norm * 1.2 > plt_size): plt_size = norm * 1.2
    
    for i in range(num_frames):

        ax.set_xlim([-plt_size, plt_size])
        ax.set_ylim([-plt_size, plt_size])
        
        x = frames[2 * i]
        y = frames[2 * i + 1]

        plt.fill(x, y, "r")

        figure.canvas.draw()
        figure.canvas.flush_events()

        if i == 0: time.sleep(1)
        ax.clear()

example_points = np.array([[-0.5,  0.5,  0.5, -0.5],
                           [-0.5, -0.5,  0.5,  0.5]])

my_frames = genPoints(np.pi / 4, example_points, 30)
animatePoints(my_frames)

time.sleep(5)