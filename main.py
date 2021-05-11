
currentNum = 0
previousNum = 1

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
num = input("n = ")

sequence = [previousNum, currentNum]
newNum = 0

for i in range(int(num)):
    try:
        newNum = sequence[0] + sequence[1]

        sequence = [sequence[1], newNum]
    
    except:
        newNum = 0
        break

print(f'X{num.translate(subscript)} = {newNum}')

saveToFile = input("\nWould you like to save this to a file? |Y| or |N|  ").lower()
if saveToFile == "y":
    f = open("number.txt", "a+")
    counter = 0
    newStrList = list(str(newNum))
    for i in range(len(newStrList)):
        if counter > 100:
            f.write("\r")
            counter = 0
        f.write(newStrList[i])
        counter += 1
    
    print("File write succecfull")

input("Press enter to close...")