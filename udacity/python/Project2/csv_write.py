import csv
import xlsx
import sys
print (sys.getdefaultencoding())
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL, escapechar='')
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])

    unicodeTypeStr = ["咕噜咕噜魔法阵‧心跳传说", 'data']
    #unicodeTypeStr = 'Russell Peters: Two Concerts, One Ticket'
    print(unicodeTypeStr)
    gbkTypeStr = unicodeTypeStr
    spamwriter.writerow(gbkTypeStr)

    print(type(unicodeTypeStr))