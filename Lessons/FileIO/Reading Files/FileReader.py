
fileDirectory = "C:\\Users\\teton\\python folder1\\FileIO\\Reading Files\\"
fileName = "InputFile.txt"

file = open(fileDirectory + fileName, 'r')
readText = file.read()
print(readText)
