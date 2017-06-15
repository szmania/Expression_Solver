__author__='szmania'

#
# Created by Curtis Szmania
# Date: 4/18/17
# Comment: PLEXSYS coding assessment
#

import sys
import re
import operator
import logging


class ExpressionSolver(object):
    def __init__(self, logLevel='DEBUG', logFile='log.log'):
        self.logLevel = logLevel
        self.logger = logging.getLogger('Expressions.__init__')
        self._setLogger(logFile=logFile)


    @property
    def logLevel(self):
        return self._logLevel

    @logLevel.setter
    def logLevel(self, level):
        self._logLevel = level

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, expr):
        self._expression = expr

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def _setLogger(self, logFile):
        """
        Logger setup.

        :param logFile:  Log file path.
        :type logFile: String.

        :return:
        """

        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        self.handler = logging.FileHandler(logFile)
        formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

        # formatter = logging.Formatter(fmt='%(message)s', datefmt='')
        self.handler.setFormatter(formatter)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        root.addHandler(self.handler)
        root.addHandler(ch)


    def run(self, expr):
        """
        Evaluates expression self._expression and returns value.

        :param expr: ExpressionSolver to solve. ie: "(1 + 2) / 3"
        :param expr: String.

        :return:  What the expression equals as a string.
        """

        logger = logging.getLogger('Expressions.run')
        logger.setLevel(self.logLevel)

        logger.debug(' Running equation solver.')

        self.expression = expr

        self.result = self._solveEquation(expr)

        self._display_result(expression=expr, result=self.result)

        return self.result



    def _solveEquation(self, expression):
        """
        Evaluates expression expression and returns value.
        
        @param expression: ExpressionSolver to solve.

        @return expression:  What the expression equals to as string.
        """

        logger = logging.getLogger('ExpressionSolver._solveEquation')
        logger.setLevel(self.logLevel)

        logger.debug(' Solve equation: "%s"' % expression)

        expression = re.sub(' ', '', expression)

        while '(' in expression:
            expression = self._solve_parentheses(expression)

        while '*' in expression:
            expression = self._solve_multiplication(expression)
            if not '*' in expression:
                break

        while '/' in expression:
            expression = self._solve_division(expression)
            if not '/' in expression:
                break


        while '+' in expression:
            expression = self._solve_addition(expression)
            if not '+' in expression:
                break

        while len(re.findall('\d+\-\d+', expression)) > 0:
        # while '-' in expression:
            expression = self._solve_subtraction(expression)
            if not '-' in expression:
                break


        if expression == '-0':
            expression = '0'

        return expression


    def _solve_parentheses(self, expression):
        """
        Solves the equations in parentheses first.

        @param expression: ExpressionSolver to solve.

        @return expression:  What whole equation including the parentheses expression is as string.

        """

        logger = logging.getLogger('ExpressionSolver._solve_parentheses')
        logger.setLevel(self.logLevel)

        expression = re.sub('\)\(', ')*(', expression)
        expression = re.sub('(\d+)\(', '\\1*(', expression)

        exp = expression[re.search('\(', expression).start():re.search('\)', expression).end()]
        logger.debug(' Solving parentheses: "%s"' % exp)

        sub = exp
        exp = exp.replace('(', '')
        exp = exp.replace(')', '')
        replaceWith = self._solveEquation(exp)
        logger.debug(' Parentheses equation equals: "%s"' % replaceWith)

        expression = expression.replace(sub, replaceWith)
        logger.debug(' ExpressionSolver is now: "%s"' % expression)
        return expression


    def _solve_multiplication(self, exp):
        """
        Solves the multiplication equations.

        @param exp: ExpressionSolver to solve.

        @return exp:  What whole equation including the multiplication expression is as string.
        """

        logger = logging.getLogger('ExpressionSolver._solve_multiplication')
        logger.setLevel(self.logLevel)

        sub = exp[re.search('\d+\*', exp).start(): re.search('\*\d+', exp).end()]
        logger.debug(' Solving multiplication: "%s"' % sub)

        num1 = re.findall('\d+\*', exp)[0].replace('*', '')
        num2 = re.findall('\*\d+', exp)[0].replace('*', '')

        replaceWith = str(operator.mul(int(num1), int(num2)))
        logger.debug(' Multiplicaiton equation equals: "%s"' % replaceWith)

        exp = exp.replace(sub, replaceWith)
        logger.debug(' ExpressionSolver is now: "%s"' % exp)

        return exp


    def _solve_division(self, exp):
        """
        Solves the division equations.

        @param exp: ExpressionSolver to solve.

        @return exp:  What whole equation including the the division expression is as string.
        """

        logger = logging.getLogger('ExpressionSolver._solve_division')
        logger.setLevel(self.logLevel)

        sub = exp[re.search('\d+\/', exp).start(): re.search('\/\d+', exp).end()]
        logger.debug(' Solving division: "%s"' % sub)

        num1 = re.findall('\d+\/', exp)[0].replace('/', '')
        num2 = re.findall('\/\d+', exp)[0].replace('/', '')

        replaceWith = str(operator.div(int(num1), int(num2)))
        logger.debug(' Division equation equals: "%s"' % replaceWith)

        exp = exp.replace(sub, replaceWith)
        logger.debug(' ExpressionSolver is now: "%s"' % exp)

        return exp


    def _solve_addition(self, exp):
        """
        Solves the addition equations.

        @param exp: ExpressionSolver to solve.

        @return exp:  What whole equation including the addition expression is as string.
        """

        logger = logging.getLogger('ExpressionSolver._solve_addition')
        logger.setLevel(self.logLevel)

        sub = exp[re.search('\d+\+', exp).start(): re.search('\+\d+', exp).end()]
        logger.debug(' Solving addition: "%s"' % sub)

        num1 = re.findall('\d+\+', exp)[0].replace('+', '')
        num2 = re.findall('\+\d+', exp)[0].replace('+', '')
        replaceWith = str(operator.add(int(num1), int(num2)))
        logger.debug(' Addition equation equals: "%s"' % replaceWith)

        exp = exp.replace(sub, replaceWith)
        logger.debug(' ExpressionSolver is now: "%s"' % exp)

        return exp


    def _solve_subtraction(self, exp):
        """
        Solves the subtraction equations.

        @param exp: ExpressionSolver to solve.

        @return exp:  What whole equation including the subtraction expression is as string.
        """

        logger = logging.getLogger('ExpressionSolver._solve_subtraction')
        logger.setLevel(self.logLevel)

        sub = exp[re.search('\d+\-', exp).start(): re.search('\-\d+', exp).end()]

        logger.debug(' Solving subtraction: "%s"' % sub)

        num1 = re.findall('\d+\-', exp)[0].replace('-', '')
        num2 = re.findall('\-\d+', exp)[0].replace('-', '')
        replaceWith = str(operator.sub(int(num1), int(num2)))
        logger.debug(' Subtraction equation equals: "%s"' % replaceWith)

        exp = exp.replace(sub, replaceWith)
        logger.debug(' ExpressionSolver is now: "%s"' % exp)

        return exp


    def _display_result(self, expression, result):
        """
        Displays results of self.expression and self.result to user in readable format.
        
        :param expression: Expression to solve.
        :type: String.
        :param result: Result of equation.
        :type: String.

        @return None
        """

        logger = logging.getLogger('ExpressionSolver._display_result')
        logger.setLevel(self.logLevel)

        logger.debug(' Displaying results.')

        print('%s = %s' % (expression, result))
        print('')


def main():
    equObj = ExpressionSolver(logLevel='INFO')

    expr1 = '1 + 1'
    val1 = equObj.run(expr1)

    expr2  = '(3 + 4) * 6'
    val2 = equObj.run(expr2)

    expr3 = '(1 * 4) + (5 * 2)'
    val3 = equObj.run(expr3)

    expr4 = '(2 * 4) * 2 + (9 * 0)'
    val4 = equObj.run(expr4)

    expr5 = '(2 - 4)(9 * 0)'
    val5 = equObj.run(expr5)

    expr6 = '4(9 / 1)'
    val6 = equObj.run(expr6)

if __name__ == "__main__":
    main()
