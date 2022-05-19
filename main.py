"""
Author: Kevin Gomez

Description: This project was made to complete the shopify Developer Intern Challenge Question.
I first want to state that I was not able to finish this challenge but nonetheless I wanted to showcase my
thought process and implementation. I was unable to finish the web application portion alongside the additional feature.
I designed my project around dictionary as they have quick access time, but I do understand
as the data gets larger the access time may decrease due to possible collisions based upon has the hash function.
Another approach would've been to set up a database and properly useSQL to get and retrieve relevant data.
I wanted to test out and try flask for the first time to build a stable web application that can perform the basic
functionalities that I was looking for. Although, I wasn't able to finish the project I still learned a lot from this
experience, it was a lot of fun!

Last Revision: May 18th, 2022
"""
from dataclasses import dataclass
from flask import Flask, request, render_template

app = Flask(__name__)

SectionDNE = "Invalid: Section does not exist"


@dataclass
class Inventory:
    """
    This class represents the massive dictionary functionality I was looking for.
    Keys are set up as other dictionaries known in this code as section types.
    Sections were different categories that items could fall under. This functionality could
    be useful in the future if we're looking for specific items in certain sections.
    """
    storage: dict

    @app.route("/<print>")
    def printAllItems(self):
        """
        This function prints out all the sections and relevant items within those sections out.

        :return: None
        """
        for key, value in self.storage.items():
            print("Section: {}".format(key))
            for key, value in self.storage[key].items():
                value.print()
            print("")

    def printSection(self, section):
        """
        Print out all items existing within a section dictionary.

        :param section: Section name
        :return: None or Error Message
        """
        print("Section: {}".format(section))
        if section in self.storage:
            for key, value in self.storage[section].items():
                value.print()
        else:
            return SectionDNE

    def removeSection(self, section):
        """
        Remove a section specific to what the user wants.

        :param section: Section name
        :return: None or Error Message
        """
        if str(section) in self.storage:
            del self.storage[section]
            return ""
        else:
            return SectionDNE

    def addSection(self, section):
        """
        Add a section specific to what the user wants.

        :param section: Section name
        :return: String
        """
        if not str(section) in self.storage:
            self.storage[section] = dict()
            return ""
        else:
            return "Invalid: Section already exists"

    def addItemToSection(self, section_name, item):
        """
        Add a specific item to a specific section.

        :param section_name: Section name
        :param item: Item being added
        :return: None or Error Message
        """
        # validate section exists
        if section_name in self.storage:
            # validate item exists
            if item.name in self.storage[section_name]:
                self.storage[section_name][item.name].quantity += item.quantity
                # validate if price is the same as on record, if different -> update price
                if item.price != self.storage[section_name][item.name].price:
                    self.storage[section_name][item.name].price = item.price
            else:  # add item if it does not exist
                self.storage[section_name][item.name] = item
        else:
            return SectionDNE

    def removeItemFromSection(self, section_name, item):
        """
        Remove a specific item from a specific section.

        :param section_name: Section name
        :param item: Item being removed
        :return: None or Error Message
        """
        # validate section exists
        if section_name in self.storage:
            # validate item exists
            if item.name in self.storage[section_name]:
                del self.storage[section_name][item.name]
            else:
                return "Invalid: Item does not exist"
        else:
            return SectionDNE


@dataclass
class InventoryItem:
    """
    This class represents items that will be added to the inventory. I wanted to create the inventory item aspect of
    this project as a dataclass because I thought it be easiest to expand this and add relevant functions. Thus,
    increasing the future functionality of this project.
    """
    name: str
    price: int
    quantity: int

    def print(self):
        """
        Prints relevant data fields of this class.
        :return: None
        """
        print("Item Name: {}".format(self.name))
        print("Item Price: {}".format(self.price))
        print("Item Quantity: {}".format(self.quantity))


@app.route("/", methods=['GET', 'POST'])
def index():
    """
    This was the first step in creating the web application. Properly setting up adding and removing sections from
    the data.
    :return: a rendered version of the html file on the local machine.
    """
    if request.method == 'POST':
        if "add" in request.form:
            storage_type = request.args.get("storage_type", "")
            var = inventory.addSection(storage_type)
            print(var)
        elif "remove" in request.form:
            remove_type = request.args.get("remove_type", "")
            var = inventory.removeSection(remove_type)
            print(var)
    elif request.method == 'GET':
        print("hello")
    return render_template("home.html")


if __name__ == '__main__':
    # Inventory -> Massive Dictionary -> holding all different inventory item types
    global inventory
    inventory = Inventory(dict())
    # Inventory Types

    # app.run(host="127.0.0.1", port=8080, debug=True)
