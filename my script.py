from manim import *
import numpy as np

# ---------------------------------------------------------
# REELS / SHORTS VERTICAL FORMAT (9:16)
# ---------------------------------------------------------
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#FFF4D6"  # warm cream background

# ===========================================================
# CHARACTER BUILDERS
# ===========================================================

def create_chintu():
    """
    CHINTU - 'The Schemer'
    Spiky hair, oversized half-tucked shirt, one sock missing.
    """
    skin = "#F4C2A1"

    head = Circle(radius=0.45, color=skin, fill_opacity=1, stroke_color="#C98A5C")

    # Spiky hair -
