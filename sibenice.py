word = ('řeka')
word = word.upper()
lst = list(word)
lst2 = len(lst) * "_ "
lst3 = []
win = 0
lose = 0
underline = "_______________________________\n"
print(lst2)


while win<len(lst) and lose<5:
    letter = input("Zadejte písmeno:").capitalize()
    if letter.isalpha():
        if letter in lst:
            print(underline +f"Písmeno {letter} je v seznamu")
            lst2 = list(lst2)
            for i, char in enumerate(lst):
                if char == letter:
                    lst2[i * 2] = letter
                    win += 1
            print( "".join(lst2) + "\n" + "".join(lst3))
        elif letter in lst3:
            print(underline +f"Písmeno {letter} již bylo zadáno")
            print("".join(lst2) + "\n" + " ".join(lst3))
        else:
            print(underline +f"Písmeno {letter} není v seznamu")
            lst3.append(letter)
            print("".join(lst2) + "\n" + "".join(lst3))
            lose += 1
    else: print("Nejedná se o písmeno.")

if win == len(lst):
    print(f"Gratulujeme, vyhrál jsi!")
else:
    print(f"Prohrál jsi! \n Slovo bylo:{word}")
