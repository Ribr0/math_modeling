import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import imageio
import os

def static_point(point, key):
    for i in range(len(point)):
        alpha = np.linspace(0, 2*np.pi, 100)
        x = point[f'point_{i}']['pos'][0] + point[f'point_{i}']['radius'] * np.cos(alpha)
        y = point[f'point_{i}']['pos'][1] + point[f'point_{i}']['radius'] * np.sin(alpha)
        plt.plot(x, y, color=point[f'point_{i}']['color'])

    plt.axis('equal')
    plt.xlim(boundary[0][0], boundary[1][0])
    plt.ylim(boundary[2][1]+2, boundary[0][1]+2)
    plt.savefig(f'pic_{key}')

def check_point(point):

    images = []
    for i in range(len(point)):
        if point[f'point_{i}']['color'] != 'r' and i < 49:
            point[f'point_{i+1}']['color'] = 'b'
            time.sleep(0.1)
            images.append(f'pic_{i}.png')
            static_point(point, i)

    im = []
    # filenames = [f'pic_{i}.png' for i in range(len(point))]
    for image in images:
      im.append(imageio.imread(image))
      os.remove(image)
    imageio.mimsave('movie.gif', im)
    os.remove('pic_0.png')

def move_point(position, radius, color, velocity):
    pass

def run(number, radius, boundary):
    '''
    boundary: [[(x, y) up-left],
               [(x, y) up-right],
               [(x, y) low-left],
               [(x, y) low-right]
              ]
    '''
    position = []
    x = boundary[0][0]
    y = boundary[0][1]
    for i in range(int(number/10)):
        for j in range(10):
            position.append([x, y])
            x += 2 * radius
        y -= 2 * radius
        x = boundary[0][0]

    point = {f'point_{i}': {} for i in range(number)}
    for i in range(len(position)):
        point[f'point_{i}'].update({'pos':position[i], 'radius': 0.5, 'color': 'r'})

    point['point_20']['color'] = 'b'
    static_point(point, 0)
    check_point(point)


boundary = [[-5, 5],
            [5, 5],
            [-5, -5],
            [5, -5]
           ]

run(50, 0.5, boundary)
