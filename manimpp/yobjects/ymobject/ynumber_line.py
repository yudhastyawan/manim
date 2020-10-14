import operator as op

from manimpp.constants import *
from manimpp.mobject.geometry import Line
from manimpp.mobject.numbers import DecimalNumber
from manimpp.mobject.types.vectorized_mobject import VGroup
from manimpp.utils.bezier import interpolate
from manimpp.utils.config_ops import digest_config
from manimpp.utils.config_ops import merge_dicts_recursively
from manimpp.utils.simple_functions import fdiv
from manimpp.utils.space_ops import normalize
from manimpp.mobject.number_line import NumberLine

class YNumberLine(NumberLine):
    CONFIG = {
        "color": LIGHT_GREY,
        "x_min": -FRAME_X_RADIUS,
        "x_max": FRAME_X_RADIUS,
        "unit_size": 1,
        "include_ticks": True,
        "tick_size": 0.1,
        "tick_frequency": 1,
        # Defaults to value near x_min s.t. 0 is a tick
        # TODO, rename this
        "leftmost_tick": None,
        # Change name
        "numbers_with_elongated_ticks": [0],
        "include_numbers": False,
        "numbers_to_show": None,
        "longer_tick_multiple": 2,
        "number_at_center": 0,
        "number_scale_val": 0.75,
        "label_direction": DOWN,
        "line_to_number_buff": MED_SMALL_BUFF,
        "include_tip": False,
        "tip_width": 0.25,
        "tip_height": 0.25,
        "decimal_number_config": {
            "num_decimal_places": 0,
        },
        "exclude_zero_from_default_numbers": False,
    }
    def __init__(self,
                 color = LIGHT_GREY,
                 x_min = -FRAME_X_RADIUS,
                 x_max = FRAME_X_RADIUS,
                 unit_size = 1,
                 include_ticks = True,
                 tick_size = 0.1,
                 tick_frequency = 1,
                 leftmost_tick = None,
                 numbers_with_elongated_ticks = None,
                 include_numbers = False,
                 numbers_to_show = None,
                 longer_tick_multiple = 2,
                 number_at_center = 0,
                 number_scale_val = 0.75,
                 label_direction = DOWN,
                 line_to_number_buff = MED_SMALL_BUFF,
                 include_tip = False,
                 tip_width = 0.25,
                 tip_height = 0.25,
                 num_decimal_places = 0,
                 exclude_zero_from_default_numbers = False,
                 ):
        self.color = color
        self.x_min = x_min
        self.x_max = x_max
        self.unit_size = unit_size
        self.include_ticks = include_ticks
        self.tick_size = tick_size
        self.tick_frequency = tick_frequency
        # Defaults to value near x_min s.t. 0 is a tick
        # TODO rename this
        self.leftmost_tick = leftmost_tick
        # Change name
        if numbers_with_elongated_ticks == None:
            self.numbers_with_elongated_ticks = [0]
        else:
            self.numbers_with_elongated_ticks = numbers_with_elongated_ticks
        self.include_numbers = include_numbers
        self.numbers_to_show = numbers_to_show
        self.longer_tick_multiple = longer_tick_multiple
        self.number_at_center = number_at_center
        self.number_scale_val = number_scale_val
        self.label_direction = label_direction
        self.line_to_number_buff = line_to_number_buff
        self.include_tip = include_tip
        self.tip_width = tip_width
        self.tip_height = tip_height
        self.decimal_number_config = {
            "num_decimal_places": num_decimal_places,
        }
        self.exclude_zero_from_default_numbers = exclude_zero_from_default_numbers
        NumberLine.__init__(self)

    def get_coordinate_labels(self, x_vals=None, scale_val=None, **kwargs):
        if x_vals is None:
            x_vals = []
        x_mobs = self.get_number_mobjects(*x_vals, scale_val=scale_val, **kwargs)

        self.coordinate_labels = x_mobs
        return self.coordinate_labels