name = "-"
age = "-"
confirmation = "-"
move_on = False
# Integer for input value regarding agreeableness with criteria
agreement = 0


def confirm(char):  # Easily evaluate yes or no responses, CASEFOLD PLEASE
    if char.casefold() == "y":
        return True
    if char.casefold() == "n":
        return False


# Do an augmented assignment
def query():  # Easily query agreeableness of each criteria
    number = int(
        input(
            "1.\tStrongly Disagree\n2.\tDisagree\n3.\tNeutral\n4.\tAgree\n"
            "5.\tStrongly Agree\n"
        )
    )
    print()
    return number


def calc_percentile(input_val, max_val):  # Calculate and return percentile
    percentile = (input_val / max_val) * 100
    return percentile


while True:  # Get the patients name and age
    name = str(input("What is your name?\t"))
    print()  # Sanitize this int input so strings don't break the program
    age = int(input((f"Hello, {name}. How old are you?\t")))
    print()
    confirmation = confirm(
        str(
            input(
                f"Your name is {name}, and your age is {age}. Is that correct?\n"
                "Please input 'y' or 'n':\t"
            )
        )
    )

    if confirmation is True:
        break


# Testing criteria for BPD
print()
print(
    "Testing percentile for BPD\n"
    "Please input number indicated depending on agreement level"
)
# Significant impairments in personality functioning
print(
    "You have impairments in identity or self direction, AND "
    "impairments in empathy or intimacy"
)
agreement += query()
# Pathological personality traits
# 1. Negative affectivity
print("You have emotional liability")
agreement += query()
print("You have anxiousness")
agreement += query()
print("You have seperation anxiety")
agreement += query()
print("You have depressivity")
agreement += query()
# 2. Disinhibition
print("You have impulsivity")
agreement += query()
print("You engage in risk taking")
agreement += query()
# 3. Antagonism
print("You have hostility")
agreement += query()

# print(agreement)
# This was the old way, swapped out for top percentage for readability
# print(f"{name}, you are in the " + str(calc_percentile(agreement, 40)) + "% percentile")
print(
    f"{name}, you are in the top " + str(100 - calc_percentile(agreement, 40)) + "%"
    " for BPD"
)

# Testing for delusion (false belief)
print()  # Reset the agreement integer for new percentile
agreement = 0
print(
    "Testing percentile of delusion\n"
    "Please input number indicated depending on agreement level\n"
    "Telling the belief to others illicits response of genuine concern"
)
agreement += query()
print("Acting on the belief alienates relationship to friends and/or family")
agreement += query()
print(
    "Acting on the belief involves self mutilation, surgery, or human experimentation"
)
agreement += query()
print(
    f"{name}, you are in the top " + str(100 - calc_percentile(agreement, 15)) + "%"
    " for delusion (false belief)"
)
