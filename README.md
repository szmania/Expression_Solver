# Expression Solver

## Description
This applicaiton takes an expression as a string and solves it. 

It is capable of handling parenthesis, exponentiation, multiplicaiton, division, addition and subtraction.
The program also recognizes when a number outside of the parenthesis is touching the parenthesis that it is supposed to do multiplicaiton.
All results return in whole numbers, rounded.

## Usage

### Arguments
`-e, --expr <expression>`
Expression as string. ie: (4+1)(5^2)/2

`--logFile <logging file>`
(Optional) File to output log to. ie: "log.log". Default is "expressionSolver.log".

`--logLevel <loglevel>`
(Optional) Logging level. ie: "WARN", "INFO", "DEBUG"
	
	
## Examples
### input 1:
`python expressionSolver.py --expr "(1 * 4) + (5 * 2)" --logFile log.log --logLevel WARN`
### output 1:
`(1 * 4) + (5 * 2) = 14`
	
	
### input 2:
`python expressionSolver.py --expr "4^3(9 / 1)" `
### output 2:
`4^3(9 / 1) = 576`
