from one_v2 import play_round, Hand

rounds = [
    'A Y',
    'B X',
    'C Z'
]

score = sum(
    play_round(*map(Hand, r.split()))
    for r in rounds
)

print(score)
assert score == 15
