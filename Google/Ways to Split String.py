class Solution:
    def numSplits(self, s: str) -> int:

            res = 0
            f_right, f_left = {}, {}
            for c in s:
                f_right[c] = 1 + f_right.get(c, 0)
                
            print(f_right)

            for c in s:
                f_left[c] = 1 + f_left.get(c, 0)

                f_right[c] -= 1
                if f_right[c] == 0: f_right.pop(c)

                if len(f_right) == len(f_left): res += 1

            return res