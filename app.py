import codecs
import json

from io import StringIO

notebook_file = codecs.open("data/simple-notebook.ipynb", 'r')

# source loads in json/dict format
source = json.loads(notebook_file.read())

cells = source["cells"]

first_cell = next(iter(cells))


def writeToBuffer(cells):
    buffer = StringIO()

    for cell in cells:
        for line in cell["source"]:
            buffer.write(line)
        buffer.write("\n")

    return buffer.getvalue()


def writeToFile(cells):
    python_script = open('data/simple-notebook.py', 'w')

    for cell in cells:
        for line in cell["source"]:
            python_script.write(line)
        python_script.write("\n")


writeToBuffer(cells)
writeToFile(cells)
