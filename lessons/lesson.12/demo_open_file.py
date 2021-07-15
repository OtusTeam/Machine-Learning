from datetime import datetime

# file = open("text.txt", "r")
# print(file.readlines())
# file.close()
#

with open("text.txt", "r") as file:
    print(file.readlines())


with open("text.txt", "w") as file:
    file.write("Hello file!\n")
    file.write(str(datetime.now()))


with open("text.txt", "a") as file:
    file.write("\nAppended line")
