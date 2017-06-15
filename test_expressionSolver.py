###
# Created by Curtis Szmania
# Date: 4/18/17
# Comment: PLEXSYS coding assessment
# Expression solver to solve a given expression string.
###

__author__='szmania'

# noinspection PyUnresolvedReferences,PyUnresolvedReferences
from expressionSolver import ExpressionSolver

def main():

    expObj = ExpressionSolver(logLevel='DEBUG')

    expr1 = '1 + 1'
    val1 = expObj.solve(expr1)

    expr2  = '(3 + 4) * 6'
    val2 = expObj.solve(expr2)

    expr3 = '(1 * 4) + (5 * 2)'
    val3 = expObj.solve(expr3)

    expr4 = '(2 * 4) * 2 + (9 * 0)'
    val4 = expObj.solve(expr4)

    expr5 = '(2 - 4)(9 * 0)'
    val5 = expObj.solve(expr5)

    expr6 = '4(9 / 4)'
    val6 = expObj.solve(expr6)

    expr7 = '4(19 / 2)^2'
    val7 = expObj.solve(expr7)

    expr8 = '4^3(9 / 1)'
    val8 = expObj.solve(expr8)

if __name__ == "__main__":
    main()
