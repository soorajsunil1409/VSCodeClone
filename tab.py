import tkinter as tk
from dataclasses import dataclass
from enum import Enum

@dataclass
class TabImage:
    image_path: str = None
    tab_name: str = ""

    def none(tab_name: str = ""):
        return TabImage(None, "")


class TabType(Enum):
    FileTab = 1


class Tab():
    def __init__(self, tab_image: TabImage, tab_name: str, tab_type: TabType) -> None:
        super().__init__()

        self.tab_image: TabImage = tab_image
        self.tab_type: TabType = tab_type
        self.tab_name: str = tab_name