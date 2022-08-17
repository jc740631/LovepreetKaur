"""..."""

import csv

# Create your PlaceCollection class in this file
from place import Place


class PlaceCollection:
    places = []

    def load_places(self,csv_file):
        with open(csv_file, 'r') as rObj:
            records = csv.reader(rObj)
            for record in records:
                record[2] = int(record[2])
                if record[3] == 'v':
                    record[3] = True
                else:
                    record[3] = False
                self.places.append(Place(record[0], record[1], record[2], record[3]))

    def save_places(self,file_name):
        with open(file_name, 'w', newline='') as csvFile:
            cwriter = csv.writer(csvFile)
            for place in self.places:
                cwriter.writerow(str(place).split(','))

    def add_place(self, place):
        self.places.append(place)

    def get_unvisited(self):
        count = 0
        for place in self.places:
            if not place.is_visited:
                count += 1
        return count

    def sort(self, sortKey):
        if sortKey == 'Name':
            self.places.sort(key=lambda x: (x.name, x.priority))
        elif sortKey == 'Country':
            self.places.sort(key=lambda x: (x.country, x.priority))
        elif sortKey == 'Priority':
            self.places.sort(key=lambda x: (x.priority, x.priority))
        else:
            self.places.sort(key=lambda x: (x.is_visited, x.priority))

    def __str__(self):
        for place in self.places:
            print(place)
        return ''
