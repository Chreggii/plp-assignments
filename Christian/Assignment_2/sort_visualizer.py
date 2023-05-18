import os
from array_tracker import ArrayTracker
from quick_sort import QuickSort
from sound_generator import SoundGenerator
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from selection_sort import SelectionSort
from graphic import Graphic
import numpy as np
import subprocess


class SortVisualizer():

    def __init__(self, sort_alg_name, n, ms, mode='light'):
        self.sort_alg_name = sort_alg_name
        self.n = n
        self.fps = 1000./ms
        self.mode = mode

    def visualize(self):

        arr = np.round(np.linspace(0, 1000, self.n), 0)
        np.random.seed(0)
        np.random.shuffle(arr)
        arr = ArrayTracker(arr)
        np.random.seed(0)

        if self.sort_alg_name == 'QuickSort':
            QuickSort(arr, 0, len(arr)-1).sort()
        elif self.sort_alg_name == 'BubbleSort':
            BubbleSort(arr).sort()
        elif self.sort_alg_name == 'InsertionSort':
            InsertionSort(arr).sort()
        elif self.sort_alg_name == 'SelectionSort':
            SelectionSort(arr).sort()
        else:
            print(
                'Sort algorithm not supported. Please choose QuickSort, BubbleSort, InsertionSort or SelectionSort.')
            raise SystemExit

        SoundGenerator(arr, self.fps).generate()

        Graphic(arr, self.n, self.sort_alg_name,
                self.fps, self.mode).generate()

        try:
            os.remove(f'output.mp4')
        except:
            pass

        cmd_str = "ffmpeg -i videos/video.mp4 -i sound/sound.wav -map 0 -map 1:a -c:v copy -shortest output.mp4"
        subprocess.run(cmd_str, shell=True)

        print(
            f'Video generated. You can find it here: {os.getcwd()}/output.mp4')
