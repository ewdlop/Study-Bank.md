import random

def fill_in_the_blank():
    sentences = [
        "The quick brown fox _____ over the lazy dog.",
        "She will _____ the cake before the party.",
        "They went to the park to _____ basketball."
    ]
    answers = ["jumps", "bake", "play"]
    index = random.randint(0, len(sentences) - 1)
    return sentences[index], answers[index]

problem, solution = fill_in_the_blank()
print(f"Problem: {problem}")
print(f"Answer: {solution}")
