import random
import sympy as sp
from typing import Tuple, List

class LebesgueIntegrationGenerator:
    def __init__(self):
        self.x = sp.Symbol('x')
        self.problem_types = [
            self.generate_simple_function,
            self.generate_characteristic_function,
            self.generate_countable_sum,
            self.generate_measure_zero_set
        ]

    def generate_simple_function(self) -> Tuple[str, str]:
        """Generate a problem involving a simple function."""
        values = [random.randint(1, 5) for _ in range(3)]
        intervals = [(i, i+1) for i in range(3)]
        
        function_def = " + ".join([
            f"{val}*χ_{{{a},{b}}}(x)" 
            for val, (a, b) in zip(values, intervals)
        ])
        
        problem = f"""
Find the Lebesgue integral of the simple function:
f(x) = {function_def}
over the interval [0,3]
where χ_{{a,b}} denotes the characteristic function on [a,b].
"""
        
        solution = sum(val * (b-a) for val, (a, b) in zip(values, intervals))
        solution_explanation = f"""
Solution:
For a simple function, we use the definition: ∫f dμ = Σ(a_i * μ(E_i))
where a_i are the function values and E_i are the measurable sets.

Calculating each term:
{' + '.join([f'{val}*({b}-{a})' for val, (a, b) in zip(values, intervals)])}
= {solution}
"""
        return problem, solution_explanation

    def generate_characteristic_function(self) -> Tuple[str, str]:
        """Generate a problem involving characteristic functions."""
        a = random.randint(-2, 2)
        b = a + random.randint(1, 3)
        
        problem = f"""
Calculate the Lebesgue integral of:
f(x) = χ_{{{a},{b}}}(x)
over R, where χ_{{{a},{b}}} is the characteristic function of [{a},{b}].
"""
        
        solution = b - a
        solution_explanation = f"""
Solution:
For a characteristic function, the Lebesgue integral equals the measure of the set.
∫χ_{{[{a},{b}]}} dx = μ([{a},{b}]) = {b} - ({a}) = {solution}

This follows from the definition of Lebesgue integral for simple functions,
since a characteristic function is a simple function taking values 0 and 1.
"""
        return problem, solution_explanation

    def generate_countable_sum(self) -> Tuple[str, str]:
        """Generate a problem involving countable sums."""
        n = random.randint(2, 4)
        coefficients = [1/2**i for i in range(1, n+1)]
        
        problem = f"""
Calculate the Lebesgue integral of the following countable sum:
f(x) = Σ_{{{1}}}^{{{n}}} (1/2^n) * χ_{{[n,n+1]}}(x)
over R.
"""
        
        solution = sum(coefficients)
        solution_explanation = f"""
Solution:
By the monotone convergence theorem, we can interchange the sum and integral:
∫(Σ_{1}^{n} (1/2^n) * χ_{{[n,n+1]}}) dx = Σ_{1}^{n} (1/2^n) * ∫χ_{{[n,n+1]}} dx

Each characteristic function integrates to 1 over its interval.
Therefore: Σ_{1}^{n} (1/2^n) * 1 = {solution}
"""
        return problem, solution_explanation

    def generate_measure_zero_set(self) -> Tuple[str, str]:
        """Generate a problem involving sets of measure zero."""
        problem = """
Let C be the Cantor set on [0,1]. Calculate the Lebesgue integral of:
f(x) = χ_C(x)
over [0,1], where χ_C is the characteristic function of the Cantor set.
"""
        
        solution_explanation = """
Solution:
The Cantor set C has Lebesgue measure zero.
Therefore, ∫χ_C dx = μ(C) = 0

This follows from the fact that at each step of the Cantor set construction,
we remove 1/3 of the remaining intervals, leading to a total measure of zero.
"""
        return problem, solution_explanation

    def generate_problem(self) -> Tuple[str, str]:
        """Generate a random Lebesgue integration problem."""
        generator = random.choice(self.problem_types)
        return generator()

# Example usage
generator = LebesgueIntegrationGenerator()

def generate_practice_set(num_problems: int = 3) -> List[Tuple[str, str]]:
    """Generate a set of practice problems with solutions."""
    return [generator.generate_problem() for _ in range(num_problems)]


generate_practice_set(3)
