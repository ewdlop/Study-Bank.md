import random

# Mock functions for different sources (replace these with actual API calls)

def check_with_calculator(expression):
    try:
        result = eval(expression)
        return f"Calculator says: {result}"
    except:
        return "Calculator can't solve this."

def check_with_ai(expression):
    # Simulate AI result
    ai_result = eval(expression) + random.randint(-1, 1)  # Simulate a small deviation
    return f"AI says: {ai_result}"

def check_with_online_tool(expression):
    # Simulate an online tool's result
    return f"Online Tool says: {eval(expression)}"

def check_with_forum(expression):
    # Simulate forum response (e.g., random agreement/disagreement)
    result = eval(expression)
    forum_opinion = random.choice([f"Forum agrees: {result}", "Forum says: You're wrong!"])
    return forum_opinion

# Main function to check multiple sources
def sanity_check(expression):
    print("Checking if you're not crazy (or if everyone else is wrong):")
    print(check_with_calculator(expression))
    print(check_with_ai(expression))
    print(check_with_online_tool(expression))
    print(check_with_forum(expression))

# Example usage
expression = "5 + 3 * 2"  # Replace this with any math expression
sanity_check(expression)
