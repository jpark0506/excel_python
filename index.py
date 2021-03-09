from openpyxl import Workbook
import random

def isEnglish(input):
    for c in input:
        if ord('가') <= ord(c) <= ord('힣'):
            return False;
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            return True;

def distinguish(input):
    cnt=0
    for i in input:
        if isEnglish(i):
            cnt=cnt+1
            continue
        elif isEnglish(i)==False:
            return [input[0:cnt+1].strip(),input[cnt+1:].strip()]
            break;




write = Workbook()

word = open("word.txt", "r")

write_text = write.create_sheet('text')

write_text = write.active

lines=[]

print("not shuffled")
for line in word:
    lines.append(distinguish(line))
random.shuffle(lines)
print("shuffled")
for line in lines:
    print(line)




for i in lines:
    write_text.append(i)

write.save('/Users/junhyeokpark/Desktop/excel_python/test.xlsx')


