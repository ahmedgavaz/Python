class py_solution:
    def __int__(self, s):
        self.s = s
    def int_to_Roman(self):
        lookup = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        res = ''
        for (n, roman) in lookup:
            (d, self.s) = divmod(self.s, n)
            res += roman * d
        return res

    def roman_to_int(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[self.s[i]] > rom_val[self.s[i - 1]]:
                int_val += rom_val[self.s[i]] - 2 * rom_val[self.s[i - 1]]
            else:
                int_val += rom_val[self.s[i]]
        return int_val

t=input("Number or Roman: ")
if t=="number":
    a=int(input("Number="))
    x=py_solution()
    x.int_to_Roman()
else:
    b=input("Roman=")
    x=py_solution()
    x.int_to_Roman()
