# V0.1

import os
import ffmpeg
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# Function to get available audio streams (with index)
def get_audio_streams(input_filepath):
    probe = ffmpeg.probe(input_filepath)
    audio_streams = []
    index = 0
    for stream in probe['streams']:
        if stream['codec_type'] == 'audio':
            audio_codec = stream['codec_name']
            audio_streams.append((index, audio_codec))
            index += 1
    return audio_streams

# Function to convert video using ffmpeg-python
def convert_video(input_filepath, output_format, selected_audio_codec, audio_stream_index):
    filename = os.path.splitext(os.path.basename(input_filepath))[0]
    timestamp_ = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filepath = os.path.join(os.path.dirname(input_filepath), f"{filename}_converted_{timestamp_}.{output_format}")

    try:
        # Run ffmpeg-python conversion
        (
            ffmpeg
            .input(input_filepath)
            .output(output_filepath, map=f'0:a:{audio_stream_index}', vcodec='copy', acodec=selected_audio_codec)
            .run()
        )
        messagebox.showinfo("Success", f"Conversion complete!\nOutput file: {output_filepath}")
    except ffmpeg.Error as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

# Function to get the input file path and extract audio streams and encodings
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("MKV files", "*.mkv"), ("All files", "*.*")])
    if file_path:
        input_path_entry.delete(0, tk.END)
        input_path_entry.insert(0, file_path)
        # Populate audio streams dropdown
        available_audio_streams = get_audio_streams(file_path)
        audio_var.set('')
        audio_menu['menu'].delete(0, 'end')
        for idx, encoding in available_audio_streams:
            audio_menu['menu'].add_command(label=f"{idx}: {encoding}", command=tk._setit(audio_var, encoding))
        
        # Also populate stream index dropdown
        stream_var.set('')
        stream_menu['menu'].delete(0, 'end')
        for idx, _ in available_audio_streams:
            stream_menu['menu'].add_command(label=f"Stream {idx}", command=tk._setit(stream_var, idx))

# Function to start conversion process
def start_conversion():
    input_filepath = input_path_entry.get()
    output_format = format_var.get()
    selected_audio_codec = audio_var.get()
    audio_stream_index = stream_var.get()

    if not input_filepath:
        messagebox.showwarning("Input Required", "Please select a video file.")
        return
    
    if not output_format:
        messagebox.showwarning("Format Required", "Please select an output format.")
        return
    
    if not selected_audio_codec:
        messagebox.showwarning("Audio Codec Required", "Please select an audio codec.")
        return

    if audio_stream_index == '':
        messagebox.showwarning("Audio Stream Required", "Please select an audio stream.")
        return

    convert_video(input_filepath, output_format, selected_audio_codec, audio_stream_index)

# Create the Tkinter window
window = tk.Tk()
window.title("Video Converter")

# Create a label and entry for the file path
tk.Label(window, text="Select Video File:").grid(row=0, column=0, padx=10, pady=10)
input_path_entry = tk.Entry(window, width=50)
input_path_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button to browse for a file
browse_button = tk.Button(window, text="Browse", command=select_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# Create a label and dropdown menu for output format
tk.Label(window, text="Select Output Format:").grid(row=1, column=0, padx=10, pady=10)
format_var = tk.StringVar(window)
format_menu = tk.OptionMenu(window, format_var, "mp4", "mkv")
format_menu.grid(row=1, column=1, padx=10, pady=10)

# Create a label and dropdown menu for audio encoding
tk.Label(window, text="Select Audio Encoding:").grid(row=2, column=0, padx=10, pady=10)
audio_var = tk.StringVar(window)
audio_menu = tk.OptionMenu(window, audio_var, '')
audio_menu.grid(row=2, column=1, padx=10, pady=10)

# Create a label and dropdown menu for audio stream selection
tk.Label(window, text="Select Audio Stream:").grid(row=3, column=0, padx=10, pady=10)
stream_var = tk.StringVar(window)
stream_menu = tk.OptionMenu(window, stream_var, '')
stream_menu.grid(row=3, column=1, padx=10, pady=10)

# Create a convert button
convert_button = tk.Button(window, text="Convert", command=start_conversion)
convert_button.grid(row=4, column=1, padx=10, pady=20)

# Start the Tkinter event loop
window.mainloop()
