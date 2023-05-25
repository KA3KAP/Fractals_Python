from turtle_graphic.Drawer import draw_fractal
from turtle_graphic.arguments import Fractals


def turtle_graphic():
    fractal = Fractals.Unnamed_Fractal
    draw_fractal(fractal['axiom'], fractal['rules'], fractal['iterations'], fractal['angle'], fractal['length'])   # iterations, axiom, rules, angle
