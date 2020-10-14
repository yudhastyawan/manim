import numpy as np
import numbers

from manimpp.constants import *
from manimpp.mobject.functions import ParametricFunction
from manimpp.mobject.geometry import Arrow
from manimpp.mobject.geometry import Line
from manimpp.mobject.number_line import NumberLine
from manimpp.mobject.svg.tex_mobject import TexMobject
from manimpp.mobject.types.vectorized_mobject import VGroup
from manimpp.utils.config_ops import digest_config
from manimpp.utils.config_ops import merge_dicts_recursively
from manimpp.utils.simple_functions import binary_search
from manimpp.utils.space_ops import angle_of_vector
from manimpp.mobject.coordinate_systems import *
from manimpp.yobjects.ycolormap import cm

class YAxes(Axes):
    CONFIG = {
        "axis_config": {
            "color": LIGHT_GREY,
            "include_tip": True,
            "exclude_zero_from_default_numbers": True,
        },
        "x_axis_config": {},
        "y_axis_config": {
            "label_direction": LEFT,
        },
        "center_point": ORIGIN,
        "dimension": 2,
        "x_min": -FRAME_X_RADIUS,
        "x_max": FRAME_X_RADIUS,
        "y_min": -FRAME_Y_RADIUS,
        "y_max": FRAME_Y_RADIUS,
    }

    def __init__(self,xmin=-FRAME_X_RADIUS,
                 xmax=FRAME_X_RADIUS,
                 ymin=-FRAME_Y_RADIUS,
                 ymax=FRAME_Y_RADIUS,
                 x_tick_frequency = 1,
                 x_labeled_nums = [0],
                 x_label_decimal = 1,
                 x_axis_width = None,
                 y_tick_frequency=1,
                 y_labeled_nums=[0],
                 y_label_decimal=1,
                 y_axis_width = None,
                 include_tip = False,
                 axes_color=LIGHT_GREY):
        self.x_min = xmin
        self.x_max = xmax
        self.y_min = ymin
        self.y_max = ymax
        if x_axis_width == None:
            self.x_axis_width = xmax - xmin
        if y_axis_width == None:
            self.y_axis_width = ymax - ymin
        self.axis_config = {
            "color": axes_color,
            "include_tip": include_tip,
            "exclude_zero_from_default_numbers": True,
        }
        self.x_num_range = float(self.x_max - self.x_min)
        self.space_unit_to_x = self.x_axis_width / self.x_num_range
        self.x_axis_config = {
            "numbers_with_elongated_ticks": x_labeled_nums,
            "tick_frequency": x_tick_frequency,
            "decimal_number_config": {
                "num_decimal_places": x_label_decimal,
            },
            "unit_size" : self.space_unit_to_x,
        }
        self.y_num_range = float(self.y_max - self.y_min)
        self.space_unit_to_y = self.y_axis_width / self.y_num_range
        self.y_axis_config = {
            "numbers_with_elongated_ticks": y_labeled_nums,
            "tick_frequency": y_tick_frequency,
            "decimal_number_config": {
                "num_decimal_places": y_label_decimal,
            },
            "unit_size": self.space_unit_to_y,
        }
        Axes.__init__(self)

    def get_grid(self,n = 1):
        group = VGroup()
        point = self.coords_to_point(self.x_min,self.y_min)
        dx = self.space_unit_to_x/n
        for i in np.arange(point[0], point[0]+self.x_axis_width + dx, dx):
            if np.mod(np.round(self.point_to_coords([i,0,0])[0],3), 1) == 0:
                group.add(Line((i * RIGHT)+(point[1] * UP), ((i * RIGHT)+(point[1] + self.y_axis_width) * UP))
                          .set_stroke(cm.DARK_GRAY, width=1))
            else:
                group.add(Line((i * RIGHT) + (point[1] * UP), ((i * RIGHT) + (point[1] + self.y_axis_width) * UP))
                          .set_stroke(cm.DARK_GRAY, width=0.5))
        dy = self.space_unit_to_y/n
        for i in np.arange(point[1], point[1]+self.y_axis_width + dy, dy):
            if np.mod(np.round(self.point_to_coords([i, 0, 0])[0], 3), 1) == 0:
                group.add(Line((i * UP) + (point[0] * RIGHT), ((i * UP) + (point[0] + self.x_axis_width) * RIGHT))
                          .set_stroke(cm.DARK_GRAY, width=1))
            else:
                group.add(Line((i * UP) + (point[0] * RIGHT), ((i * UP) + (point[0] + self.x_axis_width) * RIGHT))
                          .set_stroke(cm.DARK_GRAY, width=0.5))
        self.grid = group
        return self.grid