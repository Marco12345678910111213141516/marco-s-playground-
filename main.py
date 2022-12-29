# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def convert_to(unit, weight):
    if unit.upper() == "K":
        converted = weight / .45359
        return "Weight in Lbs: " + str(converted)
    elif unit.upper() == 'L' or unit.upper() == "P":
        converted = weight * 0.45359
        return "Weight in Kg: " + str(converted)

    return 'Bullshit'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    weight = float(input("Weight: "))
    while True:
        unit = input("(K)g or (L)bs")
        converted = convert_to(unit[0], weight)
        print(converted)
        if converted != 'Bullshit':
            print("And that´s your weight")
            quit(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
