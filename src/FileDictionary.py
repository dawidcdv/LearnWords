import csv
from src.Word import Word

# Klasa pozwala na załadowanie  słówek z pliku
class FileDictionary:


    #Funckja wczytujaca słowka z pliku csv
    #Funckja pozwala na pominiecie słowek, ktore nas nie interesuja
    #poprzez przekazanie funckji , ktora jak argument przyjume Word
    # a zwraca True/ False w zaleznosci od tego czy słowo ma byc wczytyane czy nie
    def load(self, fileName, predicate = None):
        if fileName == "":
            return

        wordsToLearn = []

        with open(fileName, newline='') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=';', quotechar='\\')
            for row in csvReader:
                if len(row) < 2:
                    continue
                word = Word(row[0], row[1])
                if predicate == None or predicate(word):
                    wordsToLearn.append(word)

        return wordsToLearn

    #Funckja sprawdza czy podane tłumaczenie dla danego słowajest poprawne
    def isAnswerCorrect(self, word : Word, answer):
        return word.getTranslate() == answer