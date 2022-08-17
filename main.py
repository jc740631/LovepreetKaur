"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.core.window import Window

from kivy.lang import Builder
from kivy.uix.button import Button

from placecollection import PlaceCollection
from place import Place
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

class TravelTrackerApp(App):
    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        self.placecollection = PlaceCollection()
        self.title = 'Travel Tracker'
        self.root = Builder.load_file('app.kv')
        self.placecollection.load_places('places.csv')
        self.root.ids.unvisited_label.text = 'Places to visit: ' + str(self.placecollection.get_unvisited())
        self.show_places()
        return self.root

    def sortby(self,key):
        self.placecollection.sort(key)
        self.show_places()

    def show_places(self):
        self.root.ids.grid.clear_widgets()
        count = 0
        for place in self.placecollection.places:
            if place.is_visited:
                button = Button(text=str(place), size_hint=(1.0, None), size=(50, 75), background_color=(0, 1, 0, 1))

            else:
                button = Button(text=str(place), size_hint=(1.0, None), size=(50, 75), background_color=(1, 0, 0, 1))

            button.id = count
            button.bind(on_press=self.change_status)
            self.root.ids.grid.add_widget(button)
            count += 1
        self.root.ids.unvisited_label.text = 'Places to visit: ' + str(self.placecollection.get_unvisited())

    def change_status(self,placeId):

        if self.placecollection.places[placeId.id].is_visited:
            self.placecollection.places[placeId.id].mark_unvisited()
            self.root.ids.statusLabel.text = f'You visited {self.placecollection.places[placeId.id].name} Great travelling!'
        else:
            self.placecollection.places[placeId.id].mark_visited()
            self.root.ids.statusLabel.text = f'You need to visit {self.placecollection.places[placeId.id].name} Get going!'
        self.show_places()
    def add_newplace(self):
        if self.root.ids.nameInput.text == '':
            self.root.ids.statusLabel.text = 'All fields must be completed'
        elif self.root.ids.country.text == '':
            self.root.ids.statusLabel.text == 'All fields must be completed'
        elif self.root.ids.priorityInput.text == '':
            self.root.ids.statusLabel.text = 'All fields must be completed'
        else:
            try:
                priority = int(self.root.ids.priorityInput.text)
                if priority < 1:
                    self.root.ids.statusLabel.text = 'Priority must be > 0'
                else:
                    name = self.root.ids.nameInput.text
                    country = self.root.ids.country.text
                    place = Place(name, country, priority, False)
                    self.placecollection.add_place(place)
                    self.show_places()
                    self.clear_all()

            except ValueError:
                self.root.ids.statusLabel.text = 'Please enter a valid number'

    def clear_all(self):
        self.root.ids.nameInput.text = ''
        self.root.ids.country.text = ''
        self.root.ids.priorityInput.text = ''

    def on_request_close(self, *args):
        self.placecollection.save_places('places2.csv')
        App.get_running_app().stop()


if __name__ == '__main__':
    TravelTrackerApp().run()
