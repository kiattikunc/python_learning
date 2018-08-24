"1 Excel"
import csv

ifile = open('test.csv', "r")
reader = csv.reader(ifile)
ofile = open('ttest2.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in reader:
    print(row)



ifile.close()
ofile.close()

"2 variable"
target_color_name='FireBrick'
target_color_rgb= (178,34,34)
target_color_name=first_color_name='FireBrick'

print(id(target_color_name)==id(first_color_name))

total_count=0
total_count+=5
total_count+=6
print(total_count)

print('Candy')

