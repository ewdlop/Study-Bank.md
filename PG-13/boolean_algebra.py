from pyeda.inter import exprvars, And, Or, Not
A, B, C = exprvars('A B C')
expression = And(A, Or(Not(B), C))
print(expression.satisfy_all())