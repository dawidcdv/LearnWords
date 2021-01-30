import csv
from src.Word import Word
from src.helper.FileHelper import FileHelper


# Klasa pozwala na pobieranie oraz zapisywanie slow do powtorki
class FileLogger():

    def __init__(self, path):
        self.fileLog = path
        self.__words = []
        self.__load()

    # Funckja pozwala na pobranie słowek według jakis kryteriow
    # poprzez przekazanie funckji  ktora jako argument
    # bedzie przyjmowac obiekt klasy Word  a zwraca True/ False
    # w zaleznosci od tego czy słowo ma byc wczytyane czy nie
    def getWords(self, predicate = None):
        if predicate is None:
            return self.__words

        return list(filter(predicate, self.__words))

    #Funckja przy dodanwaniu słwoka usuwa wczesniej to słowo
    # w celu zapewnienia unikalnosci dla danego słowa
    def add(self, word : Word):
        self.__excludeWord(word)
        self.__words.append(word)
        self.__saveWords(self.__words)

    #Funckja usuwa słowo z pliku
    def delete(self, word: Word):
        self.__excludeWord(word)
        self.__saveWords(self.__words)


    # Funckja sprawdza czy slowko jest w slowach do powtorki
    def isLogged(self, searchWord: Word):
        print(self.__words)
        for word in  self.__words:
            if searchWord == word:
                return True
        return False



    # Funckja laduje do pamieci slowka do powtorki na dzisiaj oraz na pozostale dni
    def __load(self):
        self.__words = []
        if not FileHelper.fileExist(self.fileLog):
            return

        with open(self.fileLog, newline='') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=';', quotechar='\\')
            for row in csvReader:
                if len(row) < 3:
                    continue

                word = self.__createWordFromRow(row)
                self.__words.append(word)


    #Funckja usuwa jakies slowko z naszej listy
    def __excludeWord(self, word):
        excludeThisWord = lambda currentWord, wordToSearch=word: \
            currentWord != wordToSearch
        self.__words = self.getWords(excludeThisWord)


    # Funckja zapisuje liste  słow w  pliku
    def __saveWords(self, words, mode = "w"):
        with open(self.fileLog, mode) as fd:
            text = ""
            for word in words:
                text = text + word.getWord() + ";" + word.getTranslate() + ";" + word.nextRepate + "\n"
            fd.write(text)



    # Funckja tworzy obiektowa reprezentacje słowka (wyraz, jego tlumaczenie i date powtorki)
    def __createWordFromRow(self, row):
        return Word(row[0], row[1], row[2])
