# from __future__ import unicode_literals, print_function
import spacy
import settings
from pathlib import Path
import os


class ProcessText():

    def __init__(self):
        self.processText()

    def tokenizeSentences(self, raw_text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(raw_text)
        sentences = [sent.string.strip() for sent in doc.sents]
        return sentences

    def processText(self):
        pathlist = Path(settings.OUTPUT_FOLDER).rglob('*.html')
        for path in pathlist:
            output_contents = open(path, "r").read()
            output_contents = self.cleanText(output_contents)
            open(settings.PROCESSED_FOLDER + '/' +
                 path.name, "w+").write('\n'.join(self.tokenizeSentences(output_contents)))

    def cleanText(self, output_contents):
        new_output_lines = ""
        for line in iter(output_contents.splitlines()): 
            if line.strip():
                line = line.strip()
                new_output_lines += line + os.linesep
        return new_output_lines

