# from __future__ import unicode_literals, print_function
import spacy
import settings
from pathlib import Path


class ProcessText():

    def __init__(self):
        pathlist = Path(settings.OUTPUT_FOLDER).rglob('*.html')
        for path in pathlist:
            output_contents = open(path, "r").read()
            open(settings.PROCESSED_FOLDER + '/' +
                 path.name, "w+").write('\n'.join(self.tokenizeSentences(output_contents)))

    def tokenizeSentences(self, raw_text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(raw_text)
        sentences = [sent.string.strip() for sent in doc.sents]
        return sentences
