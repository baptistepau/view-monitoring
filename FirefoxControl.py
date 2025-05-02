import threading as th
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from lib.travailJSON import *

class FirefoxControl:
    def __init__(self, configFile:str):
        # Var
        self.__daemonBoucle = 1

        # Instance de la classe jsonWork
        confFile = jsonWork(configFile)

        # Chemin vers geckoself.__driver
        gecko_path = confFile.lectureJSON("emplacmentDriver")
        profile_path = confFile.lectureJSON("emplacementProfile")
        firefox_bin = confFile.lectureJSON("emplacementFirefox")

        # Recuperation de la liste d'URL
        self.__listeURL = confFile.lectureJSONList("listeURL")

        # Recuperation temps de defilement
        self.__tempsDefilement = int(confFile.lectureJSON("time"))
        if self.__tempsDefilement == 0:
            self.__tempsDefilement = 15

        # Mise en place des option
        options = Options()
        options.add_argument(f"-profile {profile_path}")
        options.binary_location = firefox_bin

        # Demarage de geckodriver
        service = Service(gecko_path)

        # Initialisation de Webdriver pour Firefox
        self.__driver = webdriver.Firefox(service=service, options=options)

        # Creation du theard pour la boucle
        self.__thBoucle = th.Thread(target=self.__boucle, daemon=True)
        
    def start(self):
        i = 0
        for url in self.__listeURL:
            if i == 0:
                self.__driver.get(url)
            else :
                self.__driver.execute_script(f"window.open('{url}', '_blank');")
            i += 1

        self.__driver.maximize_window()
        self.__driver.fullscreen_window()
        self.__thBoucle.start()
        input("Appuyez sur ENTREE pour fermer le programme")
        self.__daemonBoucle = 0
        self.__thBoucle.join()
        self.__driver.quit()

    def __boucle(self):
        while self.__daemonBoucle == 1:
            tab_count = len(self.__driver.window_handles)
            for i in range(tab_count):
                try :
                    self.__driver.switch_to.window(self.__driver.window_handles[i])
                    self.__driver.refresh()
                except:
                    print("Erreur de rafraichissement de l'onglet numero : ", i)

                time.sleep(15)