# from __future__ import unicode_literals, print_function
import spacy
import en_core_web_sm
import settings
from pathlib import Path
import os


class ProcessText():

    def __init__(self):
        self.processText()
        
    def __removeWhitespace(self, line):
            if line.strip():
                line = line.strip()
                return line + os.linesep
            else:
                return ""

    def isMeaningful(self, token, length):

        isMeaningfulSentence = True

        if (length <= 6 and (token.pos_ == "ADJ" or token.pos_ == "ADP" or token.pos_ == "PROPN" or token.pos_ == "NUM" or token.pos_ == "ADV")):
            isMeaningfulSentence = False
            print("token: " + token.text)
            print("\t Type: " +token.pos_)
        elif (length == 1):
            print("token: " + token.text)
            print("\t Type: " +token.pos_)
            isMeaningfulSentence = False
        else:
            print("token: " + token.text)
            print("\t Type: " +token.pos_)

        return isMeaningfulSentence

    def __removeMeaninglessSentences_helper(self, line):
        nlp = en_core_web_sm.load()
        doc = nlp(line)
        isMeaningfulSentence = None

        lines = [[] for token in doc]

        for token in doc:
            if (self.isMeaningful(token, len(lines))):
                isMeaningfulSentence = True
            else:
                isMeaningfulSentence = False

        if (isMeaningfulSentence):
            print("Meaningful: " + line)
            return line + os.linesep
        else:
            print("NOT Meaningful: " + line)
            return ""

    def tokenizeSentences(self, raw_text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(raw_text)
        sentences = [sent.string.strip() for sent in doc.sents]
        return sentences

    def processText(self):
        pathlist = Path(settings.OUTPUT_FOLDER).rglob('*.html')
        for path in pathlist:
            output_contents = open(path, "r").read()
            print("Cleaning white space from " + path.name)
            output_contents = self.cleanWhitespace(output_contents)
            print("Removing non-meaningful sentences " + path.name)
            output_contents = self.removeMeaninglessSentences(output_contents)
            open(settings.PROCESSED_FOLDER + '/' +
                 path.name, "w+").write('\n'.join(self.tokenizeSentences(output_contents)))

    def cleanWhitespace(self, output_contents):
        new_output_lines = ""
        for line in iter(output_contents.splitlines()):
            new_output_lines += self.__removeWhitespace(line)
        return new_output_lines

    def removeMeaninglessSentences(self, output_contents):
        new_output_lines = ""
        for line in iter(output_contents.splitlines()): 
            new_output_lines += self.__removeMeaninglessSentences_helper(line)
        return new_output_lines