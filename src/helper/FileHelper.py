import os

#Helper to latwiejszegod dostepu do plikow
class FileHelper:

    VAR_DIR = os.path.abspath("var")


    @staticmethod
    def createVarDir():
        if not os.path.exists("var"):
            os.makedirs("var")

    @staticmethod
    def getVarFilePath(filename) -> str:
        return  os.path.join(FileHelper.VAR_DIR,filename)


    @staticmethod
    def fileExist(path):
        return os.path.isfile(path)

