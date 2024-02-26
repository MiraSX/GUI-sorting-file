# File Sorter

This Python script provides a simple graphical user interface (GUI) using Tkinter to sort files within a specified directory based on their file types into separate subdirectories.

## Features
- Sorts files into categorized directories such as images, video, documents, audio, archives, and others.
- Supports various file types including images (JPEG, PNG, JPG, SVG), video (AVI, MP4, MOV, MKV), documents (DOC, DOCX, TXT, PDF, XLSX, PPTX), audio (MP3, OGG, WAV, AMR), archives (ZIP, GZ, TAR), and others.
- Handles file name normalization to ensure compatibility across different file systems.
- Provides error handling for invalid directory paths.

## Usage
1. Run the script.
2. Select the directory you want to sort using the provided file dialog.
3. Click the "Select" button to initiate the sorting process.
4. Files will be moved to their respective categorized directories within the specified directory.
5. A success message dialog will be displayed upon completion of the sorting process.

## Requirements
- Python 3.x
- Tkinter library

## How to Run
```bash
python script.py
