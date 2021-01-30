from tkinter import Button, messagebox, Entry, Label, Menu, StringVar, Frame, N, W ,S ,E
from abc import ABCMeta, abstractmethod

# Klasa odpowiedzialna za powstawanie widoku / interfejsu graficznego
# W tej klasie znajduje sie wszystkie instrukjce dotyczace rysowania elemntow graficznych
# Klasa do porawnego dzialania potrzebuje Kontrolera, ktory implementuje metody answer, chooseFile
class View:

    class Controller:
        __metaclass__ = ABCMeta
        @abstractmethod
        def answer(self, position : int): raise NotImplementedError
        def chooseFile(self): raise NotImplementedError


    def __init__(self, tk, controller: Controller):
        self.__root = tk
        self.__controller = controller
        self.feedback = StringVar()
        self.wordToTranslate = StringVar()
        self.answer = StringVar()

    #Funkcja odpowiedzialna za tworzenie elementow graficznych
    def redner(self):
        mainframe = Frame(self.__root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)

        Label(mainframe, text="Wyraz: ").grid(column=1, row=1, sticky=W)
        Label(mainframe, textvariable=self.wordToTranslate).grid(column=2, row=1, sticky=(W, E))
        Label(mainframe, text="Tłumaczenie:").grid(column=1, row=2, sticky=E)
        Entry(mainframe, width=50, textvariable=self.answer).grid(column=2, row=2, sticky=(W, E))

        Label(mainframe, textvariable=self.feedback).grid(column=2, row=3)
        Button(mainframe, text=" Dalej! ", command= lambda answer = self.answer : self.__controller.checkAnswer(self.answer.get()))\
            .grid(column=3, row=3, sticky=W)


        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.__createMenu()

    # Funckja tworzaca menu aplikacja, umuzliwiajac wybor pliku
    def __createMenu(self):
        m = Menu(self.__root)
        m.add_command(label="Wybierz plik", command= lambda: self.__controller.chooseFile())
        self.__root['menu'] = m

    #FUnckja pozwalajaca na wyswietlenie informacji
    def showInfo(self,info):
        messagebox.showerror(title="Info", message=info)

    def setWordsToTranslate(self, word):
        self.wordToTranslate.set(word.getWord())