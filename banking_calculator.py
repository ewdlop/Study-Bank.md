#!/usr/bin/env python3
"""
Banking Calculations and Problem Generator

This module provides functions for common banking calculations and generates
practice problems for studying banking fundamentals.
"""

import random
import math


def simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Args:
        principal (float): Principal amount
        rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time (float): Time in years
    
    Returns:
        float: Interest amount
    """
    return principal * rate * time


def compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.
    
    Args:
        principal (float): Principal amount
        rate (float): Annual interest rate (as decimal)
        time (float): Time in years
        n (int): Number of times interest is compounded per year
    
    Returns:
        float: Final amount (principal + interest)
    """
    return principal * math.pow(1 + rate / n, n * time)


def calculate_apy(apr, n=12):
    """
    Calculate Annual Percentage Yield from APR.
    
    Args:
        apr (float): Annual Percentage Rate (as decimal)
        n (int): Number of compounding periods per year
    
    Returns:
        float: Annual Percentage Yield (as decimal)
    """
    return math.pow(1 + apr / n, n) - 1


def loan_payment(principal, annual_rate, years):
    """
    Calculate monthly loan payment using amortization formula.
    
    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate (as decimal)
        years (int): Loan term in years
    
    Returns:
        float: Monthly payment amount
    """
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    if monthly_rate == 0:
        return principal / num_payments
    
    payment = principal * (monthly_rate * math.pow(1 + monthly_rate, num_payments)) / \
              (math.pow(1 + monthly_rate, num_payments) - 1)
    return payment


def money_multiplier(reserve_ratio):
    """
    Calculate the money multiplier effect.
    
    Args:
        reserve_ratio (float): Reserve requirement ratio (as decimal)
    
    Returns:
        float: Money multiplier
    """
    return 1 / reserve_ratio


def total_money_created(initial_deposit, reserve_ratio):
    """
    Calculate total money that can be created through fractional reserve banking.
    
    Args:
        initial_deposit (float): Initial deposit amount
        reserve_ratio (float): Reserve requirement ratio (as decimal)
    
    Returns:
        float: Total money that can be created
    """
    return initial_deposit * money_multiplier(reserve_ratio)


def calculate_roa(net_income, total_assets):
    """
    Calculate Return on Assets.
    
    Args:
        net_income (float): Net income
        total_assets (float): Total assets
    
    Returns:
        float: ROA as percentage
    """
    return (net_income / total_assets) * 100


def calculate_roe(net_income, shareholders_equity):
    """
    Calculate Return on Equity.
    
    Args:
        net_income (float): Net income
        shareholders_equity (float): Shareholders' equity
    
    Returns:
        float: ROE as percentage
    """
    return (net_income / shareholders_equity) * 100


def generate_interest_problem():
    """Generate a random simple or compound interest problem."""
    problem_type = random.choice(['simple', 'compound'])
    principal = random.randint(1000, 50000)
    rate = round(random.uniform(0.02, 0.08), 3)
    time = random.randint(1, 10)
    
    if problem_type == 'simple':
        interest = simple_interest(principal, rate, time)
        problem = f"Calculate the simple interest on ${principal:,} at {rate*100}% annual rate for {time} years."
        solution = f"I = P × r × t = {principal} × {rate} × {time} = ${interest:,.2f}"
        answer = interest
    else:
        n = random.choice([1, 4, 12])  # annually, quarterly, monthly
        freq_map = {1: 'annually', 4: 'quarterly', 12: 'monthly'}
        final_amount = compound_interest(principal, rate, time, n)
        problem = f"Calculate the final amount on ${principal:,} at {rate*100}% annual rate compounded {freq_map[n]} for {time} years."
        solution = f"A = P(1 + r/n)^(nt) = {principal}(1 + {rate}/{n})^({n}×{time}) = ${final_amount:,.2f}"
        answer = final_amount
    
    return {
        'problem': problem,
        'solution': solution,
        'answer': answer
    }


def generate_loan_problem():
    """Generate a random loan payment calculation problem."""
    principal = random.randint(5000, 100000)
    rate = round(random.uniform(0.03, 0.10), 3)
    years = random.choice([3, 4, 5, 7, 10, 15, 20, 30])
    
    monthly_payment = loan_payment(principal, rate, years)
    
    problem = f"Calculate the monthly payment for a ${principal:,} loan at {rate*100}% annual interest for {years} years."
    solution = f"Using the amortization formula: M = ${monthly_payment:,.2f}"
    
    return {
        'problem': problem,
        'solution': solution,
        'answer': monthly_payment
    }


def generate_apy_problem():
    """Generate a random APY calculation problem."""
    apr = round(random.uniform(0.02, 0.08), 3)
    n = random.choice([1, 4, 12, 365])
    freq_map = {1: 'annually', 4: 'quarterly', 12: 'monthly', 365: 'daily'}
    
    apy = calculate_apy(apr, n)
    
    problem = f"A bank offers {apr*100}% APR compounded {freq_map[n]}. What is the APY?"
    solution = f"APY = (1 + {apr}/{n})^{n} - 1 = {apy*100:.3f}%"
    
    return {
        'problem': problem,
        'solution': solution,
        'answer': apy
    }


def generate_money_multiplier_problem():
    """Generate a random money multiplier problem."""
    reserve_ratio = round(random.uniform(0.05, 0.20), 2)
    deposit = random.randint(10000, 100000)
    
    multiplier = money_multiplier(reserve_ratio)
    total = total_money_created(deposit, reserve_ratio)
    
    problem = f"If the reserve requirement is {reserve_ratio*100}% and a customer deposits ${deposit:,}, how much total money can be created?"
    solution = f"Money Multiplier = 1/{reserve_ratio} = {multiplier:.2f}\nTotal = ${deposit:,} × {multiplier:.2f} = ${total:,.2f}"
    
    return {
        'problem': problem,
        'solution': solution,
        'answer': total
    }


