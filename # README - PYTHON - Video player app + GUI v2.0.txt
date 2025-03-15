create a VIDEO PLAYER app in PYTHON

Creating a simple video player app in Python can be done using the tkinter library for the GUI and tkinter.ttk for styling, along with the opencv (cv2) and imageio libraries for video playback. Here's how you can create one:


---

Steps to Build a Video Player App

1. Install Dependencies
Make sure you have the required libraries installed:

pip install opencv-python numpy imageio[ffmpeg] pillow


2. Create the Video Player App

import cv2
import imageio
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Video Player")

        # Video Label
        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        # Buttons
        self.btn_open = tk.Button(root, text="Open Video", command=self.open_file)
        self.btn_open.pack()

        self.btn_play = tk.Button(root, text="Play", command=self.play_video)
        self.btn_play.pack()

        self.btn_stop = tk.Button(root, text="Stop", command=self.stop_video)
        self.btn_stop.pack()

        self.video_path = None
        self.playing = False

    def open_file(self):
        """Open a video file"""
        self.video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if self.video_path:
            print(f"Loaded: {self.video_path}")

    def play_video(self):
        """Play the selected video"""
        if not self.video_path:
            print("No video selected!")
            return

        self.playing = True
        self.cap = imageio.get_reader(self.video_path)

        def stream():
            for frame in self.cap:
                if not self.playing:
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)

                self.video_label.config(image=imgtk)
                self.video_label.image = imgtk
                self.root.update()

        self.root.after(1, stream)

    def stop_video(self):
        """Stop the video"""
        self.playing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()




---

Features of This Video Player:

✔ Open and play .mp4, .avi, .mov files
✔ Basic GUI with Play and Stop buttons
✔ Uses imageio for frame-by-frame video processing
✔ Converts OpenCV frames to Tkinter-compatible images

Would you like to enhance it with features like pause, volume control, or fullscreen mode?

-----

add a GUI to it

To enhance the video player app with a better GUI, we can use Tkinter with ttk styling and improve functionality by adding:

✅ Play, Pause, Stop buttons
✅ Progress bar (seek bar)
✅ Volume control
✅ Open file dialog


---

1️⃣ Install Required Libraries

Before running the script, install the necessary dependencies:

pip install opencv-python numpy imageio[ffmpeg] pillow tk


---

2️⃣ Full GUI Video Player App in Python

import cv2
import imageio
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import threading
import time

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Video Player")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Video Display
        self.video_label = tk.Label(self.root, bg="black")
        self.video_label.pack(pady=10)

        # Progress Bar
        self.progress = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", command=self.seek_video)
        self.progress.pack(fill="x", padx=20, pady=10)

        # Control Buttons
        control_frame = tk.Frame(self.root, bg="black")
        control_frame.pack(pady=10)

        self.btn_open = ttk.Button(control_frame, text="Open", command=self.open_file)
        self.btn_open.grid(row=0, column=0, padx=5)

        self.btn_play = ttk.Button(control_frame, text="Play", command=self.play_video)
        self.btn_play.grid(row=0, column=1, padx=5)

        self.btn_pause = ttk.Button(control_frame, text="Pause", command=self.pause_video)
        self.btn_pause.grid(row=0, column=2, padx=5)

        self.btn_stop = ttk.Button(control_frame, text="Stop", command=self.stop_video)
        self.btn_stop.grid(row=0, column=3, padx=5)

        # Volume Control
        self.volume_scale = ttk.Scale(self.root, from_=0, to=1, orient="horizontal", command=self.set_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(fill="x", padx=20, pady=10)

        self.video_path = None
        self.playing = False
        self.paused = False
        self.frame_count = 0
        self.current_frame = 0

    def open_file(self):
        """Open a video file"""
        self.video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if self.video_path:
            self.cap = imageio.get_reader(self.video_path)
            self.frame_count = self.cap.get_length()
            print(f"Loaded: {self.video_path}")

    def play_video(self):
        """Play the selected video"""
        if not self.video_path:
            print("No video selected!")
            return

        self.playing = True
        self.paused = False

        def stream():
            for i, frame in enumerate(self.cap):
                if not self.playing:
                    break
                if self.paused:
                    while self.paused:
                        time.sleep(0.1)
                    continue
                
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)

                self.video_label.config(image=imgtk)
                self.video_label.image = imgtk
                self.progress.set((i / self.frame_count) * 100)

                self.root.update()

        threading.Thread(target=stream, daemon=True).start()

    def pause_video(self):
        """Pause the video"""
        self.paused = not self.paused

    def stop_video(self):
        """Stop the video"""
        self.playing = False
        self.video_label.config(image="")

    def seek_video(self, value):
        """Seek video to a specific position"""
        pass  # Implement seeking logic

    def set_volume(self, value):
        """Adjust volume"""
        pass  # Implement volume control if using a video library that supports it

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()


---

🔹 Features of This Enhanced Video Player

✅ Tkinter GUI with buttons & controls
✅ Play, Pause, Stop functionality
✅ Progress bar for video seeking (future update)
✅ Volume control slider (to be integrated with audio libraries)
✅ Threaded playback to prevent UI freezing

Would you like me to add fullscreen mode, subtitle support, or a different video library like ffpyplayer for audio?

