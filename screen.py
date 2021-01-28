import tkinter as tk
from tkinter import ttk
import cv2
import numpy as np
import pyautogui

resolution =(1366,768)
continueRecording=True

codec = cv2.VideoWriter_fourcc(*'XVID') 
filename="screenrecord.MP4"
fps = 30.0
output =cv2.VideoWriter(filename, codec, fps, resolution)

win = tk.Tk()
win.title("Screen Recorder")



def record_screen():
    win.iconify()
    recordOneFrame()

def recordOneFrame():
    global continueRecording
    img=pyautogui.screenshot()
    frame = np.array(img)

    frame =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)

    if continueRecording:
        win.after(round(1/80.*1000),recordOneFrame)
        
    

start_recordbtn= ttk.Button(win, text="Start Record", width=20 , command=record_screen)
start_recordbtn.pack(pady=(10,0))

def stop_record():
    global continueRecording
    continueRecording = False
    cv2.destroyAllWindows()
    output.release()

stop_recordbtn= ttk.Button(win, text="Stop Record",   width=20 , command=stop_record )
stop_recordbtn.pack(pady=(10,0))

win.mainloop()
cv2.destroyAllWindows()
output.release()
