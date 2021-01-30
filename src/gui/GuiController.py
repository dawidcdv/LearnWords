import datetime
import tkinter as tk
from tkinter.filedialog import askopenfilename
from src.gui.View import View

#Kontroler GUI
class GuiController(View.Controller):

    APP_NAME = "Learn words"

    def __init__(self,config,dictionary, logger, root = tk.Tk() ):
        self.__root =  root
        self.__config = config
        self.__logger = logger
        self.__dictionary=dictionary
        self.__word = None
        self.__iterWords = None

    # Funkcja uruchamiajaca aplikacje
    # Funckja z configu pobiera ostatnio wybrany plik ze slowkami
    # w przypadku braku takiego pliku aplikacja prosi o wybranie pliku
    # A nastepnie inicializuje slowka
    # W pierwszej kolejnosci sa slowka przeznaczone do powtorki nastepnie do nauki
    def run(self):
        self.__root.title(self.APP_NAME)
        self.__view=View(self.__root, self)
        self.__view.redner()
        if self.__config.getDefaultDictionaryPath() != "":
            self.__initWords()
        else:
            self.chooseFile()

        self.__root.mainloop()



    # Funckja pozwala na wybor pliku ze slowkami
    # Funckja rowniez zapisuje wskazany plik w configu jako domyslny
    # Dzieki temuw  przyszlych uruchmieniach programu uzytkownik nie musi podawac za kazdym razem pliku
    def chooseFile(self):
        path = askopenfilename()
        self.__root.update()
        self.__dictionary.load(path)
        self.__config.saveDefaultDictionaryPath(path)
        self.__initWords()


    # Funckja sprawdza poprawnosc odpowiedzi oraz przez wywolanie powyzszej funckji(nextWord)
    # ustawia nastepne slowko do przetlumaczenia
    def checkAnswer(self, answer):
        if(self.__word == None or answer == ""):
            return

        if  self.__dictionary.isAnswerCorrect(self.__word, answer):
            self.__view.feedback.set("OK")
            data = datetime.datetime.now() + datetime.timedelta(days=7)
        else:
            data = datetime.datetime.now()
            self.__view.feedback.set("ŹLE")

        self.__view.answer.set("")
        self.__word.nextRepate = data.date().__str__()
        self.__logger.add(self.__word)
        self.__askForNextWord()


    # Funckja wywolywana po wyborze pliku, lub uruchomieniu programu
    # W pierwszej kolejnosci odpytywane sa slowka do powtorki
    def __initWords(self):
        self.__clear()
        wordsToRepate = self.__getWordsToRepate()
        newWords =  self.__getWordsToLearn()
        self.__iterWords = iter(wordsToRepate + newWords)
        self.__askForNextWord()


    #Pobierane sa slowka do nauki wedlug konkretnej strategii
    #W tym przypadku wykluczam słowka, ktore sa zalogowane
    def __getWordsToLearn(self):
        notLoggedWords = lambda currentWord, logger =self.__logger :\
             not logger.isLogged(currentWord)
        return self.__dictionary.load(self.__config.getDefaultDictionaryPath(), notLoggedWords)

    # Funckja pobiera słowka  z logu wedlug konkretnej strategii
    # W tym przypadku jesli słowko było przeznaczona do powtorki
    # na dzien dzisiejszy lub wczensiejszy
    def __getWordsToRepate(self):
        toRepateToday = lambda currentWord, today = datetime.date.today(): \
            datetime.date.fromisoformat(currentWord.nextRepate) <= today
        return  self.__logger.getWords(toRepateToday)



    # Funckja, ktora pobiera nastepne slowko z iteratora
    # W przypadku braku dalszych slowek wyswielta komunikat o braku słowek
    def __askForNextWord(self):
        try:
            self.__word = next(self.__iterWords)
            self.__view.wordToTranslate.set(self.__word.getWord())
        except StopIteration:
            self.__view.showInfo("Koniec slowek")

    # Funckja, ktora resetuje zmiany wprowadzone wczesniej
    # Glownie wykorzystywana w przypadku ponownej inicjalizacji pliku
    def __clear(self):
        self.__word =None
        self.__view.wordToTranslate.set("")
        self.__view.feedback.set("")


