#------------------------IMPORT------------------------
#Create graphical interfaces with Python
from tkinter import *
#Create toolbox to open, save and choose files and folders
from tkinter import filedialog
#Install pygame
import pygame


#------------------------WINDOW------------------------
#Open window
pygame.mixer.init()

#Create window
window = Tk()
"""
Tk = create window
"""

#Set the window title
window.title("Simple MP3 Player")

#Set the window size
window.geometry("350x200")


#------------------------BUTTON FUNCTIONS------------------------
#Button select song
def select_song():
		#Open file explorer to pick a file and save it in "path" variable
    path = filedialog.askopenfilename(
        title="Choose an MP3",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    """
    askopenfilename = open file explorer
    
    filedialog.askopenfilename = in the filedialog toolbox,
    use "." the askopenfilename tool
    
    [] = list
    () = Tuple, two items
    Example:
	    filetypes=[
		    ("MP3 Files", "*.mp3"),
		    ("MP4 Files", "*.mp4")
	    ]
    """
    
    #If path is NOT empty, I mean, if you choose a file
    if path:
		    #Load mp3 file
        pygame.mixer.music.load(path)
        """
        pygame.mixer.music.load = load file
        pygame.mixer.music.load(path) = load file from "path"
        """
        
        #Show only the file name, hide the full folder path
        song_label.config(text=path.split("/")[-1])
        """
        .config = modify text, colour, size, etc
        
        song_label.config(text=path.split("/")[-1]) = Split full path, 
        take only the last item (file name)
        Example:
        - If "path" is "C:/Musica/Cancion.mp3"
        - And write path.split("/")
        - Split in ["C:", "Musica", "Cancion.mp3"]
        - [-1] take the last item
        """

#Button play
def play():
    pygame.mixer.music.play()

#Button pause
def pause():
    pygame.mixer.music.pause()

#Button resume
def resume():
    pygame.mixer.music.unpause()

#Button stop
def stop():
    pygame.mixer.music.stop()


#------------------------UI------------------------
#.........Create song ingo label.........
#Create label
song_label = Label(window, text="No song selected", wraplength=300)
"""
Label = create text

Label(window) = text must go INSIDE the window 

wraplength = max text width
"""

#Show label
song_label.pack(pady=15)
"""
.pack = show 
pady = vertical space
"""

#Show label
song_label.pack(pady=15)
"""
.pack = show 
pady = vertical space
"""

#........................................................................

#.........Create container that holds all the buttons together.........
#Create container
btn_frame = Frame(window)
"""
Frame = Create a container, it shows nothing
Frame(window) = frame must go INSIDE the window 
"""

#Show container
btn_frame.pack(pady=5)
"""
.pack = show 
pady = vertical space
"""
#........................................................................

#Buttons
Button(btn_frame, text="Select", command=select_song).grid(row=0, column=0, padx=3)
Button(btn_frame, text="Play", command=play).grid(row=0, column=1, padx=3)
Button(btn_frame, text="Pause", command=pause).grid(row=0, column=2, padx=3)
Button(btn_frame, text="Resume", command=resume).grid(row=0, column=3, padx=3)
Button(btn_frame, text="Stop", command=stop).grid(row=0, column=4, padx=3)

#Open window
window.mainloop()
