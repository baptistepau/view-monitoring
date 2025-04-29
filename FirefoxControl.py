import threading as th
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

class FirefoxControl:
    def __init__(self, configFile:str):
        # Var
        self.__daemonBoucle = 1
        # Chemin vers geckoself.__driver
        gecko_path = r"driver/geckodriver.exe"
        profile_path = r"C:\Users\bpauchet\AppData\Roaming\Mozilla\Firefox\Profiles\0s0mzheo.default-esr"
        firefox_bin = r"C:\Program Files\Mozilla Firefox ESR\firefox.exe"  # <-- ajuste ce chemin !

        options = Options()
        options.add_argument(f"-profile {profile_path}")
        options.binary_location = firefox_bin

        service = Service(gecko_path)

        # Initialisation de Webdriver pour Firefox
        self.__driver = webdriver.Firefox(service=service, options=options)
        self.__thBoucle = th.Thread(target=self.__boucle, daemon=True)
        
    def start(self):
        self.__driver.get("https://odoo.st-jo.com/web#action=183&active_id=1&model=helpdesk.ticket&view_type=kanban&cids=1&menu_id=131")
        self.__driver.execute_script("window.open('https://google.com', '_blank');")
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
                self.__driver.switch_to.window(self.__driver.window_handles[i])
                time.sleep(15)