def bowling_score(rolls):
    total = 0
    frame = 0
    is_newframe = True
    is_strike = False
    is_spare = False
    for index, roll in enumerate(rolls):
        if frame == 10:
            print(rolls[index], rolls[index - 1], index, len(rolls))
            if is_strike or is_spare:
                if index + 2 < len(rolls):
                    raise ValueError("za duża ilość rzutów")
            else:
                if index + 1 <= len(rolls):
                    raise ValueError("za duża ilość rzutów")
            break
        is_strike = False
        is_spare = False
        if roll < 0 or roll > 10:
            raise ValueError(f"Zła liczba strąconych kręgli w frame {frame+1}")
        if roll == 10:
            if index + 2 >= len(rolls):
                raise ValueError("za mała ilość rzutów")
            total += rolls[index + 1]
            total += rolls[index + 2]
            frame += 1
            is_strike = True
        elif not is_newframe:
            if rolls[index - 1] + roll > 10:
                raise ValueError(
                    f"nieprawidłowa liczba punktów drugiego rzutu  w frame {frame+1}"
                )
            elif rolls[index - 1] + roll == 10:
                if index + 1 >= len(rolls):
                    raise ValueError("za mała ilość rzutów")
                total += rolls[index + 1]
                is_spare = True
            frame += 1
            is_newframe = True
        else:
            is_newframe = False
        total += roll
    return total

