from manim.animation.creation import Write
from manim.constants import DOWN, ORIGIN, RIGHT
from manim.mobject.text.tex_mobject import MathTex
from manim.mobject.text.text_mobject import Text
from manim.mobject.types.vectorized_mobject import VGroup
from manim.scene.scene import Scene

from .colors import Colors


class Intro(Scene):
    def construct(self):
        ds_o = MathTex(r"\mathbb{O}", fill_color=Colors.POWDER_BLUE.value).scale(4)
        ds_r = MathTex("R", fill_color=Colors.BURNT_PEACH.value).scale(3)
        ds_der = MathTex("der", fill_color=Colors.POWDER_BLUE.value).scale(2)
        ds_of = Text("of", fill_color=Colors.DUSK_BLUE.value).scale(1.6)
        ds_eason = MathTex("eason", fill_color=Colors.BURNT_PEACH.value).scale(2)

        ds_r.shift(1.1 * RIGHT + 0.6 * DOWN)
        ds_der.shift(2.4 * RIGHT + 0.3 * DOWN)
        ds_of.shift(3.7 * RIGHT + 0.3 * DOWN)
        ds_eason.shift(2.9 * RIGHT + 0.9 * DOWN)

        logo = VGroup(ds_eason, ds_der, ds_of, ds_r, ds_o)
        logo.move_to(ORIGIN)

        self.play(Write(ds_o), run_time=0.5)
        self.play(Write(ds_r), run_time=0.25)
        self.play(Write(ds_der), run_time=0.75)
        self.play(Write(ds_of), run_time=0.5)
        self.play(Write(ds_eason), run_time=1.25)

        self.wait(0.9)
