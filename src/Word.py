
# Obiektowa reprezentacja słówka do tlumaczenia
class Word:

    def __init__(self, word, translate, nextRepate = None):
        self.__word = word
        self.__translate = translate
        self.nextRepate = nextRepate

    def __eq__(self,other):
        if other == None or not isinstance(other, Word):
            return False;

        return self.getHashCode() == other.getHashCode()

    def getWord(self):
        return self.__word

    def getTranslate(self):
        return self.__translate

    def getHashCode(self):
        return self.__translate + self.__word