import json
import matplotlib.pyplot as plt
import numpy as np
import os


def plot_camera_positions_with_direction(json_data):
    # Load JSON data
    data = json.loads(json_data)

    # Function to extract camera positions and orientation vectors from the transformation matrix
    def extract_camera_position_and_orientation(matrix):
        position = matrix[:3, 3]
        matrix[0:3, 2] *= -1
        orientation = matrix[:3, :3]  # Assuming the camera is looking in the +Z direction
        return position, orientation

    # Function to plot camera orientation arrows
    def plot_orientation_arrows(position, orientation, arrow_length=0.5):
        x_axis = np.array(orientation[:, 0])
        y_axis = np.array(orientation[:, 1])
        z_axis = np.array(orientation[:, 2])

        arrow_end = position + arrow_length * z_axis
        ax.quiver(position[0], position[1], position[2],
                  arrow_end[0], arrow_end[1], arrow_end[2],
                  color='k', label='Direction', alpha=0.8)

    # Function to plot camera frustums
    def plot_camera_frustum(position, orientation, depth=1.0, width=0.5, height=0.5):
        z_axis = np.array(orientation[:, 2])

        # Compute frustum corners
        corners = [
            position,
            position + depth * z_axis + 0.5 * width * orientation[:, 0] + 0.5 * height * orientation[:, 1],
            position + depth * z_axis + 0.5 * width * orientation[:, 0] - 0.5 * height * orientation[:, 1],
            position + depth * z_axis - 0.5 * width * orientation[:, 0] + 0.5 * height * orientation[:, 1],
            position + depth * z_axis - 0.5 * width * orientation[:, 0] - 0.5 * height * orientation[:, 1],
        ]

        # Connect the corners to form the frustum
        for i in range(4):
            ax.plot([corners[0][0], corners[i + 1][0]],
                    [corners[0][1], corners[i + 1][1]],
                    [corners[0][2], corners[i + 1][2]], color='b', alpha=0.5)

        ax.plot([corners[1][0], corners[2][0]], [corners[1][1], corners[2][1]], [corners[1][2], corners[2][2]],
                color='b', alpha=0.5)
        ax.plot([corners[1][0], corners[4][0]], [corners[1][1], corners[4][1]], [corners[1][2], corners[4][2]],
                color='b', alpha=0.5)
        ax.plot([corners[2][0], corners[3][0]], [corners[2][1], corners[3][1]], [corners[2][2], corners[3][2]],
                color='b', alpha=0.5)
        ax.plot([corners[3][0], corners[4][0]], [corners[3][1], corners[4][1]], [corners[3][2], corners[4][2]],
                color='b', alpha=0.5)

    # Initialize lists to store camera positions and orientation vectors
    camera_positions_x = []
    camera_positions_y = []
    camera_positions_z = []

    # Plot the camera positions and orientation vectors in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Extract camera positions and orientation vectors from each frame's transformation matrix
    for frame in data["frames"]:
        matrix = np.array(frame["transform_matrix"])
        camera_position, orientation_vector = extract_camera_position_and_orientation(matrix)
        camera_positions_x.append(camera_position[0])
        camera_positions_y.append(camera_position[1])
        camera_positions_z.append(camera_position[2])

        # Plot camera frustum
        # plot_camera_frustum(camera_position, orientation_vector)

    ax.scatter(camera_positions_x, camera_positions_y, camera_positions_z, marker='o', s=10)
    ax.scatter(camera_positions_x[0], camera_positions_y[0], camera_positions_z[0], marker='o', s=15, color='red')
    ax.scatter(camera_positions_x[-1], camera_positions_y[-1], camera_positions_z[-1], marker='o', s=15, color='red')


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Camera Positions')
    plt.show()


# Example usage:
# Assuming your JSON data is stored in a file called 'transforms.json'

# Uncomment the following for camera positions visualization:

# with open('transforms.json', 'r') as file:
#     json_data = file.read()
# plot_camera_positions_with_direction(json_data)

