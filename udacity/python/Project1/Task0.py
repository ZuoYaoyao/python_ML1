"""
Intro to Python Project 1, Task 0

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


def output(text, call):
    print("First record of texts,{} texts {} at time {}".format(text[0][0], text[0][1], text[0][2]))
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds"
          .format(call[-1][0], call[-1][1], call[-1][2], call[-1][3]))


output(texts, calls)

"""
TASK 0::
what is the first record of texts and what is the last record of calls
Print messages: 
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

