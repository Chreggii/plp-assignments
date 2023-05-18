# PLP Assignment 2

## Sreenshot & Videos

The screenshots which are showing that the code is running can be found in the `screenshots` folder.

Since the zip file would be too big, I published the videos on Youtube:

- Quick Sort | 101 entities | 16ms delay | dark mode -> https://youtu.be/V4L8IHl9YDI
- Selection Sort | 120 entities | 16ms delay | dark mode -> https://youtu.be/MpZmIiAObYA
- Bubble Sort | 101 entities | 16ms delay | dark mode -> https://youtu.be/O5-p_tGZZ6o
- Insertion Sort | 101 entities | 16ms delay | light mode -> https://youtu.be/hYAlzI3S9uU

- Insertion Sort | 110 entities | 50ms delay | dark mode -> https://youtu.be/DJkRuKLFfHw
- Quick Sort | 120 entities | 100ms delay | dark mode -> https://youtu.be/1BkXzuCOaGE

## Run Appliation

### Preconditions

- Install the required dependencies with `pip install -r requirements/requirements.txt`
- Make sure `ffmpeg` is installed ([Download Link](https://ffmpeg.org/download.html)).

### Running Application

Run the application with the following command `python main.py` or `python3 main.py`.\
The generated video will be saved in the `output.mp4` file.

### SortVisualizer Arguments

The `SortVisualizer` constructor requires the following parameter:

|     Name   | Description                                    | Type                                                              |  Required |
|------------|------------------------------------------------|-------------------------------------------------------------------|-----------|
| sorterName | The name of the desired sort algorithmus.      | "QuickSort" \| "BubbleSort" \| "InsertionSort" \| "SelectionSort" | Yes       |
| n          | n, the highest number in the dataset.          | Number                                                            | Yes       |
| ms         | The delay in ms.                               | Number                                                            | Yes       |
| mode       | The mode in which the graphic should be shown. | "light" \| "dark"                                                 | No        |
