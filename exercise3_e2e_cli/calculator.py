"""
Tiny calculator CLI.

Usage:
  echo "add 5 10"    | python calc.py
  echo "div 6 3"     | python calc.py
  echo "clamp 11 0 10" | python calc.py
Prints the numeric result or 'ERROR' on invalid input.
"""
import sys
from math import isfinite

def main():
    data = sys.stdin.read().strip().split()
    if not data or len(data) < 3:
        print("ERROR"); return
    op = data[0]
    try:
        nums = list(map(float, data[1:]))
    except ValueError:
        print("ERROR"); return

    try:
        if op == "add" and len(nums) == 2:
            res = nums[0] + nums[1]
        elif op == "div" and len(nums) == 2:
            if nums[1] == 0: raise ValueError("div0")
            res = nums[0] / nums[1]
        elif op == "clamp" and len(nums) == 3:
            x, lo, hi = nums
            if lo > hi: raise ValueError("range")
            res = max(lo, min(x, hi))
        else:
            print("ERROR"); return
        if not isfinite(res): print("ERROR"); return
        # print without trailing .0 if integer-like
        print(int(res) if res.is_integer() else res)
    except ValueError:
        print("ERROR")

if __name__ == "__main__":
    main()