def generate_practice_problems(num_problems=10):
    """
    Generate a set of random banking practice problems.
    
    Args:
        num_problems (int): Number of problems to generate
    
    Returns:
        list: List of problem dictionaries
    """
    problem_generators = [
        generate_interest_problem,
        generate_loan_problem,
        generate_apy_problem,
        generate_money_multiplier_problem
    ]
    
    problems = []
    for i in range(num_problems):
        generator = random.choice(problem_generators)
        problem = generator()
        problem['number'] = i + 1
        problems.append(problem)
    
    return problems


def print_problems(problems, show_solutions=False):
    """
    Print banking practice problems.
    
    Args:
        problems (list): List of problem dictionaries
        show_solutions (bool): Whether to show solutions
    """
    print("=" * 70)
    print("BANKING PRACTICE PROBLEMS")
    print("=" * 70)
    print()
    
    for p in problems:
        print(f"Problem {p['number']}:")
        print(p['problem'])
        print()
        
        if show_solutions:
            print("Solution:")
            print(p['solution'])
            print()
    
    if not show_solutions:
        print("\n" + "=" * 70)
        print("SOLUTIONS")
        print("=" * 70)
        print()
        
        for p in problems:
            print(f"Problem {p['number']}:")
            print(p['solution'])
            print()


def banking_calculator():
    """Interactive banking calculator."""
    print("\n" + "=" * 50)
    print("BANKING CALCULATOR")
    print("=" * 50)
    print("\nChoose a calculation:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. APY from APR")
    print("4. Monthly Loan Payment")
    print("5. Money Multiplier")
    print("6. Return on Assets (ROA)")
    print("7. Return on Equity (ROE)")
    print("8. Generate Practice Problems")
    print("9. Exit")
    
    choice = input("\nEnter your choice (1-9): ")
    
    if choice == '1':
        principal = float(input("Enter principal amount: $"))
        rate = float(input("Enter annual interest rate (as %): ")) / 100
        time = float(input("Enter time in years: "))
        interest = simple_interest(principal, rate, time)
        print(f"\nSimple Interest: ${interest:,.2f}")
        print(f"Total Amount: ${principal + interest:,.2f}")
    
    elif choice == '2':
        principal = float(input("Enter principal amount: $"))
        rate = float(input("Enter annual interest rate (as %): ")) / 100
        time = float(input("Enter time in years: "))
        n = int(input("Enter compounding frequency per year (1=annually, 4=quarterly, 12=monthly): "))
        final = compound_interest(principal, rate, time, n)
        print(f"\nFinal Amount: ${final:,.2f}")
        print(f"Interest Earned: ${final - principal:,.2f}")
    
    elif choice == '3':
        apr = float(input("Enter APR (as %): ")) / 100
        n = int(input("Enter compounding frequency per year: "))
        apy = calculate_apy(apr, n)
        print(f"\nAPY: {apy*100:.3f}%")
    
    elif choice == '4':
        principal = float(input("Enter loan amount: $"))
        rate = float(input("Enter annual interest rate (as %): ")) / 100
        years = int(input("Enter loan term in years: "))
        payment = loan_payment(principal, rate, years)
        total_paid = payment * years * 12
        total_interest = total_paid - principal
        print(f"\nMonthly Payment: ${payment:,.2f}")
        print(f"Total Amount Paid: ${total_paid:,.2f}")
        print(f"Total Interest Paid: ${total_interest:,.2f}")
    
    elif choice == '5':
        reserve_ratio = float(input("Enter reserve requirement ratio (as %): ")) / 100
        deposit = float(input("Enter initial deposit: $"))
        multiplier = money_multiplier(reserve_ratio)
        total = total_money_created(deposit, reserve_ratio)
        print(f"\nMoney Multiplier: {multiplier:.2f}")
        print(f"Total Money Created: ${total:,.2f}")
    
    elif choice == '6':
        net_income = float(input("Enter net income: $"))
        total_assets = float(input("Enter total assets: $"))
        roa = calculate_roa(net_income, total_assets)
        print(f"\nReturn on Assets (ROA): {roa:.2f}%")
    
    elif choice == '7':
        net_income = float(input("Enter net income: $"))
        equity = float(input("Enter shareholders' equity: $"))
        roe = calculate_roe(net_income, equity)
        print(f"\nReturn on Equity (ROE): {roe:.2f}%")
    
    elif choice == '8':
        num = int(input("Enter number of problems to generate: "))
        show_sol = input("Show solutions immediately? (y/n): ").lower() == 'y'
        problems = generate_practice_problems(num)
        print_problems(problems, show_solutions=show_sol)
    
    elif choice == '9':
        print("\nThank you for using the Banking Calculator!")
        return
    
    else:
        print("\nInvalid choice. Please try again.")
    
    print()


def main():
    """Main function to run the banking calculator or generate problems."""
    print("=" * 50)
    print("BANKING FUNDAMENTALS - CALCULATION TOOL")
    print("=" * 50)
    print("\nThis tool helps you practice banking calculations.")
    
    while True:
        banking_calculator()
        again = input("Would you like to perform another calculation? (y/n): ")
        if again.lower() != 'y':
            break
    
    print("\nHappy studying!")


if __name__ == "__main__":
    # Example usage: Generate and print 5 practice problems
    print("Example: Generating 5 random banking practice problems\n")
    problems = generate_practice_problems(5)
    print_problems(problems, show_solutions=True)
    
    # Run interactive calculator
    print("\n" * 2)
    main()
