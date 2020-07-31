class StringMap:

    sentence = ""
    fileName = ""

    def __init__(self, sentence, fileName):
        self.sentence = sentence
        self.fileName = fileName

    def __str__(self):
        return str(self.fileName) + ": " + str(self.sentence)
