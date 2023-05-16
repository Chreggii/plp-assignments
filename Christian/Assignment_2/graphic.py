import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os

plt.style.use('dark_background')  # comment out for "light" theme
plt.rcParams["font.size"] = 16

dir = "d:\Privat\git\plp-assignments\Christian\Assignment_2" if os.getcwd(
) == "d:\Privat\git\plp-assignments" else os.getcwd()


class Graphic():

    def __init__(self, array, n, sorter, fps):
        self.array = array
        self.n = n
        self.sorter = sorter
        self.fps = fps

        # fig, ax = plt.subplots(figsize=(16, 8))
        # self.container = ax.bar(np.arange(0, len(array), 1),
        #                         array.full_copies[0], align="edge", width=0.8)
        # fig.suptitle(f"{sorter} sort")
        # ax.set(xlabel="Index", ylabel="Value")
        # ax.set_xlim([0, n])
        # self.txt = txt = ax.text(0.01, 0.99, "", ha="left",
        #                          va="top", transform=ax.transAxes)

        # print('Video is generating. Please wait...')
        # ani = FuncAnimation(fig, self.update, frames=range(len(self.array.full_copies)),
        #                     blit=True, interval=1000./fps, repeat=False)

        # ani.save(f'{dir}/videos/video.mp4')

    def generate(self):

        fig, ax = plt.subplots(figsize=(16, 8))
        self.container = ax.bar(np.arange(0, len(self.array), 1),
                                self.array.full_copies[0], align="edge", width=0.8)
        fig.suptitle(f"{self.sorter} sort")
        ax.set(xlabel="Index", ylabel="Value")
        ax.set_xlim([0, self.n])
        self.txt = ax.text(0.01, 0.99, "", ha="left",
                           va="top", transform=ax.transAxes)

        print('Video is generating. Please wait...')
        ani = FuncAnimation(fig, self.update, frames=range(len(self.array.full_copies)),
                            blit=True, interval=1000./self.fps, repeat=False)

        ani.save(f'{dir}/videos/video.mp4')

    def update(self, frame):
        self.txt.set_text(f"Accesses = {frame}")
        for rectangle, height in zip(self.container.patches, self.array.full_copies[frame]):
            rectangle.set_height(height)
            rectangle.set_color("#1f77b4")

        idx, op = self.array.GetActivity(frame)
        if op == "get":
            self.container.patches[idx].set_color("magenta")
        elif op == "set":
            self.container.patches[idx].set_color("red")
        return (self.txt, *self.container)
