###
# Created by Curtis Szmania
# Date: 4/18/17
# Comment: PLEXSYS coding assessment
# Expression solver to solve a given expression string.
###

__author__='szmania'

from argparse import ArgumentParser
from logging import DEBUG, FileHandler, Formatter, getLogger, StreamHandler
# noinspection PyUnresolvedReferences
from operator import add, div, mul, pow, sub
from re import findall, search, sub as reSub
from sys import stdout

class ExpressionSolver(object):
    def __init__(self, logFile='expressionSolver.log', logLevel='DEBUG'):
        self.__logFile = logFile
        self.__logLevel = logLevel
        self.logger = getLogger('Expressions.__init__')
        self._setup_logger(logFile=self.__logFile)

    @property
    def logLevel(self):
        return self.__logLevel

    @logLevel.setter
    def logLevel(self, level):
        self.__logLevel = level
        
    @property
    def logFile(self):
        return self.__logFile

    @logFile.setter
    def logFile(self, value):
        self.__logFile = value

    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expr):
        self.__expression = expr

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    def _setup_logger(self, logFile):
        """
        Logger setup.

        :param logFile:  Log file path.
        :type logFile: String.

        :return:
        """

        root = getLogger()
        root.setLevel(DEBUG)

        self.handler = FileHandler(logFile)
        formatter = Formatter('%(levelname)s:%(name)s:%(message)s')

        # formatter = Formatter(fmt='%(message)s', datefmt='')
        self.handler.setFormatter(formatter)

        ch = StreamHandler(stdout)
        ch.setLevel(DEBUG)
        ch.setFormatter(formatter)

        root.addHandler(self.handler)
        root.addHandler(ch)

    def solve(self, expr):
        """
        Evaluates expression self.__expression and returns value.

        :param expr: ExpressionSolver to solve. ie: "(1 + 2) / 3"
        :param expr: String.

        :return: What the expression equals as a string.
        """

        logger = getLogger('Expressions.solve')
        logger.setLevel(self.logLevel)

        logger.debug(' Running equation solver.')

        self.__expression = expr

        self.__result = self._solve_equation(expr)

        self._display_result(expr=self.__expression, result=self.__result)

        return self.__result

    def _solve_equation(self, expr):
        """
        Evaluates expression expression and returns value.
        
        :param expr: expression to solve.
        :type expr: String.
        
        :return: Return result as string.
        """

        logger = getLogger('ExpressionSolver._solve_equation')
        logger.setLevel(self.__logLevel)

        logger.debug(' Solve equation: "%s"' % expr)

        expr_stripped = reSub(' ', '', expr)

        while '(' in expr_stripped:
            expr_stripped = self._solve_parentheses(expr_stripped)

        while '^' in expr_stripped:
            expr_stripped = self._solve_exponentiation(expr_stripped)
            if not '^' in expr_stripped:
                break

        while '*' in expr_stripped:
            expr_stripped = self._solve_multiplication(expr_stripped)
            if not '*' in expr_stripped:
                break

        while '/' in expr_stripped:
            expr_stripped = self._solve_division(expr_stripped)
            if not '/' in expr_stripped:
                break

        while '+' in expr_stripped:
            expr_stripped = self._solve_addition(expr_stripped)
            if not '+' in expr_stripped:
                break

        while len(findall('\d+\-\d+', expr_stripped)) > 0:
        # while '-' in expression:
            expr_stripped = self._solve_subtraction(expr_stripped)
            if not '-' in expr_stripped:
                break

        if expr_stripped == '-0':
            expr_stripped = '0'

        return str(expr_stripped)

    def _solve_parentheses(self, expr):
        """
        Solves the equations in parentheses first.

        :param expr: Expression with parentheses to solve.
        :type expr: String.

        :return:  What whole equation including the parentheses expression is as string.
        """

        logger = getLogger('ExpressionSolver._solve_parentheses')
        logger.setLevel(self.__logLevel)

        expr = reSub('\)\(', ')*(', expr)
        expr = reSub('(\d+)\(', '\\1*(', expr)

        expr2 = expr[search('\(', expr).start():search('\)', expr).end()]
        logger.debug(' Solving parentheses: "%s"' % expr2)

        expr2_old = expr2
        expr2 = expr2.replace('(', '')
        expr2 = expr2.replace(')', '')
        replaceWith = self._solve_equation(expr2)
        logger.debug(' Parentheses equation equals: "%s"' % replaceWith)

        expr = expr.replace(expr2_old, replaceWith)
        logger.debug(' Expression is now: "%s"' % expr)
        return expr

    def _solve_exponentiation(self, expr):
        """
        Solves the exponentiation equations.

        :param expr: Expression to solve.
        :type expr: String.

        :return:  What whole equation including the exponentiation expression is as string.
        """

        logger = getLogger('ExpressionSolver._solve_exponentiation')
        logger.setLevel(self.__logLevel)

        expr_sub = expr[search('\d+\^', expr).start(): search('\^\d+', expr).end()]
        logger.debug(' Solving multiplication: "%s"' % expr_sub)

        num1 = findall('\d+\^', expr)[0].replace('^', '')
        num2 = findall('\^\d+', expr)[0].replace('^', '')

        replaceWith = str(pow(int(num1), int(num2)))
        logger.debug(' Exponentiation equation equals: "%s"' % replaceWith)

        expr = expr.replace(expr_sub, replaceWith)
        logger.debug(' Expression is now: "%s"' % expr)

        return expr

    def _solve_multiplication(self, expr):
        """
        Solves the multiplication equations.

        :param expr: Expression to solve.
        :type expr: String.
        
        :return:  What whole equation including the multiplication expression is as string.
        """

        logger = getLogger('ExpressionSolver._solve_multiplication')
        logger.setLevel(self.__logLevel)

        reSub = expr[search('\d+\*', expr).start(): search('\*\d+', expr).end()]
        logger.debug(' Solving multiplication: "%s"' % reSub)

        num1 = findall('\d+\*', expr)[0].replace('*', '')
        num2 = findall('\*\d+', expr)[0].replace('*', '')

        replaceWith = str(mul(int(num1), int(num2)))
        logger.debug(' Multiplicaiton equation equals: "%s"' % replaceWith)

        expr = expr.replace(reSub, replaceWith)
        logger.debug(' Expression is now: "%s"' % expr)

        return expr

    def _solve_division(self, expr):
        """
        Solves the division equations.

        :param expr: Expression to solve.
        :type expr: String.

        :return:  What whole equation including the the division expression is as string.
        """

        logger = getLogger('ExpressionSolver._solve_division')
        logger.setLevel(self.__logLevel)

        reSub = expr[search('\d+\/', expr).start(): search('\/\d+', expr).end()]
        logger.debug(' Solving division: "%s"' % reSub)

        num1 = findall('\d+\/', expr)[0].replace('/', '')
        num2 = findall('\/\d+', expr)[0].replace('/', '')

        replaceWith = str(div(int(num1), int(num2)))
        logger.debug(' Division equation equals: "%s"' % replaceWith)

        expr = expr.replace(reSub, replaceWith)
        logger.debug(' Expression is now: "%s"' % expr)

        return expr

    def _solve_addition(self, expr):
        """
        Solves the addition equations.

        :param expr: Expression to solve.
        :type: String.

        :return:  What whole equation including the addition expression is as string.
        """

        logger = getLogger('ExpressionSolver._solve_addition')
        logger.setLevel(self.__logLevel)

        reSub = expr[search('\d+\+', expr).start(): search('\+\d+', expr).end()]
        logger.debug(' Solving addition: "%s"' % reSub)

        num1 = findall('\d+\+', expr)[0].replace('+', '')
        num2 = findall('\+\d+', expr)[0].replace('+', '')
        replaceWith = str(add(int(num1), int(num2)))
        logger.debug(' Addition equation equals: "%s"' % replaceWith)

        expr = expr.replace(reSub, replaceWith)
        logger.debug(' Expression is now: "%s"' % expr)

        return expr

    def _solve_subtraction(self, expr):
        """
        Solves the subtraction equations.

        :param expr: Expression to solve.
        :type expr: String.
        
        :return exp:  What whole equation including the subtraction expression is as string.
        """

        logger = getLogger('ExpressionSolver._solve_subtraction')
        logger.setLevel(self.__logLevel)

        reSub = expr[search('\d+\-', expr).start(): search('\-\d+', expr).end()]

        logger.debug(' Solving subtraction: "%s"' % reSub)

        num1 = findall('\d+\-', expr)[0].replace('-', '')
        num2 = findall('\-\d+', expr)[0].replace('-', '')
        replaceWith = str(sub(int(num1), int(num2)))
        logger.debug(' Subtraction equation equals: "%s"' % replaceWith)

        expr = expr.replace(reSub, replaceWith)
        logger.debug(' Expression is now: "%s"' % expr)

        return expr

    def _display_result(self, expr, result):
        """
        Displays results of self.expression and self.result to user in readable format.
        
        :param expr: Expression to solve.
        :type: String.
        :param result: Result of equation.
        :type: String.

        @return None
        """

        logger = getLogger('ExpressionSolver._display_result')
        logger.setLevel(self.__logLevel)

        logger.debug(' Displaying results.')

        print('%s = %s' % (expr, result))
        print('')

def get_args():
    """
    Get arguments from command line, and returns them as dictionary.

    :return: Dictionary of arguments.
    :type: Dictionary.
    """

    parser = ArgumentParser(description='Give rank of poker hand given five sets of tuples representing five cards.')

    parser.add_argument('-e', '--expr', dest='expression', type=str, required=True,
                        help='Expression as string.')

    parser.add_argument('--logLevel', dest='logLevel', default='INFO',
                        help='Set logging level')

    parser.add_argument('--logFile', dest='logFile', default='expressionSolver.log',
                        help='Logging file.')

    args = parser.parse_args()
    return args.__dict__

def main():
    kwargs = get_args()

    expObj = ExpressionSolver(logFile=kwargs['logFile'],logLevel=kwargs['logLevel'])
    expObj.solve(kwargs['expression'])

if __name__ == "__main__":
    main()
