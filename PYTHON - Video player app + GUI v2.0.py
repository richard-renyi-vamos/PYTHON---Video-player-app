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
