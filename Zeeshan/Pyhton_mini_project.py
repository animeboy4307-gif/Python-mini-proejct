"""
Advanced Dice Roller with Statistics
Run in VS Code: open this file and press the Run button (or `python dice_roller.py`).
"""

import random
from collections import Counter

MAX_BAR_WIDTH = 40  # longest bar in the histogram


def get_positive_int(prompt, minimum=1, maximum=10_000):
    """Keep asking until the user enters a valid whole number in range."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if value < minimum or value > maximum:
            print(f"  Please enter a number between {minimum} and {maximum}.")
            continue
        return value


def roll_dice(num_dice, sides):
    """Roll `num_dice` dice with `sides` sides and return the results as a list."""
    return [random.randint(1, sides) for _ in range(num_dice)]


def print_roll_summary(results, roll_number):
    """Show the result of a single roll."""
    print(f"\nRoll #{roll_number}: {results}")
    print(f"  Sum of this roll: {sum(results)}")


def print_statistics(history, sides):
    """Print totals, averages and a text-based frequency graph."""
    if not history:
        print("\nNo rolls yet.")
        return

    total_sum = sum(history)
    count = len(history)
    average = total_sum / count
    counter = Counter(history)
    most_common_value, most_common_count = counter.most_common(1)[0]

    print("\n" + "=" * 55)
    print("STATISTICS")
    print("=" * 55)
    print(f"Total dice rolled : {count}")
    print(f"Sum of all rolls  : {total_sum}")
    print(f"Average per die   : {average:.2f}  (expected: {(sides + 1) / 2:.2f})")
    print(f"Lowest / Highest  : {min(history)} / {max(history)}")
    print(f"Most frequent     : {most_common_value} (appeared {most_common_count}x)")

    print("\nFREQUENCY DISTRIBUTION")
    print("-" * 55)
    max_count = max(counter.values())
    width = len(str(sides))

    for face in range(1, sides + 1):
        face_count = counter.get(face, 0)
        bar_length = round(face_count / max_count * MAX_BAR_WIDTH) if max_count else 0
        # Make sure a face that appeared at least once always shows a bar
        if face_count > 0 and bar_length == 0:
            bar_length = 1
        percent = face_count / count * 100
        bar = "#" * bar_length
        print(f"{face:>{width}} | {bar} {face_count} ({percent:.1f}%)")
    print("-" * 55)


def main():
    print("=" * 55)
    print("   ADVANCED DICE ROLLER WITH STATISTICS")
    print("=" * 55)

    while True:  # outer loop: choose dice settings
        sides = get_positive_int("\nHow many sides per die? (e.g. 6, 20): ", minimum=2)
        history = []        # every individual die result
        roll_count = 0

        while True:  # inner loop: keep rolling with the same die type
            num_dice = get_positive_int("How many dice to roll? ", maximum=1000)
            results = roll_dice(num_dice, sides)
            history.extend(results)
            roll_count += 1

            print_roll_summary(results, roll_count)
            print_statistics(history, sides)

            choice = input(
                "\n[Enter] roll again | [n] new dice type (clears history) | [q] quit: "
            ).strip().lower()

            if choice == "q":
                print("\nThanks for rolling! Goodbye.")
                return
            if choice == "n":
                print("\nHistory cleared. Starting fresh.")
                break


if __name__ == "__main__":
    main()