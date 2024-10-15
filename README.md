# Video Converter with Audio Stream and Codec Selection

This is a Python-based video conversion tool that uses the `ffmpeg-python` package to allow users to convert video files, select the desired audio stream, and choose the audio codec for the output video. The GUI is built using Tkinter.

## Features

- __File Selection__: Users can select a video file from their local system.
- __Audio Stream Detection__: The tool automatically detects available audio streams in the selected video file.
- __Audio Codec Selection__: Users can select the desired audio codec for the output file.
- __Video Conversion__: The tool copies the video stream without re-encoding and converts the audio stream using the selected codec.

## Requirements

To run this project, you need the following installed on your system:

1. Python 3.6+
2. FFmpeg: Make sure FFmpeg is installed and accessible via your system's PATH.
3. Python Packages:
    - `ffmpeg-python`
    - `tkinter`

You can install the necessary Python packages by running:

```bash
pip install ffmpeg-python
```
## Installation of FFmpeg

1. __Windows__: You can download the FFmpeg binary from FFmpeg.org. Add the path to FFmpeg binaries to your system’s PATH.
2. __Linux__: Install `FFmpeg` using the package manager:

```bash
sudo apt install ffmpeg
```
3. __Mac__: Install via Homebrew:

```bash

brew install ffmpeg
```

## Usage
Running the Application

1. Clone the repository or download the script.
2. Run the Python script:

```bash
python video_converter.py
```

## GUI Walkthrough

1. __Select Video File__: Click the "Browse" button to choose a video file (supports `.mkv` and other video formats).
2. __Select Output Format__: Choose the output video format (`mp4`, `mkv`, etc.) from the dropdown menu.
3. __Select Audio Stream__: Based on the detected audio streams, you can select which audio stream to use (e.g., the first or second audio stream).
4. __Select Audio Codec__: Choose the audio codec for the output file (e.g., `aac`, `mp3`, etc.).
5. __Convert__: Click the "Convert" button to start the conversion. The converted video file will be saved in the same directory as the original file, with a timestamp appended to its name.

### Example

- Select a video file such as `input.mkv`.
- Choose `mp4` as the output format.
- Choose the desired audio stream and codec (e.g., `aac`).
- Click __Convert__.
- The output file will be saved as `input_converted_YYYYMMDD_HHMMSS.mp4`.

## Code Explanation

- __`get_audio_streams()`__: This function uses ffmpeg.probe() to retrieve information about available audio streams in the selected video file.
- __`convert_video()`__: Converts the selected video using ffmpeg-python. It copies the video stream and converts the audio stream based on the selected audio codec and stream index.
- __Tkinter GUI__: The Tkinter interface allows the user to interact with the program by selecting files, audio streams, and codecs, and then starting the conversion process.

## Dependencies

- __ffmpeg-python__: A Python binding for FFmpeg.
- __Tkinter__: Standard Python library for building GUIs (already included in Python installations).

## Troubleshooting

- Ensure __FFmpeg__ is installed and properly added to the system's PATH.
- If the output video has no audio, double-check that you have selected the correct audio stream and codec.
- Make sure you have the correct permissions to read the input file and write the output file.

## License

This project is licensed under the [MIT License](LICENSE).