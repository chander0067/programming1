
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

__author__ = 'Chanderdeep'

class ItemHireApp(App):
    status_text = StringProperty()

    def __init__(self):
        super(ItemHireApp, self).__init__()
        self.dicDiscription ={}
        self.dicCost = {}
        self.dicAvailablity ={}

    def build(self):
        self.title = "ITEM HIRE APP"
        self.root= Builder.load_file('ItemHire.kv')
        self.file_reader()
        self.create_entry_bottons()
        return self.root

    def file_reader(self):
        f= open("items.csv",'r')
        movie= f.readlines()
        n=0


        for i in movie:
            self.movieName = i.strip().split(',')[0]
            self.discription = i.strip().split(',')[1]
            self.dicDiscription [self.movieName] = self.discription
            self.cost = float(i.strip().split(',')[2])
            self.dicCost [self.movieName]= self.cost
            self.availablity = i.strip().split(',')[-1]


            if self.availablity== "out":
                self.dicAvailablity [self.movieName] = "*"

            else:
                self.dicAvailablity[self.movieName] = ""

    

    def add_Item(self, added_name, added_desc, added_number):
        f = open("Items.csv", 'a')
        new = added_name+","+added_desc+","+str(added_number)+","+"in\n"
        f.write(new)
        f.close()


    def return_item(self):
        for name in self.dicAvailablity:
            if self.dicAvailablity[name] == "*":

                temp_button = Button(text=name)
                temp_button.bind(on_release=self.press_entry_return)
                self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry_return(self, instance):
        name= instance.text
        instance.background_color = (1, 1, 0, 1)
        self.dicAvailablity[name] = ""
        self.file_updater()



    def hire_item(self):
        for name in self.dicAvailablity:
            if self.dicAvailablity[name] == "":

                temp_button = Button(text=name)
                temp_button.bind(on_release=self.press_entry_hire)
                self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry_hire(self, instance):
        name= instance.text
        instance.background_color = (1, 1, 0, 1)
        self.dicAvailablity[name] = ""
        self.file_updater()        
        
