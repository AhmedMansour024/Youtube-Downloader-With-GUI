import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
import yt_dlp as yt



def choose_download_location():
    global download_path
    download_path = filedialog.askdirectory()
    if download_path:
        return download_path
    return None

def download_video():
    url = url_string.get()
    quality = quality_int.get()
    
    if quality < 144:
        quality = 720
    
    if not download_path:
        # Download options
        ydl_opts = {
            'format': f'best[height<={quality}]',
            'outtmpl': '%(title)s.%(ext)s',
            'ignoreerrors': True
        }

    else:
        # Download options
        ydl_opts = {
            'format': f'best[height<={quality}]',                   # quality option
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',        # Save file with same video title
            'ignoreerrors': True,                                   # skip unavailable videos and Ignore errors
        }

    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Download complete!")
    print(f"Downloaded With Quality {quality}")
    return None



# window
window = ttk.Window(themename="minty")

# title
window.title("Youtube Downloder")

# window size
window.geometry("800x400")

padframe = ttk.Frame(master=window)
padlabel = ttk.Label(master=padframe, text="Youtube Downloader", font="Calibri 24 bold")

# frame label
frame_label = ttk.Frame(master=window)
# URL label
url_label = ttk.Label(master=frame_label, text="Enter Youtube URL")
# quality label
quality_label = ttk.Label(master=frame_label, text="Enter Quality")

# frame entry
frame = ttk.Frame(master=window)
# URL entry
url_string = tk.StringVar()
url = ttk.Entry(master=frame, width=50, textvariable=url_string)
# quality entry
quality_int = tk.IntVar()
quality = ttk.Entry(master=frame, textvariable=quality_int)
#download location button
file_button = ttk.Button(master=frame, text="Download Location", command=choose_download_location)

# button 
button = ttk.Button(master=window, text="Download", command=download_video)

padlabel.pack()
padframe.pack(pady=40)

# pack frame_label
url_label.pack(side='left', padx=10)
quality_label.pack(side='left', padx=210)
frame_label.pack()

# pack frame
url.pack(side='left', padx=10)
quality.pack(side='left')
file_button.pack(side='left', padx=10)
frame.pack(pady=5)

# pack button
button.pack(pady=20)


# window runner
window.mainloop()

