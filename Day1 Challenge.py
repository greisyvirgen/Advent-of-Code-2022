# Greisy Virgen

# In case the Elves get hungry and need extra snacks, they need to know which Elf
# to ask: they'd like to know how many Calories are being carried by the Elf carrying
# the most Calories. In the example above, this is 24000 (carried by the fourth Elf).
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def calorie_count():
    file = open('day1.txt', 'r')
    line = file.readlines()

    stats = {}
    elf_num = 1
    calories = 0

    for cal in line:
        if cal.strip():
            # If the line has a value,
            # we add it to count
            calories += int(cal)

        else:
            # We reached a blank line, add total calories
            # carried by current elf and move to the next.
            stats[f"Elf {elf_num}"] = calories
            elf_num += 1
            calories = 0

    file.close()
    return max(stats.values())


if __name__ == "__main__":
    print(calorie_count())
