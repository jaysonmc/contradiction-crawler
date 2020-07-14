# from __future__ import unicode_literals, print_function
import spacy
import settings


class ProcessText():

    def tokenizeSentences(self, raw_text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(raw_text)
        sentences = [sent.string.strip() for sent in doc.sents]
        print(sentences)
