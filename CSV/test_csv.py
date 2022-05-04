import csv
import random

with open('test_6.csv', 'w', newline='') as csvfile:
    #pisane file
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])

    # with 30 000 rows ===>about 3 min time for process(very slow)
    for a in range(300):
        spamwriter.writerow(
            [f'{random.randint(1,200)}',
             f' {random.randint(1,100)}',
             f' 200{random.randint(0,9)}-0{random.randint(1,9)}-{random.randint(0,2)}{random.randint(1,8)}',
             f" 201{random.randint(0,9)}"
             f"-0{random.randint(1,9)}-"
             f"{random.randint(0,2)}{random.randint(1,8)}"])


# with open('test.csv', newline='') as csvfile:
#     #chetene file
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row[0])
#         print(row[1])