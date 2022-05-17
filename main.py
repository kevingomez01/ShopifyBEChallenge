# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
