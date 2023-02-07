import numpy as np
from sympy.utilities.lambdify import lambdify
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
import math
from scipy.optimize import minimize

obj_eq_inp = input('Objective Equation: ')

design_var_inp = list(input('Enter design variables: '))

num_of_const_eqs = int(input('Enter # of constraint equations: '))

constraints = []

bnds = []


def constraint_fun(eq):
    return eq(*x)


def make_f(i):
    def f(x):
        return i(*x)

    return f


# get constraint equations
for num in range(0, num_of_const_eqs):
    const = {}

    constraint_inp = input(f'Constraint Equation {num+1}: ')

    equation = lambdify(design_var_inp, constraint_inp)
    constraint = make_f(equation)

    type_input = input('Constraint Type (ineq/eq): ')

    const['type'] = type_input

    const['fun'] = constraint

    constraints.append(const)

x0 = []

for design_variable in design_var_inp:
    # get bounds

    lb = (float(input(f'{design_variable} lower bound: ')))
    ub = (float(input(f'{design_variable} upper bound: ')))

    x0.append((ub+lb)/2)

    bound = (lb, ub)

    bnds.append(bound)


def objective(x):
    obj_eq = lambdify(design_var_inp, obj_eq_inp)

    return obj_eq(*x)

solution = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=constraints)
x = solution.x

print(f'objective of x0: {objective(x0)}')
# show final objective
print(solution)

for index, solution in enumerate(solution.x):
    print(f'{design_var_inp[index]}: {solution}')




# ans for cantilever:

# Objective Equation: 7800*.6*3.14*((d**2)-(d-2*t)**2)*.25
# Enter design variables: dt
# Enter # of constraint equations: 2
# Constraint Equation 1: .005*(3*210*10**9*3.14159)*(d**4-(d-2*t)**4)-64*5000*.6**3
# Constraint Type (ineq/eq): ineq
# Constraint Equation 2: 250*3.14159*(d**4-(d-2*t)**4)-10**-6*32*5000*.6*d
# Constraint Type (ineq/eq): ineq
# d lower bound: .02
# d upper bound: .06
# t lower bound: .002
# t upper bound: .008
# Final Objective: 4.511618093224392
# d: 0.059999995697493896
# t: 0.005648677015782783




#
#
# Objective Equation: 73513.268*(2*r*t-t**2)
# Enter design variables: rt
# Enter # of constraint equations: 3
# Constraint Equation 1: r**3-.0012796*(2*r-t)
# Constraint Type (ineq/eq): ineq
# Constraint Equation 2: 15707.963*(2*r*t-t**2)-1
# Constraint Type (ineq/eq): ineq
# Constraint Equation 3: r-20*t
# Constraint Type (ineq/eq): ineq
# r lower bound: .02
# r upper bound: .2
# t lower bound: .001
# t upper bound: .01
#      fun: 2.8670174520000007
#      jac: array([ 147.02653602, 2793.50308853])
#  message: 'Inequality constraints incompatible'
#     nfev: 44
#      nit: 13
#     njev: 12
#   status: 4
#  success: False
#        x: array([0.02 , 0.001])
# r: 0.020000000000000004
# t: 0.001






