def display_result(strength, recomm):
    levels = {
        0: ("Very Weak", "😱"),
        1: ("Narrow", "🔴"),
        2: ("Weak", "🟠"),
        3: ("Medium", "🟡"),
        4: ("Strong", "🟢"),
        5: ("Solid", "💪"),
    }

    level_txt, emoji = levels[strength]

    if strength == 5 and not recomm:
        level_txt, emoji = "Very Solid", "⛓"

    print(f"\n{emoji} Strength: {level_txt}  ({strength}/5)")

    if recomm:
        print("*** Tips you should follow to enhance your password ***")
        for tip in recomm:
            print(f"  - {tip}")
