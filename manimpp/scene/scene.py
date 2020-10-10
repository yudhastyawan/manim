from manimlib.imports import *

class YScene(Scene):
    CONFIG = {
        "camera_class": Camera,
        "camera_config": {},
        "file_writer_config": {},
        "skip_animations": False,
        "always_update_mobjects": False,
        "random_seed": 0,
        "start_at_animation_number": None,
        "end_at_animation_number": None,
        "leave_progress_bars": False,
    }

    def setBackgroundColor(self,cm):
        self.camera_config = {
            "background_color": background_color,
        }

    def setBackgroundColor(self,cm):
        self.camera_config = {
            "background_color": cm,
        }
        self.camera = self.camera_class(**self.camera_config)