from sort_visualizer import SortVisualizer

if __name__ == "__main__":
    sorterName = "QuickSort"
    n = 100
    ms = 16
    mode = 'dark'

    visualizer = SortVisualizer(sorterName, n, ms, mode).visualize()
