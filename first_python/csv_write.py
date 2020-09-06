import csv

f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "김초롱", True])
wr.writerow([2, "김누구", False])
f.close()