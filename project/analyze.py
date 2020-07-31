import settings
from pathlib import Path
from contradiction import exec
from StringMapModel import StringMap

class Analyze:

    stringMapArr = []

    def __init__(self):
        self.analyze()
        self.stringMapArr = []

    def analyze(self):
        print("Analzying")
        pathlist = Path(settings.PROCESSED_FOLDER).rglob('*.html')
        for path in pathlist:
            output_lines = open(path, "r").readlines() 
            self.buildStringMapArr(output_lines, path)
        
        self.searchStringMapArrForContradictions()

    def buildStringMapArr(self, output_lines, path):
        for sentence in output_lines: 
            self.stringMapArr.append(StringMap(sentence, path))

    def searchStringMapArrForContradictions(self):
        for stringMap in self.stringMapArr:
            self.scanForContradictions(stringMap)

    def scanForContradictions(self, firstStringMap):
        for secondStringMap in self.stringMapArr: 
            if (firstStringMap.sentence != secondStringMap.sentence):
                print("Comparing " + str(firstStringMap))
                print("with " + str(secondStringMap))
                exec(firstStringMap.sentence, secondStringMap.sentence)
            
