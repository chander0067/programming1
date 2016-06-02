                                                                                                    
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

__author__ = 'Chanderdeep'

class ItemHireApp(App):
    status_text = StringProperty()

    def __init__(self):
        super(ItemHireApp, self).__init__()
        self.dicDescription ={}
        self.dicCost = {}
        self.dicAvailablity ={}

    def build(self):
        self.title = "ITEM HIRE APP"
        self.root= Builder.load_file('ItemHire.kv')
        self.file_reader()
        self.create_entry_bottons()
        return self.root

       

    def add_Item(self, added_name, added_desc, added_number):
        f = open("Items.csv", 'w')
        new = added_name+","+added_desc+","+str(added_number)+","+"in\n"
        f.write(new)
        f.close()

    def file_reader(self):
        f= open("items.csv",'r')
        movie= f.readlines()
        n=0


        for i in movie:
            self.movieName = i.strip().split(',')[0]
            self.description = i.strip().split(',')[1]
            self.dicDescription [self.movieName] = self.description
            self.cost = float(i.strip().split(',')[2])
            self.dicCost [self.movieName]= self.cost
            self.availablity = i.strip().split(',')[-1]


            if self.availablity== "out":
                self.dicAvailablity [self.movieName] = "*"

            else:
                self.dicAvailablity[self.movieName] = ""



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
        self.dicAvailablity[name] = "*"
        self.file_updater()        
    
            
            

    def press_entry(self, instance):
        name = instance.text
        self.status_text = "Movie: "+ name + "\nDescription: " + self.dicDescription[name] + "\nCost:" + str(self.dicCost[name])


    def create_entry_bottons(self):
        
        for name in self.dicDescription:

            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

            
    def press_add(self):

        self.status_text = "Enter details for new items"

        self.root.ids.popup.open()
        

    def press_save(self, added_name, added_desc, added_number):

        self.dicCost[added_name] = added_number
        self.dicDescription[added_name] = added_desc
        
        self.root.ids.entriesBox.cols = len(self.dicCost) // 5 + 1
        #  buttons for new entry 
        temp_button = Button(text=added_name)
        temp_button.background_color = (1, 2, 0, 1)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)

        self.root.ids.popup.dismiss()
        self.add_Item(added_name, added_desc, added_number)
        self.clear_fields()    
    

    def file_updater(self):
        f = open('Items.csv','w')
        for name in self.dicDescription:
            new = name +","+self.dicDescription[name]+","+str(self.dicCost[name])+","+self.dicAvailablity[name]+'\n'
            f.write(new)

        f.close()
        

    def clear_fields(self):

        self.root.ids.addedName.text = ""
        self.root.ids.addedNumber.text = ""

    def press_cancel(self):

        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""

    def exit(self):
        exit()




ItemHireApp().run()





