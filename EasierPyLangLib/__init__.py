# v0.2.0
from . import formulas
from .formulas import BMI, average, clamp, factorial, fib, gcd, is_even

__version__ = "0.2.0"

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
]

# test run
if __name__ == "__main__":
    import EasierPyLangLib.example as example
