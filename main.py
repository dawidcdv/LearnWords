from src.FileLogger import FileLogger
from src.FileDictionary import FileDictionary
from src.helper.FileHelper import FileHelper
from src.gui.GuiController import GuiController
from src.Config import Config

# Tworzy folder var jesli nie istnieje
FileHelper.createVarDir()

CONFIG_PATH = FileHelper.getVarFilePath('config.ini')
LOG_PATH = FileHelper.getVarFilePath('log.csv')

#Uruchamiam aplikacje
GuiController(Config(CONFIG_PATH), FileDictionary(), FileLogger(LOG_PATH)).run()


