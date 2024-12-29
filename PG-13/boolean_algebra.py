def guess_purpose():
    print("Can you guess the purpose of the boolean expression?")

from pyeda.inter import exprvars, And, Or, Not
A, B, C = exprvars('A B C')
expression = And(A, Or(Not(B), C))
print(expression.satisfy_all())

guess_purpose()
