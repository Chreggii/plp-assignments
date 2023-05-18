from sort_visualizer import SortVisualizer
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == "__main__":
    sorterName = "QuickSort"
    n = 100
    ms = 50
    mode = 'dark'

    visualizer = SortVisualizer(sorterName, n, ms, mode).visualize()
