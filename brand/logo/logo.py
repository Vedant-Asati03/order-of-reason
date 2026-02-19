from manim import *
from colors import Colors


class ManimCELogo(Scene):
    def construct(self):
        ds_o = MathTex(r"\mathbb{O}", fill_color=Colors.POWDER_BLUE.value).scale(4)
        ds_r = MathTex("R", fill_color=Colors.BURNT_PEACH.value).scale(3)
        ds_r.shift(1.1 * RIGHT + 0.6 * DOWN)
        logo = VGroup(ds_o, ds_r)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)
