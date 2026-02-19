import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from utilities.colors import Colors


class LineTest(Scene):
    def construct(self):
        line1 = Line([0, 0, 0], [5, 0, 0]).set_color(Colors.DEEP_OCEAN.value)
        line2 = Line([0, 1, 0], [5, 0, 0]).set_color(Colors.BURNT_PEACH.value)
        line3 = Line([0, 2, 0], [5, 0, 0]).set_color(Colors.SEAFOAM.value)
        line4 = Line([0, 3, 0], [5, 0, 0]).set_color(Colors.WARM_SAND.value)
        line5 = Line([0, 4, 0], [5, 0, 0]).set_color(Colors.STEEL_BLUE.value)
        self.add(line1, line2, line3, line4, line5)
