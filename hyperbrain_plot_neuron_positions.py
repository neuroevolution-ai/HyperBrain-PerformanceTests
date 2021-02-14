import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation

matplotlib.use('Qt5Agg')


def get_circle_points(n):
    circle_x = np.zeros(n)
    circle_y = np.zeros(n)
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)

    for i in range(n):
        circle_x[i] = 0.45*np.cos(t[i])+0.5
        circle_y[i] = 0.45*np.sin(t[i])+0.5

    return circle_x, circle_y


def get_rgb_points(width, height):
    space_x = np.linspace(0, 1, width)
    space_y = np.linspace(0, 1, height)

    grid_x, grid_y = np.meshgrid(space_x, space_y)

    x = grid_x.flatten()
    y = grid_y.flatten()

    return x, y


def update_plot(i):
    if i == 0:
        global t_start
        t_start = time.time()
        print(i)

    scat_red_inputs.set_array(color_data[i])
    scat_green_inputs.set_array(color_data[i])
    scat_blue_inputs.set_array(color_data[i])

    if i == number_frames-1:
        print((time.time() - t_start))
        print(i)
    return


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=3, metadata=dict(artist='Me'), bitrate=-1)

number_frames = 100
input_image_width = 64
input_image_height = 64
red_z = 1.3
green_z = 1.6
blue_z = 1.9
number_neurons = 5000
number_outputs = 16
outputs_z = -0.5

# Inputs from rgb meshgrids
rgb_x, rgb_y = get_rgb_points(input_image_width, input_image_height)

# CTRNN Neurons are randomly placed in a cube with length = 1
neurons_x, neurons_y, neurons_z = np.random.random((3, number_neurons))

# Outputs as a circle
outputs_x, outputs_y = get_circle_points(number_outputs)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

color_red = np.random.random(input_image_width*input_image_height)
color_green = np.random.random(input_image_width*input_image_height)
color_blue = np.random.random(input_image_width*input_image_height)
color_data = np.random.random((number_frames, input_image_width*input_image_height))

scat_red_inputs = ax.scatter(rgb_x, rgb_y, red_z, c=color_red, s=15, edgecolors='none', cmap="Reds", alpha=0.7)
scat_green_inputs = ax.scatter(rgb_x, rgb_y, green_z, c=color_green, s=15, edgecolors='none', cmap="Greens", alpha=0.7)
scat_blue_inputs = ax.scatter(rgb_x, rgb_y, blue_z, c=color_blue, s=15, edgecolors='none', cmap="Blues", alpha=0.7)
scat_neurons = ax.scatter(neurons_x, neurons_y, neurons_z, c="Black", s=15, edgecolors='none')
scat_outputs = ax.scatter(outputs_x, outputs_y, outputs_z, c="Orange", s=30, edgecolors='none')

ani = animation.FuncAnimation(fig, update_plot, frames=100, repeat=False, interval=20)

# Set Plot to Fullscreen
manager = plt.get_current_fig_manager()
manager.window.showMaximized()

# plt.show()

# ani.save('lines.mp4', writer=writer)

print("Finished")
