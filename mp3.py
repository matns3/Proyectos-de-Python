from tkinter import *
from tkinter import filedialog
import pygame

# Initialize
pygame.mixer.init()
window = Tk()
window.title("Simple MP3 Player")
window.geometry("350x200")

# Functions
def select_song():
    path = filedialog.askopenfilename(
        title="Choose an MP3",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    if path:
        pygame.mixer.music.load(path)
        song_label.config(text=path.split("/")[-1])

def play():
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

# UI
song_label = Label(window, text="No song selected", wraplength=300)
song_label.pack(pady=15)

btn_frame = Frame(window)
btn_frame.pack(pady=5)

Button(btn_frame, text="Select", command=select_song).grid(row=0, column=0, padx=3)
Button(btn_frame, text="Play", command=play).grid(row=0, column=1, padx=3)
Button(btn_frame, text="Pause", command=pause).grid(row=0, column=2, padx=3)
Button(btn_frame, text="Resume", command=resume).grid(row=0, column=3, padx=3)
Button(btn_frame, text="Stop", command=stop).grid(row=0, column=4, padx=3)

window.mainloop()