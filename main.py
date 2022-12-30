import random

from collections import Counter

SLOT_ART = ["🧁", "🍪", "🍩", "🍓", "🥕", "🍕"]
SLOT_HEIGHT = len(SLOT_ART)
SLOT_WIDTH = len(SLOT_ART)
SLOT_FACE_SEPARATOR = " "


def roll_slot(number_of_slots):
    return [random.choice(SLOT_ART) for _i in range(number_of_slots)]


def generate_diagram(number_of_slots):
    rolls = roll_slot(number_of_slots)

    slots_text = " ".join(rolls)
    title_text = " RESULTS ".center(len(slots_text), "~")

    return "\n".join([title_text, slots_text, congratulate(rolls)])


def congratulate(rolls):
    counter = Counter(rolls)

    congratulation_message = ""

    for roll, count in counter.most_common():
        if count == 7:
            congratulation_message += f"x7 JackPot! you win $10000 and a permanent ban from this casino for winning too hard{roll}!\n"
        elif count == 6:
            congratulation_message += f"x6 JackPot! you win $5000 {roll}!\n"
        elif count == 5:
            congratulation_message += f"x5 JackPot! you win $500 {roll}!\n"
        elif count == 4:
            congratulation_message += f"x4 JackPot! you win $100 {roll}!\n"
        elif count == 3:
            congratulation_message += f"x3 Jackpot! you win $50 {roll}!\n"
        elif count == 2:
            congratulation_message += f"x2 Jackpot! you win $10 {roll}!\n"

    return congratulation_message


def parse_input(input_string):
    # Makes sure that only 2-7 are available options

    if input_string.strip() in {"2", "3", "4", "5", "6", "7"}:
        return int(input_string)
    else:
        print("Bruh... just enter a number from 2 to 7")
        raise SystemExit(1)


# App's main code
# 1. Get & validate input
num_slot_input = input("WELCOME TO THE CASINO, CHOOSE HOW MANY SLOTS YOU WANT [2-7] AND WIN A PRIZE / PRIZES (PICK YOUR NUMBER HERE) ======>")
num_slot = parse_input(num_slot_input)
# 3. Generate the art
slot_face_diagram = generate_diagram(num_slot)
# 4. display it
print(f"\n{slot_face_diagram}")