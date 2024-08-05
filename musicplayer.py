import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        
        pygame.mixer.init()
        
        self.current_song = None
        self.song_list = []
        self.paused = False
        
        self.label = tk.Label(root, text="No song playing", font=("Helvetica", 12))
        self.label.pack(pady=10)
        
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(side="left", padx=10)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(side="left", padx=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side="left", padx=10)
        
        self.load_button = tk.Button(root, text="Load Folder", command=self.load_folder)
        self.load_button.pack(side="left", padx=10)
    
    def load_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.song_list = [os.path.join(folder_selected, f) for f in os.listdir(folder_selected) if f.endswith(".mp3")]
            if self.song_list:
                self.current_song = self.song_list[0]
                self.label.config(text=f"Loaded {len(self.song_list)} songs.")
            else:
                messagebox.showinfo("Info", "No mp3 files found in the selected folder.")
    
    def play_music(self):
        if not self.paused:
            if self.current_song:
                pygame.mixer.music.load(self.current_song)
                pygame.mixer.music.play()
                self.label.config(text=f"Playing: {os.path.basename(self.current_song)}")
        else:
            pygame.mixer.music.unpause()
            self.paused = False
            self.label.config(text=f"Playing: {os.path.basename(self.current_song)}")
    
    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused = True
        self.label.config(text=f"Paused: {os.path.basename(self.current_song)}")
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.label.config(text="No song playing")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()