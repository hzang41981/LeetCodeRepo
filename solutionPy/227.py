class Solution(object):
    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        curr = 0
        sign = 1
        prev = 1
        multi = True
        for c in s:
            if c.isdigit():
                curr = curr*10 + int(c)
                print(curr)
            elif c == "+":
                if multi:
                    res += prev*curr*sign
                else:
                    res += prev//curr*sign
                    multi = True
                prev = 1
                curr = 0
                sign = 1
            elif c == "-":
                if multi:
                    res += prev*curr*sign
                else:
                    res += prev//curr*sign
                    multi = True
                prev = 1
                curr = 0
                sign = -1
            elif c == "*":
                if multi:
                    prev *= curr
                else:
                    prev //= curr
                    multi = True
                curr = 0
            else:
                if multi:
                    prev *= curr
                else:
                    prev //= curr
                multi = False
                curr = 0
        if multi:
            res += prev * curr * sign
        else:
            res += prev // curr * sign

        return res

    def calculate(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        res = 0
        curr = 0
        prev = 0
        operator = "+"
        len_s = len(s)
        for i in range(len_s):
            if s[i].isdigit():
                curr = curr * 10 + int(s[i])
            if (not s[i].isdigit() and not s[i] == " ") or i == len_s - 1:
                if operator == "+" or operator == "-":
                    res += prev
                    prev = curr if operator == "+" else -curr
                if operator == "*":
                    prev *= curr
                if operator == "/":
                    # python 3 and 2
                    prev = int(prev / curr)
                    # if prev > 0:
                    #     prev //= curr
                    # else:
                    #     prev = - ((-prev)//curr)
                operator = s[i]
                curr = 0
        res += prev
        return res




if __name__ == '__main__':
    s = Solution()
    print(s.calculate("14-3/2"))