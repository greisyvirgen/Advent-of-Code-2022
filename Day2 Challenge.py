# Greisy Virgen

# Scoring:
# Rock = 1, Paper = 2, Scissors = 3
# If lost +0 points, If draw +3 points, If won +6 points
# A, B, C --> Elf choices
# X, Y, Z --> My choices

# Just need to calculate my wins
def rps():
    """Rock, Paper, Scissors game."""
    file = open("day2.txt", "r")
    line = file.readlines()

    plays = {
        'Elf': [],
        'Me': []
    }

    my_plays = {
        "A": {},
        "B": {},
        "C": {}
    }

    elf_plays = {
        "A": {},
        "B": {},
        "C": {}
    }

    pts_elf = 0
    pts_me = 0

    # Create the possible choices
    # _point_calc(elf_plays, my_plays)

    # X Y Z have different meaning
    _determine_outcome(elf_plays, my_plays)

    for choice in line:
        choice = choice.split()
        elf = choice[0]
        me = choice[1]

        pts_elf += elf_plays[elf][me]
        pts_me += my_plays[elf][me]

    return pts_me


def _point_calc(elf_pts, me_pts):
    """
    Helper function to determine winner and points.
    :param c1: Elf's choice
    :param c2: My choice
    :return: points
    """
    rock, paper, scissors = 1, 2, 3
    win = 6
    draw = 3
    lost = 0

    if "A":
        # Elf chose rock

        if "X":
            # Rock v. Rock
            # pts_elf = (rock + draw)
            # pts_me = (rock + draw)
            me_pts["A"]["X"] = (rock + draw)
            elf_pts["A"]["X"] = (rock + draw)

        if "Y":
            # Rock v. Paper
            # pts_me = (rock + win)
            me_pts["A"]["Y"] = (paper + win)
            elf_pts["A"]["Y"] = rock

        if "Z":
            # Rock v. Scissors
            # pts_elf = (rock + win)
            me_pts["A"]["Z"] = scissors
            elf_pts["A"]["Z"] = (rock + win)

    if "B":
        # Elf chose Paper

        if "X":
            # Paper v. Rock
            # pts_elf = (paper + win)
            me_pts["B"]["X"] = rock
            elf_pts["B"]["X"] = (paper + win)

        if "Y":
            # Paper v. Paper
            # pts_me = (paper + draw)
            # pts_elf = (paper + draw)
            me_pts["B"]["Y"] = (paper + draw)
            elf_pts["B"]["Y"] = (paper + draw)

        if "Z":
            # Paper v. Scissors
            # pts_me = (scissors + win)
            me_pts["B"]["Z"] = (scissors + win)
            elf_pts["B"]["Z"] = paper

    if "C":
        # Elf chose scissors

        if "X":
            # Scissors v. Rock
            # pts_me = (rock + win)
            me_pts["C"]["X"] = (rock + win)
            elf_pts["C"]["X"] = scissors

        if "Y":
            # Scissors v. Paper
            # pts_elf = (scissors + win)
            me_pts["C"]["Y"] = paper
            elf_pts["C"]["Y"] = (scissors + win)

        if "Z":
            # Scissors v. Scissors
            # pts_me = (scissors + draw)
            # pts_elf = (scissors + draw)
            me_pts["C"]["Z"] = (scissors + draw)
            elf_pts["C"]["Z"] = (scissors + draw)


def _determine_outcome(elf_pts, me_pts):
    """
    Helper function that X means I loose,
    Y means draw, and Z means I win.
    """
    rock, paper, scissors = 1, 2, 3
    win = 6
    draw = 3

    # X - LOSE
    # Y - DRAW
    # Z - WIN

    if "A":
        # Elf chose rock

        if "X":     # LOSE
            # Rock v. Rock
            # pts_elf = (rock + draw)
            # pts_me = (rock + draw)
            me_pts["A"]["X"] = scissors
            elf_pts["A"]["X"] = (rock + win)

        if "Y":     # DRAW
            # Rock v. Paper
            # pts_me = (rock + win)
            me_pts["A"]["Y"] = (rock + draw)
            elf_pts["A"]["Y"] = (rock + draw)

        if "Z":     # WIN
            # Rock v. Scissors
            # pts_elf = (rock + win)
            me_pts["A"]["Z"] = (paper + win)
            elf_pts["A"]["Z"] = rock

    if "B":
        # Elf chose Paper

        if "X":     # Lose
            # Paper v. Rock
            # pts_elf = (paper + win)
            me_pts["B"]["X"] = rock
            elf_pts["B"]["X"] = (paper + win)

        if "Y":     # draw
            # Paper v. Paper
            # pts_me = (paper + draw)
            # pts_elf = (paper + draw)
            me_pts["B"]["Y"] = (paper + draw)
            elf_pts["B"]["Y"] = (paper + draw)

        if "Z":     # win
            # Paper v. Scissors
            # pts_me = (scissors + win)
            me_pts["B"]["Z"] = (scissors + win)
            elf_pts["B"]["Z"] = paper

    if "C":
        # Elf chose scissors

        if "X":      # lose
            # Scissors v. Rock
            # pts_me = (rock + win)
            me_pts["C"]["X"] = paper
            elf_pts["C"]["X"] = (scissors + win)

        if "Y":     # draw
            # Scissors v. Paper
            # pts_elf = (scissors + win)
            me_pts["C"]["Y"] = (scissors + draw)
            elf_pts["C"]["Y"] = (scissors + draw)

        if "Z":     # win
            # Scissors v. Scissors
            # pts_me = (scissors + draw)
            # pts_elf = (scissors + draw)
            me_pts["C"]["Z"] = (rock + win)
            elf_pts["C"]["Z"] = scissors


if __name__ == "__main__":
    print(rps())
