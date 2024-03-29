import math
from decimal import Decimal


class ExpressionEvaluator:
    DEFAULT_SYMBOL_LIST = {
        'pi': Decimal(
            '3.'
            '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
            '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'
        ),
        'e': Decimal(
            '2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'),
        'phi': (1 + math.sqrt(5)) / 2,
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'Decimal': Decimal,
    }

    class EvaluationError(Exception):
        pass

    def __init__(self, symbol_list=None):
        self.symbol_dict = (symbol_list or ExpressionEvaluator.DEFAULT_SYMBOL_LIST).copy()

    def eval_expr(self, expr):
        try:
            return eval(expr, {}, self.symbol_dict)
        except SyntaxError:
            raise self.EvaluationError("Invalid Expression Syntax")
        except NameError:
            raise self.EvaluationError("Unrecognized Tokens in Expression")
