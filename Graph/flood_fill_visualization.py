import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.colors import ListedColormap

# Grid size
H, W = 30, 30

# Colors: 0=white, 1=black, 2=red
WHITE = 0
BLACK = 1
RED = 2

# Create image matrix
img = np.zeros((H, W), dtype=int)

# Draw black square
img[8:22, 8:22] = BLACK

# Define colormap properly (new matplotlib compatible)
cmap = ListedColormap([
    (1, 1, 1, 1),  # white
    (0, 0, 0, 1),  # black
    (1, 0, 0, 1)  # red
])

plt.ion()
fig, ax = plt.subplots()
im = ax.imshow(img, cmap=cmap, vmin=0, vmax=2)
ax.set_title("Click inside the black square to flood fill")
ax.axis("off")


def flood_fill(x, y):
    target = img[x, y]
    if target == RED:
        return

    q = deque([(x, y)])
    img[x, y] = RED

    while q:
        x, y = q.popleft()

        # to see clockwise action on screen,
        # we need to use the direction as screen coordinates
        # which is col, row
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < W and 0 <= ny < H and img[nx, ny] == target:
                img[nx, ny] = RED
                q.append((nx, ny))

        im.set_data(img)
        plt.draw()
        plt.pause(0.02)



def onclick(event):
    if event.xdata is None or event.ydata is None:
        return
    x, y = int(event.xdata), int(event.ydata)
    # screen coordinate (col, row) == matrix coordinate (row, col)
    flood_fill(y, x)


fig.canvas.mpl_connect("button_press_event", onclick)
plt.show(block=True)
