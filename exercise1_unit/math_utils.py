import math
from numbers import Real
import numpy as np

def add(a: int, b: int) -> int:
    """Return a + b. Raise TypeError if inputs are not strictly int or float (not bool)."""
    if (not isinstance(a, (int, float)) or isinstance(a, bool) or
        not isinstance(b, (int, float)) or isinstance(b, bool)):
        raise TypeError("Both arguments must be numeric (int or float, not bool)")
    return a + b

def div(a: float, b: float) -> float:
    """Return a / b. Raise ValueError if b == 0."""
    if b == 0 or not math.isfinite(b):
        raise ValueError("division by zero")
    return a / b
    # TODO: to uncomment the below line and comment the above line and observe the effects
    # return float(np.float32(a) / np.float32(b))

def clamp(x: float, low: float, high: float) -> float:
    """Confine x to [low, high]. Reject NaN and infinities."""
    # reject NaN and infinities
    for val in (x, low, high):
        if math.isnan(val) or math.isinf(val):
            raise ValueError("Arguments must be finite real numbers")

    if low > high:
        raise ValueError("low must be <= high")

    return max(low, min(x, high))
