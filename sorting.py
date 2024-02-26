import os
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory


def sort_files(BASE_DIR):
    if not os.path.exists(BASE_DIR):
        return print("please enter a valid path")

    os.makedirs(BASE_DIR + "/images", exist_ok=True)
    os.makedirs(BASE_DIR + "/video", exist_ok=True)
    os.makedirs(BASE_DIR + "/documents", exist_ok=True)
    os.makedirs(BASE_DIR + "/audio", exist_ok=True)
    os.makedirs(BASE_DIR + "/archives", exist_ok=True)
    os.makedirs(BASE_DIR + "/other", exist_ok=True)

    for i in os.listdir(BASE_DIR):
        i = i.lower()
        if (
            i == "images"
            or i == "video"
            or i == "documents"
            or i == "audio"
            or i == "archives"
            or i == "other"
        ):
            continue
        if os.path.isdir(i):
            sort_files(BASE_DIR + "/" + i)
        else:
            file_type = i.split(".")[-1]
            if file_type in ["jpeg", "png", "jpg", "svg"]:
                os.replace(
                    BASE_DIR + "/" + i,
                    BASE_DIR + "/images/" + normalize_name(i),
                )
            elif file_type in ["avi", "mp4", "mov", "mkv"]:
                os.replace(
                    BASE_DIR + "/" + i,
                    BASE_DIR + "/video/" + normalize_name(i),
                )
            elif file_type in ["doc", "docx", "txt", "pdf", "xlsx", "pptx"]:
                os.replace(
                    BASE_DIR + "/" + i,
                    BASE_DIR + "/documents/" + normalize_name(i),
                )
            elif file_type in ["mp3", "ogg", "wav", "amr"]:
                os.replace(
                    BASE_DIR + "/" + i,
                    BASE_DIR + "/audio/" + normalize_name(i),
                )
            elif file_type in ["zip", "gz", "tar"]:
                os.replace(
                    BASE_DIR + "/" + i,
                    BASE_DIR + "/archives/" + normalize_name(i),
                )
            else:
                os.replace(
                    BASE_DIR + "/" + i,
                    BASE_DIR + "/other/" + normalize_name(i),
                )
    messagebox.showinfo("Success", "Files sorted successfully")


def normalize_name(name):
    name = name.lower()
    tanslated_dict = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "yo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }
    translated_name = []

    for char in name:
        if char.isalnum() and char != "." and char in tanslated_dict:
            translated_name.append(tanslated_dict[char])
        elif char.isnumeric:
            translated_name.append(char)
        else:
            translated_name.append("_")
    translated_name = "".join(translated_name)
    return translated_name


if __name__ == "__main__":
    window = tk.Tk()
    main = tk.Label(window, text="Enter the path to the directory").grid(
        row=0, column=0
    )
    sort_dir = tk.Button(
        window, text="Select", command=lambda: sort_files(askdirectory())
    ).grid(row=0, column=1)

    window.mainloop()
