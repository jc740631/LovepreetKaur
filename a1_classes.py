"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
from placecollection import PlaceCollection
import csv


def welcome():
    print('Travel Tracker 1.0 - by Lindsay Ward')


def loadCSV(csvFile):
    places = []
    with open(csvFile, 'r') as rObj:
        records = csv.reader(rObj)
        for record in records:
            record[2] = int(record[2])
            places.append(record)
    return places


def show(places):
    places.sort(key=lambda x: (x[3], x[2]))
    # getting the max length of city and country
    maxCityLength = int(len(max(places, key=lambda x: len(x[0]))[0]))
    maxStateLength = int(len(max(places, key=lambda x: len(x[1]))[1]))
    nos = 0
    visited = 0
    for place in places:
        # made the length of city and state same as max lenght by adding extra space to end
        cityName = place[0] + (maxCityLength - len(place[0])) * ' '
        stateName = place[1] + (maxStateLength - len(place[1])) * ' '

        nos += 1
        if place[3] == 'n':
            print(f"*{nos}. {cityName} in {stateName} priority {place[2]:5}")
        else:
            print(f' {nos}. {cityName} in {stateName} priority {place[2]:5} ')
            visited += 1
    if visited == nos:
        print(f'{nos} places. No places left to visit. Why not add a new place?')
    else:
        print(f'{nos} places. You still want to visit {nos - visited} places.')


def Menu():
    print('Menu:')
    print('L - List places')
    print('A - Add new place')
    print('M - Mark a place as visited')
    print('Q - Quit')
    choice = input('>>> ')
    return choice.upper();


def addPlace(places):
    while True:
        city = input('Name: ')
        if city.strip() == '':
            print('Input can not be blank')
        else:
            break
    while True:
        country = input('Country: ')
        if country.strip() == '':
            print('Input can not be blank')
        else:
            break

    while True:

        try:
            priority = int(input('Priority: '))
            if priority < 0:
                print('Number must be > 0')
            else:
                break
        except ValueError:
            print('Invalid input; enter a valid number')
    return Place(city,country,priority,'n')



def markVisited(place_collection):
    print(place_collection)
    unvisited = 0
    for place in place_collection.places:
        if not place.is_visited:
            unvisited += 1
    if unvisited == 0:
        print('No unvisited places')
        return

    while True:
        try:
            print('Enter the number of a place to mark as visited')
            nos = int(input('>>> '))
            if nos < 1:
                print('Number must be > 0')
            else:
                if nos > len(place_collection.places):
                    print('Invalid place number')
                elif place_collection.places[nos - 1].is_visited:
                    print('That place is already visited')
                    break
                else:
                    place_collection.places[nos-1].is_visited = True
                    break
        except ValueError:
            print('Invalid input; enter a valid number')

def main():
    welcome()
    place_collection = PlaceCollection()
    place_collection.load_places('places.csv')
    print(f"{len(place_collection.places)} places loaded from places.csv")
    choice = Menu()
    while choice != 'Q':
        if choice == 'L':
            print(place_collection)
        elif choice == 'A':
            place = addPlace()
            place_collection.add_place(place)
            print(f"{place.name} in {place.country} (priority {place.priority}) added to Travel Tracker")
        elif choice == 'M':
            markVisited(place_collection)
        else:
            print('Invalid menu choice')
        choice = Menu()
    place_collection.save_places('places.csv')

if __name__ == "__main__":
    main()
