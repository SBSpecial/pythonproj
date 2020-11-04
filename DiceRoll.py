import random

def die4():
    print(random.randint(1, 4))

def die6():
    print(random.randint(1, 6))

def die8():
    print(random.randint(1, 8))

def die10():
    print(random.randint(1, 10))

def die12():
    print(random.randint(1, 12))

def die20():
    print(random.randint(1, 20))

def main():

    die_list = []
    roll_list = []
    # Get user input die
    die_type = input("What die would you like to roll from the following list: d4 d6 d8 d10 d12 d20\n")
    die_list.append(die_type)

    while True:
        die_type = input("Would you like to roll any other die from the following list: d4 d6 d8 d10 d12 d20\n Enter q to quit entering die types\n")

        if die_type.lower() == "q":
            break
        die_list.append(die_type)

    for die in die_list:
        num_roll = int(input("How many times would you like to roll this die {}?".format(die)))

        if die == "d4":
            for i in range(num_roll):
                die4()
        elif die == "d6":
            for i in range(num_roll):
                die6()
        elif die == "d8":
            for i in range(num_roll):
                die8()
        elif die == "d10":
            for i in range(num_roll):
                die10()
        elif die == "d12":
            for i in range(num_roll):
                die12()
        elif die == "d20":
            for i in range(num_roll):
                die20()
        else:
            print("Uh")


if __name__ == '__main__':
    main()
