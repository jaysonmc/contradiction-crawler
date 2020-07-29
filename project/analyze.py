import settings
from pathlib import Path
from contradiction import exec

class Analyze:

    def __init__(self):
        self.analyze()

    def analyze(self):
        print("Analzying")
        pathlist = Path(settings.PROCESSED_FOLDER).rglob('*.html')
        for path in pathlist:
            print(path)
            output_lines = open(path, "r").readlines() 
            self.scanFile(output_lines)

    def scanFile(self, output_lines):
        for firstSentence in output_lines: 
            self.searchContradictions(firstSentence, output_lines)

    def searchContradictions(self, firstSentence, output_lines):
        for secondSentence in output_lines: 
            print(firstSentence)
            print(secondSentence)
            exec(firstSentence, secondSentence)
            

            
