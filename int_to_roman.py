def int_to_roman(num: int) -> str:

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


integer_value = 1994
result = int_to_roman(integer_value)
print(f"The Roman numeral for {integer_value} is {result}")


# def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         str_num = str(num)
#         roman = ''
#         for idx, digit in enumerate(str_num):
#             if digit == '4':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'IV'
#                 elif idx == len(str_num)-2:
#                     roman += 'XL'
#                 elif idx == len(str_num)-3:
#                     roman += 'CD'
#             elif digit == '9':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'IX'
#                 elif idx == len(str_num)-2:
#                     roman += 'XC'
#                 elif idx == len(str_num)-3:
#                     roman += 'CM'
#             elif digit == '1':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'I'
#                 elif idx == len(str_num)-2:
#                     roman += 'X'
#                 elif idx == len(str_num)-3:
#                     roman += 'C'
#                 elif idx == len(str_num)-4:
#                     roman += 'M'
#             elif digit == '2':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'II'
#                 elif idx == len(str_num)-2:
#                     roman += 'XX'
#                 elif idx == len(str_num)-3:
#                     roman += 'CC'
#                 elif idx == len(str_num)-4:
#                     roman += 'MM'
#             elif digit == '3':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'III'
#                 elif idx == len(str_num)-2:
#                     roman += 'XXX'
#                 elif idx == len(str_num)-3:
#                     roman += 'CCC'
#                 elif idx == len(str_num)-4:
#                     roman += 'MMM'
#             elif digit == '5':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'V'
#                 elif idx == len(str_num)-2:
#                     roman += 'L'
#                 elif idx == len(str_num)-3:
#                     roman += 'D'
#             elif digit == '6':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'VI'
#                 elif idx == len(str_num)-2:
#                     roman += 'LX'
#                 elif idx == len(str_num)-3:
#                     roman += 'DC'
#             elif digit == '7':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'VII'
#                 elif idx == len(str_num)-2:
#                     roman += 'LXX'
#                 elif idx == len(str_num)-3:
#                     roman += 'DCC'
#             elif digit == '8':
#                 if idx == len(str_num)-1: # единиц
#                     roman += 'VIII'
#                 elif idx == len(str_num)-2:
#                     roman += 'LXXX'
#                 elif idx == len(str_num)-3:
#                     roman += 'DCCC'

#         return roman