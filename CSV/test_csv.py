import csv
with open('test.csv', 'w', newline='') as csvfile:
    #pisane file
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['den','islav'])


with open('test.csv', newline='') as csvfile:
    #chetene file
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0])
        print(row[1])