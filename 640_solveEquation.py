import re
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        symbol_dict = {'+': 1, '-': -1}
        x_value = 0
        num_value = 0
        equation_symbol = 1
        factor_symbol = 1
        index = 0
        print(equation)
        while index < len(equation):
            if equation[index] in ("+",'-'):
                factor_symbol = symbol_dict[equation[index]]
                index += 1
                continue
            if equation[index] == '=':
                equation_symbol = -1
                factor_symbol = 1
                index += 1
                continue
            factor_string = ""
            for inner_index in range(index, len(equation)):
                if re.match("[0-9xX]", equation[inner_index]):
                    factor_string += equation[inner_index]
                    index = inner_index
                elif equation[inner_index] in ("+", '-', '='):
                    index = inner_index - 1
                    break
                else:
                    print("unexpected factor")
            if factor_string != "":
                print("this sub object= " + factor_string + " symbol= " + str(factor_symbol) + " equation symbol = " + str(equation_symbol))
                if factor_string[-1] in ('x', 'X'):
                    if len(factor_string) == 1:
                        x_value += factor_symbol * equation_symbol
                    else:
                        x_value += factor_symbol * equation_symbol * int(factor_string[:-1])
                else:
                    num_value += factor_symbol * equation_symbol * int(factor_string)
            index += 1
        print(x_value, num_value)
        if x_value == 0 and num_value !=0:
            return "No solution"
        elif x_value == 0 and num_value == 0:
            return "Infinite solutions"
        elif x_value != 0 and num_value == 0:
            return "x=0"
        else:
            return "x=" + str(int(-num_value/x_value))



test_input = "1-x+x-x+x+x=99"
print(Solution().solveEquation(test_input))


