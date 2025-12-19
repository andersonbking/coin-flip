import random

coin = ["heads", "tails"]
yes = ["yes", "y", "yeah", "sure", "ye", "yep","yea","ys","yse","yess","yee","yees"]

while True:
    flip = input("Ready to flip a coin? ").lower()
    print()

    if flip in yes:
        print(random.choice(coin))
        print()
    else:
        break
