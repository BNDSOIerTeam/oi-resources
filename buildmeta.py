# Scan to build pages.json
import pathlib

from markdown import markdown


for dir in pathlib.Path('.').glob('**'):
    result = []
    for file in dir.glob('*.md'):
        print(markdown(file.read_text(), extensions = ['meta']))