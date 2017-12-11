"""
Intro to Python Lab 1, Task 2

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


def max_time(record):
    call_dict = {}
    number = ""
    time = 0
    for item in record:
        if item[0] in call_dict:
            call_dict[item[0]] += int(item[3])
        else:
            call_dict[item[0]] = int(item[3])
        if item[1] in call_dict:
            call_dict[item[1]] += int(item[3])
        else:
            call_dict[item[1]] = int(item[3])
    for key in call_dict:
        if time < call_dict[key]:
            time = call_dict[key]
            number = key
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, time))


# call function
max_time(calls)


"""
TASK 2:: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""