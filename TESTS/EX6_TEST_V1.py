def findTheKiller(whisper: str, suspects: list[str]) -> list[str]:
    """
        Find the killer, looking for similar letters
        - Whisper: You use letters and signs
            - Use "~" for silence
            - Use "$" to define end
        - Suspects: You can put any name you want
    """
    # Normalized whisper with lower case for all letters
    normalizedWhisper = whisper.lower()
    # If ends with "$" we slice it to complete the task
    if normalizedWhisper.endswith('$'):
        normalizedWhisper = normalizedWhisper[:-1]
    # Normalized suspects with lower case each
    normalizedSuspects = [word.lower() for word in suspects]
    # Erasing duplicated
    normalizedSuspects = list(dict.fromkeys(normalizedSuspects))

    # Saving the final result
    finalSuspects = []

    for i in range(len(normalizedSuspects)):
        if len(normalizedWhisper) != len(normalizedSuspects[i]):
            continue
        counter = 0
        for j in normalizedSuspects[i]:
            for k in normalizedWhisper:
                if k == j:
                    counter += 1
        if counter > 0:
            finalSuspects.append(normalizedSuspects[i])

    return print(f"''") if len(finalSuspects) == 0 else print(finalSuspects)

print("")
findTheKiller("D~~~~~A",["Jeff","Dracula","Frankenstein","Darcula"])
findTheKiller("F~e~D~$",["Freddy","Frankenstein","Firefighter"])
findTheKiller("M~~uel",["Manuel","Minaret","Maldonado"])
findTheKiller("Mi~~DEF",["Midudev","Midu","Madeval"])
findTheKiller("A~~A~~A", ["Anna", "Amanda"])
findTheKiller("~~~~~$", ["Alice", "Bob"])
findTheKiller("Mi~~DEF",["Midudev","Midudev","Madeval"])
