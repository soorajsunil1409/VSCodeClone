import tkinter as tk
from tab import Tab, TabImage, TabType


tab_label_color = "#121212"
tab_heading_frame_color = "#222222"
tab_main_frame_color = "#222222"
tab_label_height = 50


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Code Editor")
        self.geometry("700x700")

        self.container = tk.Frame(self, bd=0, bg="#222222")
        self.container.place()

        self.nav_frame = SideNav(self, bg="red")
        self.nav_frame.place(x=0, y=0, width=200, relheight=1)
        self.nav_frame.initialize_tabs()
        self.nav_frame.update_tabs()


class SideNav(tk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.tabs_info: list[Tab] = [Tab(TabImage.none("File Tab"), "File Tab", TabType.FileTab), Tab(TabImage.none("File Tab"), "File Tab", TabType.FileTab), Tab(TabImage.none("File Tab"), "File Tab", TabType.FileTab)]
        self.tab_frames: list[list[tk.Frame, tk.Frame]] = []
        self.selected_tab_idx = 0


        self.tab_heading_frame = tk.Frame(self, bg=tab_heading_frame_color, bd=0, highlightthickness=1)
        self.tab_main_frame = tk.Frame(self, bg=tab_main_frame_color, bd=0, highlightthickness=1)

    
    def initialize_tabs(self) -> None:
        self.tab_heading_frame.place(relheight=1, width=50, x=0, y=0)
        self.tab_main_frame.place(relheight=1, relwidth=1, x=50, y=0)
        for tab_info in self.tabs_info:
            self.tab_label = tk.Label(self.tab_heading_frame, bg=tab_label_color, text=tab_info.tab_name)
            self.tab_frame = tk.Frame(self.tab_main_frame, bg=tab_label_color, bd=2)
            self.tab_frames.append([self.tab_label, self.tab_frame])

    def update_tabs(self) -> None:
        self.update()
        for i, (tab_label, tab_frame) in enumerate(self.tab_frames):
            tab_label.place(x=0, y=i*tab_label_height, height=tab_label_height, width=50)
            tab_frame.place(x=0, y=0, relwidth=1, relheight=1)
            
        self.tab_frames[self.selected_tab_idx][1].tkraise()

