import csv


def main():
    with open('videos.csv') as video_file:
        csv_reader = csv.reader(video_file)

        next(csv_reader)  # Skips the first line

        for line in csv_reader:
            print(line)


# main()


def animals():
    headers = ['type', 'dangerous', 'age']
    animals = [['dog', False, 20], ['cat', True, 30], ['snake', True, 50]]

    with open('animals.csv', 'w', newline='') as animals_file:
        csv_writer = csv.writer(animals_file)
        csv_writer.writerow(headers)

        for animal in animals:
            csv_writer.writerow(animal)


# animals()


def csv_dict():
    with open('videos.csv', 'r') as video_file:
        csv_reader = csv.DictReader(video_file)

        for line in csv_reader:
            print(line)


csv_dict()