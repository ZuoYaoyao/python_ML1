"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def amounts_number(record1, record2):
    count = set()
    for item in record1:
        if item[0] not in count:
            count.add(item[0])
        if item[1] not in count:
            count.add(item[1])

    for item in record2:
        if item[0] not in count:
            count.add(item[0])
        if item[1] not in count:
            count.add(item[1])
    return len(count)


print("There are {} different telephone numbers in the records.".format(amounts_number(texts, calls)))
"""
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""
