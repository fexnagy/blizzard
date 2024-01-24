import os
import cursor
import time

# Cls and hide cursor
os.system("cls")
cursor.hide()


# Delay function
def dl(s):
    time.sleep(s)


# Print title
file_path = "data/title.txt"

with open(file_path, "r") as file:
    dl(1)
    for line in file:
        print(line, end="")
        dl(0.5)

# Exit game
input("Press enter to continue...")
cursor.show()
