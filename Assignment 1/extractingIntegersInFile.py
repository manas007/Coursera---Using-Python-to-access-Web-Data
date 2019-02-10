""" Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_166936.txt (There are 85 values and the sum ends with 98 """


import re

fileHandler = open('regex_sum_42.txt', 'r')
numList = list()
totalSum = 0
x = None

for line in fileHandler:
    x = re.findall('[0-9]+', line)
    if len(x) < 1:
        continue
    else:
        for number in x:
            numList.append(int(number))
            totalSum += int(number)

print(numList)
