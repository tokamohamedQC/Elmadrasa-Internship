stringFile = open("Python course 2/Challenge #5/strings_input.txt")
outputStringFile = open("Python course 2/Challenge #5/string_output.txt", "w")
phrase = ""

for line in stringFile:
    phrase += " " + line.strip()

print(phrase, file=outputStringFile)
outputStringFile.close()
