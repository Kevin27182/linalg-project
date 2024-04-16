import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.animation as animation
import transforms3d
import math







cubeArray = [] #Array that holds all of the cubes (stores each cube's corner array positions)
innerArraySize = 3
cubeArraySize = 2
"""
Ask how many cubes
"""

cubeArraySize = 1

width = float(input("Enter the width of the square: "))

xRotDegree = float(input("Enter the amount of degrees you want to rotate the cube by along the x axis: "))
yRotDegree = float(input("Enter the amount of degrees you want to rotate the cube by along the y axis: "))
zRotDegree = float(input("Enter the amount of degrees you want to rotate the cube by along the z axis: "))

"""
Sets the matrices for the cubes
"""
#How many cubes you want until it prints the final result. u = 1 is the starting matrix, cubeArraySize is the final matrix position
for u in range(cubeArraySize):
    positionsHolder = [] #Create an array that will hold all of the dataHolder arrays 

    #Bottom of cube
    dataHolder = []
    dataHolder.append(0)
    dataHolder.append(0)
    dataHolder.append(0)
    positionsHolder.append(dataHolder)

    dataHolder = []
    dataHolder.append(0)
    dataHolder.append(0)
    dataHolder.append(width)
    positionsHolder.append(dataHolder)

    dataHolder = []
    dataHolder.append(width)
    dataHolder.append(0)
    dataHolder.append(width)
    positionsHolder.append(dataHolder)

    dataHolder = []
    dataHolder.append(width)
    dataHolder.append(0)
    dataHolder.append(0)
    positionsHolder.append(dataHolder)

    #Top of Cube
    dataHolder = []
    dataHolder.append(0)
    dataHolder.append(width)
    dataHolder.append(0)
    positionsHolder.append(dataHolder)

    dataHolder = []
    dataHolder.append(0)
    dataHolder.append(width)
    dataHolder.append(width)
    positionsHolder.append(dataHolder)

    dataHolder = []
    dataHolder.append(width)
    dataHolder.append(width)
    dataHolder.append(width)
    positionsHolder.append(dataHolder)

    dataHolder = []
    dataHolder.append(width)
    dataHolder.append(width)
    dataHolder.append(0)
    positionsHolder.append(dataHolder)


    cubeArray.append(positionsHolder) #Once all of the positionsHolder array has been completed (gathered the corner vertices), it appends it to cubeArray




# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
vertices = np.array([
    [cubeArray[0][0][0], cubeArray[0][0][1], cubeArray[0][0][2]],
    [cubeArray[0][1][0], cubeArray[0][1][1], cubeArray[0][1]][2],
    [cubeArray[0][2][0], cubeArray[0][2][1], cubeArray[0][2]][2],
    [cubeArray[0][3][0], cubeArray[0][3][1], cubeArray[0][3]][2],
    [cubeArray[0][4][0], cubeArray[0][4][1], cubeArray[0][4]][2],
    [cubeArray[0][5][0], cubeArray[0][5][1], cubeArray[0][5]][2],
    [cubeArray[0][6][0], cubeArray[0][6][1], cubeArray[0][6]][2],
    [cubeArray[0][7][0], cubeArray[0][7][1], cubeArray[0][7]][2]
])

# Define the edges of the cube
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Function to update the plot for each frame of the animation
def update(num, verts, ax):
    ax.clear()
    
    ax.set_xlim([-2,2])
    ax.set_ylim([-2,2])
    ax.set_zlim([-2,2])

    updated_verts = np.copy(verts)
    # Rotate each vertex sequentially
    for i, vertex in enumerate(verts):
        # Rotate along x-axis
        if num < xRotDegree:
            R_x = transforms3d.axangles.axangle2mat([1, 0, 0], np.radians(num))
        else:
            R_x = transforms3d.axangles.axangle2mat([1, 0, 0], np.radians(xRotDegree))
        # Rotate along y-axis
        if num > xRotDegree and num < xRotDegree + yRotDegree:
            R_y = transforms3d.axangles.axangle2mat([0, 1, 0], np.radians(num - xRotDegree))
        elif num >= xRotDegree + yRotDegree:
            R_y = transforms3d.axangles.axangle2mat([0, 1, 0], np.radians(yRotDegree))
        else:
            R_y = np.eye(3)  # No rotation
        # Rotate along z-axis
        if num > xRotDegree + yRotDegree and num < xRotDegree + yRotDegree + zRotDegree:
            R_z = transforms3d.axangles.axangle2mat([0, 0, 1], np.radians(num - xRotDegree - yRotDegree))
        elif num >= xRotDegree + yRotDegree + zRotDegree:
            R_z = transforms3d.axangles.axangle2mat([0, 0, 1], np.radians(zRotDegree))
        else:
            R_z = np.eye(3)  # No rotation
        
        R = np.dot(np.dot(R_x, R_y), R_z)
        updated_verts[i] = np.dot(vertex, R)
        
        ax.scatter(*updated_verts[i], color='b')
    
    # Update the edges based on the updated vertices
    updated_edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    for edge in updated_edges:
        ax.plot3D([updated_verts[edge[0]][0], updated_verts[edge[1]][0]],
                  [updated_verts[edge[0]][1], updated_verts[edge[1]][1]],
                  [updated_verts[edge[0]][2], updated_verts[edge[1]][2]], 'r')
    
    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Set the aspect ratio
    ax.set_box_aspect([1,1,1])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=180, fargs=(vertices, ax), interval=50)

# Show the plot
plt.show()