class Fractals:
    Vicek_Fractal = {"axiom": "F-F-F-F",
                     "rules": {"F": "F-F+F+F-F"},
                     "iterations": 4,  # TOP: 6
                     "angle": 90
                    }

    Krishna_Anklets = {"axiom": " -X--X",
                       "rules": {"X": "XFX--XFX"},
                       "iterations": 5,  # TOP: 9
                       "angle": 45
                       }
    Dragon_Curve = {"axiom": "FX",
                    "rules": {"X": "X+YF+", "Y": "-FX-Y"},
                    "iterations": 10, # TOP: 16
                    "angle": 90
                    }
    TerDragon_Curve = {"axiom": "F",
                       "rules": {"F": "F-F+F"},
                       "iterations": 6,  # TOP: 10
                       "angle": 120
                       }
    Double_Dragon_Curve = {"axiom": "FX+FX",
                           "rules": {"X": "X+YF+", "Y": "-FX-Y"},
                           "iterations": 13,  # TOP: 16
                           "angle": 90
                           }
    Triple_Dragon_Curve = {"axiom": "FX+FX+FX",
                           "rules": {"X": "X+YF+", "Y": "-FX-Y"},
                           "iterations": 10,  # TOP: 15
                           "angle": 90,
                           }
    Unnamed_Fractal = {"axiom": "FF",
                       "rules": {"F": "+F+F--F+F"},
                       "iterations": 6,  # TOP: 15
                       "angle": 45,
                       "length": 2
                       }
    Second_Unnamed_Fractal = {"axiom": "FF",
                              "rules": {"F": "+F+F--F+FX", "X": "--"},
                              "iterations": 4,  # TOP: 15
                              "angle": 45,
                              "length": 5
                              }





