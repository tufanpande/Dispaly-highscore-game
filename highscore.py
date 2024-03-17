import random

def game():
    score = random.randint(1, 1100)
    print(f"The score is {score}")
    return score

score = game() #returns certain score to variable score
# Read high scores from file
with open("score.txt", "r") as f:
    highscore_lines = f.readlines()

# Convert each line to an integer and store them in a list
highscores = [int(line.strip()) for line in highscore_lines]

# Determine the highest score
highscore = max(highscores)

# Check if current score beats the high score
if score > highscore:
    # Write the new high score to the file
    with open("score.txt", "w") as f:
        f.write(str(score))
else:
    print("You aren't able to beat the high score")


# with open("highscore.txt", "r") as f:
#     highscore = int(f.read())
# if highscore<score:
#     with open("highscore.txt", "w") as f:
#         f.write(f"{score}")
# else:
#     print("You aren't able to beat the high score")
      