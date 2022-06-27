import numpy as np
import cv2

import src

# Load data
print('Load data...')
data = np.load('hw3.npy', allow_pickle = True)

verts = data[()]['verts']
vertex_colors = data[()]['vertex_colors']
face_indices = data[()]['face_indices']
depth = data[()]['depth']
cam_eye = data[()]['cam_eye']
cam_up = data[()]['cam_up']
cam_lookat = data[()]['cam_lookat']
ka = data[()]['ka']
kd = data[()]['kd']
ks = data[()]['ks']
n = data[()]['n']
light_positions = data[()]['light_positions']
light_intensities = data[()]['light_intensities']
Ia = data[()]['Ia']
M = data[()]['M']
N = data[()]['N']
W = data[()]['W']
H = data[()]['H']
bg_color = data[()]['bg_color']

print('Done!')

# Gouraud ambient
print('Render image gouraud_ambient...')
img = src.render_object('gouraud', 70, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, ka, 0, 0, np.array(light_positions), np.array(light_intensities), Ia)
cv2.imwrite(
    '1.gouraud_ambient.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print('Done!')

# Gouraud diffuse
print('Render image gouraud_diffuse...')

img = src.render_object('gouraud', 70, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, 0, kd, 0, np.array(light_positions), np.array(light_intensities), Ia)
cv2.imwrite(
    '2.gouraud_diffuse.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print('Done!')

# Gouraud specular
print('Render image gouraud_specular...')

img = src.render_object('gouraud', 70, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, 0, 0, ks, np.array(light_positions), np.array(light_intensities), Ia)
cv2.imwrite(
    '3.gouraud_specular.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print('Done!')

# Gouraud all
print('Render image gouraud_all...')

img = src.render_object('gouraud', 70, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, ka, kd, ks, np.array(light_positions), np.array(light_intensities), Ia)
cv2.imwrite(
    '4.gouraud_all.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print('Done!')