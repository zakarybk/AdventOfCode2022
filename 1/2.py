from pathlib import Path

data = Path("i.txt").read_text()

elves = data.split("\n\n")
calories = lambda foods: map(int, foods.splitlines())

largest = sorted(map(lambda foods: sum(calories(foods)), elves), reverse=True)

print(sum(largest[:3]))