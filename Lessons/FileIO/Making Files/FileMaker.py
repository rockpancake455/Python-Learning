from time import sleep

# Drive          = C:
# File Name      =                                                   FileMaker.py
# Directory      = C:\Users\teton\python folder1\FileIO\Making Files\
# File Path      = C:\Users\teton\python folder1\FileIO\Making Files\FileMaker.py
# File Extension =                                                            .py

# File Extensions
# .txt  = Text File
# .csv  = Comma Seperated Values (Value1,Value2,Value3)
# .xml  = Extensible Markup Language
# .py   = Python File
# .cs   = C# File
# .cpp  = C++ File
# .jpeg = Joint Photographic Experts Group / Image
# .png  = Portable Network Graphic / Image
# .svg  = Scalable Vector Graphic / Vector Image
# .stl  = stereolithography / 3D Model

# [#R-G-B-] Min = 0, Max = 255
# [#1C1C46] [#1C1C46] [#1C1C46]
# [#1C1C46] [#1C1C46] [#1C1C46]
# [#1C1C46] [#1C1C46] [#1C1C46]

fileDirectory = "C:\\Users\\teton\\python folder1\\FileIO\\Making Files\\"
fileName = "OutputFile.txt"
outputText = "Hello World!!"

file = open(fileDirectory + fileName, 'w')
file.write(outputText)
file.close()