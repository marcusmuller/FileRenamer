import os
import time
import PySimpleGUI as sg

def rename_files(folder_path, include_subfolders, input_format, output_format):
    count = 0

    start_time = time.time()

    for root, dirs, files in os.walk(folder_path):
        if not include_subfolders and root != folder_path:
            break
        for file in files:
            if file.lower().endswith(input_format):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file[:file.rfind(".")] + output_format)
                os.rename(old_file_path, new_file_path)
                count += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    return count, elapsed_time

# GUI Layout
layout = [
    [sg.Text("File Renamer", font=("Helvetica", 20), justification="center")],
    [sg.Text("Folder Path"), sg.Input(key="-FOLDER_PATH-"), sg.FolderBrowse()],
    [sg.Checkbox("Include Subfolders", default=False, key="-INCLUDE_SUBFOLDERS-")],
    [
        sg.Column([
            [sg.Text("Input", justification="center")],
            [sg.Radio(".ts", "INPUT_FORMAT", default=True, key="-TS-")],
            [sg.Radio(".mpeg", "INPUT_FORMAT", key="-MPEG-")],
            [sg.Radio(".mpg", "INPUT_FORMAT", key="-MPG-")]
        ], justification="center"),
        sg.Column([
            [sg.Text("Output", justification="center")],
            [sg.Radio(".mp4", "OUTPUT_FORMAT", default=True, key="-MP4-")],
            [sg.Radio(".m4v", "OUTPUT_FORMAT", key="-M4V-")],
            [sg.Radio(".mkv", "OUTPUT_FORMAT", key="-MKV-")]
        ], justification="center")
    ],
    [sg.Button("Rename Files"), sg.Button("Exit")],
    [sg.Text("Script by marcusmuller", font=("Helvetica", 8), justification="right")]
]

# Create the window
window = sg.Window("File Renamer", layout, finalize=True)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Rename Files":
        folder_path = values["-FOLDER_PATH-"]
        include_subfolders = values["-INCLUDE_SUBFOLDERS-"]
        input_format = ""
        output_format = ""

        if values["-TS-"]:
            input_format = ".ts"
        elif values["-MPEG-"]:
            input_format = ".mpeg"
        elif values["-MPG-"]:
            input_format = ".mpg"

        if values["-MP4-"]:
            output_format = ".mp4"
        elif values["-M4V-"]:
            output_format = ".m4v"
        elif values["-MKV-"]:
            output_format = ".mkv"

        if not folder_path:
            sg.popup("Select a folder.")
        elif not input_format:
            sg.popup("Select an input format.")
        elif not output_format:
            sg.popup("Select an output format.")
        else:
            matching_files = [file for root, dirs, files in os.walk(folder_path) for file in files if file.lower().endswith(input_format)]
            if not matching_files:
                sg.popup(f"No files found with the input format '{input_format}' in the selected folder. Please choose another folder.")
            else:
                count, elapsed_time = rename_files(folder_path, include_subfolders, input_format, output_format)
                success_message = f"File renaming completed!\nTotal files renamed: {count}\nElapsed time: {elapsed_time:.2f} seconds"
                sg.popup(success_message, title="Completed")

# Close the window
window.close()
