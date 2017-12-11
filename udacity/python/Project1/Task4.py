"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
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


def find_telemarketers(text, call):
    # init var
    result = []
    result1 = set()
    set1 = set()
    set2 = set()
    set3 = set()

    for item in call:
        # construct set with hidden telemarketers
        result1.add(item[0])
        # never receive call
        set1.add(item[1])
        # find 140
        if item[0][0:3] == '140':
            if item[0] not in result:
                result.append(item[0])

    for item in text:
        # never send txt
        set2.add(item[0])
        # never receive txt
        set3.add(item[1])

    # Difference to remove unqualified ones
    result1 = result1 - set1
    result1 = result1 - set2
    result1 = result1 - set3

    # append to list
    for item in result1:
        result.append(item)
    # output results
    result.sort()
    print("These numbers could be telemarketers:")
    for item in result:
        print(item)


# call the function
find_telemarketers(texts, calls)

"""
    another way
    # never receive call
    for item in call:
        if item[1] in result1:
            result1.remove(item[1])

    # never text
    for item in text:
        # never send text
        if item[0] in result1:
            result1.remove(item[0])
        # never receive text
        if item[1] in result1:
            result1.remove(item[1])
    """


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
