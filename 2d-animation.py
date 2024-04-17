
# Reference: Linear Algebra with Applications by Jeffery Holt, p. 103

import numpy as np
import matplotlib.pyplot as plt, matplotlib.animation as anim
import sys, os

fpath = os.path.dirname(sys.argv[0])

def genPoints(theta, start_points, anim_num_frames = 250):
    """Function that generates the point data to drive a rotation animation"""

    dtheta = theta / (anim_num_frames - 1)

    drot_matrix = np.array([[np.cos(dtheta), -np.sin(dtheta)],
                            [np.sin(dtheta),  np.cos(dtheta)]])

    prev_frame = start_points
    anim_frames = start_points

    for i in range(1, anim_num_frames):

        new_frame = np.linalg.multi_dot([drot_matrix, prev_frame])
        anim_frames = np.vstack([anim_frames, new_frame])
        prev_frame = new_frame

    for i in range(50):
        anim_frames = np.vstack([anim_frames[0:2], anim_frames])

    for i in range(50):
        anim_frames = np.vstack([anim_frames, anim_frames[-2:]])

    return anim_frames

def animatePoints(frames, save = False, name = "2d-anim.gif", color="tab:blue"):
    """Animates given frames (takes as input: (2*n, 4) ndarray, where n is the number of animation frames)"""

    plt_size = 0
    for i in range(frames.shape[1]):

        x = frames[0][i]
        y = frames[1][i]
        norm = np.sqrt(x ** 2 + y ** 2)
        if (norm * 1.2 > plt_size): plt_size = norm * 1.2

    figure, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim([-plt_size, plt_size])
    ax.set_ylim([-plt_size, plt_size])
    poly = plt.fill(frames[0],frames[1],color)
    num_frames = (int)(frames.shape[0] / 2)

    def update(i): 
        """Callback function for animation"""

        poly[0].set_xy(frames[2 * i : 2 * i + 2].T)
        return poly

    ani = anim.FuncAnimation(figure, update, frames = list(range(num_frames)), interval = 20, blit = True, repeat = False)
    if save : ani.save(fpath + "\\{}".format(name), fps = 30)  

    plt.show()

# Hexagon, for fun
phi = np.pi / 3
hex_points = np.array([ [np.cos(phi * 0), np.cos(phi * 1), np.cos(phi * 2), np.cos(phi * 3), np.cos(phi * 4), np.cos(phi * 5)],
                        [np.sin(phi * 0), np.sin(phi * 1), np.sin(phi * 2), np.sin(phi * 3), np.sin(phi * 4), np.sin(phi * 5)] ])

# Regular ole square
square_points = np.array([[-0.5,  0.5,  0.5, -0.5],
                          [-0.5, -0.5,  0.5,  0.5]])

my_square_frames = genPoints(np.pi / 4, square_points, anim_num_frames = 50)
animatePoints(my_square_frames, save = False, name = "2d-anim-square.gif")

my_hex_frames = genPoints(-np.pi, hex_points, anim_num_frames = 100)
animatePoints(my_hex_frames, save = False, name = "2d-anim-hex.gif", color = "firebrick")