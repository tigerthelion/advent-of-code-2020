import csv
def load_data(file_name):
    data = []
    with open(file_name) as datfile:
        reader = csv.reader(datfile)
        for row in reader:
            data.append(int(row[0]))
    return data        