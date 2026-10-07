# v0.1.2.0
from . import formulas
from .formulas import BMI, average, clamp, factorial, fib, gcd, is_even

from . import maths
from .maths import pi, e

__version__ = "0.1.2.0"

__all__ = [
    "formulas",
    "BMI",
    "fib",
    "factorial",
    "average",
    "is_even",
    "gcd",
    "clamp",
    "__version__",
    "pi",
    "e"
]

# test run
if __name__ == "__main__":
    import EasierPyLangLib.example as example
