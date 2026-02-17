from manim import *
from colors import Colors


class ManimCELogo(Scene):
    def construct(self):
        grid = (
            NumberPlane()
            .apply_function(
                lambda p: (
                    p
                    + np.array(
                        [
                            np.sin(p[1]),
                            np.sin(p[0]),
                            0,
                        ]
                    )
                )
            )
            .set_stroke(Colors.JET_BLACK.value)
        )
        # safe = Rectangle(
        #     width=1546 / 2560 * config.frame_width,
        #     height=423 / 1440 * config.frame_height,
        # )
        ds_o = MathTex(r"\mathbb{O}", fill_color=Colors.POWDER_BLUE.value).scale(4)
        ds_r = MathTex("R", fill_color=Colors.BURNT_PEACH.value).scale(3)
        ds_der = MathTex("der", fill_color=Colors.POWDER_BLUE.value).scale(2)
        ds_of = Text("of", fill_color=Colors.DUSK_BLUE.value).scale(1.6)
        ds_eason = MathTex("eason", fill_color=Colors.BURNT_PEACH.value).scale(2)
        ds_r.shift(1.1 * RIGHT + 0.6 * DOWN)
        ds_der.shift(2.4 * RIGHT + 0.3 * DOWN)
        ds_of.shift(3.7 * RIGHT + 0.3 * DOWN)
        ds_eason.shift(2.9 * RIGHT + 0.9 * DOWN)
        logo = VGroup(ds_eason, ds_der, ds_of, ds_r, ds_o)  # order matters
        logo.move_to(ORIGIN)
        self.add(grid, logo)

