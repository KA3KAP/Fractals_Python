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
    Cross_2 = {"axiom": "F+F+F+F",
               "rules": {"F": "F+F-F+F+F"},
               "iterations": 5,  # TOP: 6
               "angle": 90,
               "length": 6
               }
    ChainCross = {"axiom": "X",
                       "rules": {"X": "FF", "F": "+F+F--F+F"},
                       "iterations": 2,  # TOP: 15
                       "angle": 45,
                       "length": 5
                       }

    Wheel = {"axiom": "FF",
                  "rules": {"X": "+X", "F": "XXFXF--FXF"},
                  "iterations": 4,  # TOP: 15
                  "angle": 45,
                  "length": 10
                  }

    Bud = {"axiom": "FF",
           "rules": {"F": "+F+F--F+F+F+F--F+F", "X": "+F+F--F+F"},
           "iterations": 4,  # TOP: 4 - почка
           "angle": 45,
           "length": 8}

    Second_Unnamed_Fractal = {"axiom": "FF",
                              "rules": {"F": "+F+F--F+FX", "X": "--"},
                              "iterations": 4,  # TOP: 15
                              "angle": 45,
                              "length": 5
                              }





