import os
from array_tracker import ArrayTracker
from quick_sort import QuickSort
from sound_generator import SoundGenerator
from bubble_sort import BubbleSort
from insertion_sort import InserationSort
from graphic import Graphic
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

print(os.getcwd())

dir = "d:\Privat\git\plp-assignments\Christian\Assignment_2" if os.getcwd(
) == "d:\Privat\git\plp-assignments" else os.getcwd()


if __name__ == "__main__":
    sorterName = "Quick"

    N = 50
    FPS = 60

    arr = np.round(np.linspace(0, 1000, N), 0)
    np.random.seed(0)
    np.random.shuffle(arr)
    arr = ArrayTracker(arr)
    np.random.seed(0)

    # QuickSort(arr, 0, len(arr)-1).sort()
    BubbleSort(arr).sort()
    # InserationSort(arr).sort()

    SoundGenerator(arr, FPS).generate()

    Graphic(arr, N, sorterName, FPS).generate()

    try:
        os.remove(f'{dir}/output.mp4')
    except:
        pass

    cmd_str = f"ffmpeg -i {dir}/videos/video.mp4 -i {dir}/sound/sound.wav -map 0 -map 1:a -c:v copy -shortest {dir}/output.mp4"
    subprocess.run(cmd_str, shell=True)

    print(f'Video generated. You can find it here: {os.getcwd()}/output.mp4')
