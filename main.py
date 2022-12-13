

tempNumber = 1
triedCounter = 1
gotOneCounter = 1

if __name__ == '__main__':
    while tempNumber >= 0:
        tempNumber = int(tempNumber) + 1

        if tempNumber % 2:
            tempNumber = int(tempNumber) / 2
            if int(tempNumber) == 1:
                gotOneCounter += 1

            triedCounter += 1
        else:
            tempNumber = int(tempNumber) * 3 + 1
            if int(tempNumber) == 1:
                gotOneCounter += 1

            triedCounter += 1

        print("[Brute Force] [3X + 1 System Message] New combination tried.")

        print(f"[Brute Force] [3X + 1 System Message] {triedCounter} Combinations tried so far.")
        print(f"[Brute Force] [3X + 1 System Message] {gotOneCounter} Loops passed so far.")

        print('test')
