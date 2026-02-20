from manim import *
from scripts.utilities import Colors
import numpy as np

# (latex, angle_deg, distance, scale, color, opacity)
# Symbols are placed in polar coords from center so they radiate outward.
# Frame is ~14.2 wide x 8 tall, so distances near 90°/270° are capped ~3.
BG_SYMBOLS = [
    # --- outer ring ---
    (r"\lim_{x \to a} f(x) = L", 5, 5.2, 0.50, Colors.POWDER_BLUE, 0.55),
    (r"\forall \varepsilon > 0", 38, 4.6, 0.58, Colors.DUSK_BLUE, 0.52),
    (r"\exists\, \delta > 0", 68, 3.3, 0.58, Colors.POWDER_BLUE, 0.52),
    (r"\sup S \in \mathbb{R}", 95, 2.9, 0.58, Colors.STEEL_BLUE, 0.55),
    (r"\int_a^b f(x)\,dx", 120, 3.6, 0.60, Colors.SEAFOAM, 0.55),
    (r"\sum_{n=1}^{\infty} a_n", 150, 4.8, 0.58, Colors.WARM_SAND, 0.52),
    (r"\mathbb{R}", 178, 5.4, 0.95, Colors.DUSK_BLUE, 0.45),
    (r"|a_n - L| < \varepsilon", 205, 4.5, 0.50, Colors.POWDER_BLUE, 0.50),
    (r"\inf S \in \mathbb{R}", 232, 4.0, 0.55, Colors.STEEL_BLUE, 0.52),
    (r"\overline{A} \subset \mathbb{R}", 258, 3.0, 0.55, Colors.BURNT_PEACH, 0.48),
    (r"(a_n)_{n \in \mathbb{N}}", 278, 3.0, 0.58, Colors.WARM_SAND, 0.52),
    (
        r"f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}",
        305,
        4.0,
        0.42,
        Colors.STEEL_BLUE,
        0.50,
    ),
    (r"\mathcal{C}([a,b])", 338, 4.6, 0.60, Colors.WARM_SAND, 0.52),
    # --- inner ring (closer, simpler symbols) ---
    (r"\varepsilon", 22, 2.4, 0.90, Colors.BURNT_PEACH, 0.44),
    (r"\delta", 55, 2.2, 0.90, Colors.BURNT_PEACH, 0.42),
    (r"\infty", 108, 2.3, 0.95, Colors.SEAFOAM, 0.44),
    (r"\forall n \geq N", 190, 2.7, 0.60, Colors.DUSK_BLUE, 0.48),
    (r"\sup", 243, 2.3, 0.82, Colors.POWDER_BLUE, 0.42),
    (r"\left\| f \right\|_\infty", 290, 2.6, 0.65, Colors.POWDER_BLUE, 0.50),
    (r"n \to \infty", 322, 2.5, 0.65, Colors.DUSK_BLUE, 0.50),
]

NUM_RAYS = 18


class RealAnalysisThumbnail(Scene):
    def construct(self):
        # --- radial dashed rays emanating from center ---
        for i in range(NUM_RAYS):
            angle = i * TAU / NUM_RAYS
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            ray = DashedLine(
                start=direction * 1.1,
                end=direction * 8.0,
                dash_length=0.10,
                dashed_ratio=0.35,
                color=Colors.STEEL_BLUE.value,
                stroke_opacity=0.12,
                stroke_width=1.0,
            )
            self.add(ray)

        # --- soft glow rings behind title ---
        for radius, opacity in [(1.9, 0.05), (1.5, 0.09), (0.7, 0.13)]:
            self.add(
                Circle(radius=radius, color=Colors.BURNT_PEACH.value)
                .set_fill(Colors.BURNT_PEACH.value, opacity=opacity)
                .set_stroke(width=0)
            )

        # --- background symbols placed radially from center ---
        for latex, angle_deg, dist, scale, color, opacity in BG_SYMBOLS:
            a = np.radians(angle_deg)
            sym = (
                MathTex(latex, color=color.value)
                .scale(scale)
                .move_to([dist * np.cos(a), dist * np.sin(a), 0])
                .set_opacity(opacity)
            )
            self.add(sym)

        # --- foreground title (on top of everything) ---
        title = MathTex(r"\text{Real Analysis}", color=Colors.BURNT_PEACH.value).scale(
            2
        )
        self.add(title)
