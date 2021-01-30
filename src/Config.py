import configparser

#Klasa ktora odczytuje / zapisuje ustawienia konfiguracyjne
class Config:


    class Sections:
        class Dictionary:
            SECTION_NAME = "dictionary"
            PATH = "path"

    def __init__(self, path):
        self.__path = path
        self.config = configparser.ConfigParser()
        self.config.read(path)


    # Funckaj pobierajaca domyslna sciezke ostatnio wybranego słownika z pliku konfiguracyjnego
    def getDefaultDictionaryPath(self):
        dictionary = Config.Sections.Dictionary
        return self.getConfig(dictionary.SECTION_NAME,dictionary.PATH)

    # Funckja zapisuje sciezke w pliku konfiguracyjnym
    def saveDefaultDictionaryPath(self,path):
        dictionary = Config.Sections.Dictionary
        self.__writeOption(dictionary.SECTION_NAME,dictionary.PATH, path)

    def getConfig(self, section, key):
        if section in self.config:
            if key in self.config[section]:
                return self.config.get(section, key)
        return ""

    def __writeOption(self,section, key, value):
        if section not in self.config:
            self.config.add_section(section)
        self.config[section][key] = value
        f = open(self.__path, 'w+')
        self.config.write(f)

