# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from dataclasses import dataclass
from flask import Flask, request, render_template

app = Flask(__name__)

SectionDNE = "Invalid: Section does not exist"

@dataclass
class Inventory:
    storage: dict

    @app.route("/<print>")
    def printAllItems(self):
        for key, value in self.storage.items():
            print("Section: {}".format(key))
            for key, value in self.storage[key].items():
                value.print()
            print("")

    def printSection(self, section):
        print("Section: {}".format(section))
        if section in self.storage:
            for key, value in self.storage[section].items():
                value.print()
        else:
            return SectionDNE

    def removeSection(self, section):
        if str(section) in self.storage:
            del self.storage[section]
            return ""
        else:
            return SectionDNE

    def addSection(self, section):
        if not str(section) in self.storage:
            self.storage[section] = dict()
            return ""
        else:
            return "Invalid: Section already exists"

    def addItemToSection(self, section_name, item):
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
    name: str
    price: int
    quantity: int

    def print(self):
        print("Item Name: {}".format(self.name))
        print("Item Price: {}".format(self.price))
        print("Item Quantity: {}".format(self.quantity))


@app.route("/", methods=['GET', 'POST'])
def index():
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

    #app.run(host="127.0.0.1", port=8080, debug=True)
