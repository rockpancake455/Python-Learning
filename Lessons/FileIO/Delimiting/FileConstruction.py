"""

Run    T1  , T2  , T3\n
  1    50.0,49.8,82.0\n
  2    50.1,50.0,81.8\n
  3    50.2,50.2,81.9
  
"""
import os

T1Data = [20.0,20.1,20.2,20.3,20.4,20.5,20.6,20.7,20.8,20.9,21.0]
T2Data = [50.0,50.1,50.2,50.3,50.4,50.5,50.6,50.7,50.8,50.9,51.0]
T3Data = [80.0,80.1,80.2,80.3,80.4,80.5,80.6,80.7,80.8,80.9,81.0]

outputString = ""
for i in range(0, len(T1Data)):  
  outputString += f"{T1Data[i]},{T2Data[i]},{T3Data[i]}"
  if i != len(T1Data) - 1:
    outputString += "\n"

file = open(f"{os.path.dirname(__file__)}\\OutputFile.txt", 'w')
file.write(outputString)
file.close()

# outputLines: list[str] = []
# for i in range(0, len(T1Data)):
#   outputLines.append(f"{T1Data[i]},{T2Data[i]},{T3Data[i]}")
#   if i != len(T1Data) - 1:
#     outputLines[i] += "\n"

# file = open(f"{os.path.dirname(__file__)}\\OutputFile.txt", 'w')
# file.writelines(outputLines)
