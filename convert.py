import csv

with open('./route/to/path.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    f= open("filename.txt","w+")
    for row in reader:
        question = str(row[0])
        answer = str(row[1])

        f.write("{}\n".format(question))
        f.write("{}\n".format(answer))

    f.close()
csvFile.close()
