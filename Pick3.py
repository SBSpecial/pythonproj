import random

def main():
    numGuess = random.randint(1,30)
    chances = 3

    print("Guess the number within three chances")
    while chances > 0:
            try:
                userGuess = int(input("Pick a number between 1 and 30: "))

                if userGuess > numGuess:
                    print("Your choice was too high, guess lower")
                    chances -= 1

                    if chances == 0:
                        print("You're out of guesses. The number was", numGuess)
                        break

                    print("You have", chances, "left")
                elif userGuess < numGuess:
                    print("Your choice was too low, guess higher")
                    chances -= 1

                    if chances == 0:
                        print("You're out of guesses, the number was", numGuess)
                        break

                    print("You have", chances, "left.")
                else:
                    print("You have guessed the proper number!")

            except (RuntimeError, ValueError, NameError):
                print("Invalid Input")
                continue


if __name__ == '__main__':
    main()
