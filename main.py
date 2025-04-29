from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

def main():
    # Chemin vers geckodriver
    gecko_path = r"driver/geckodriver.exe"
    profile_path = r"C:\Users\bpauchet\AppData\Roaming\Mozilla\Firefox\Profiles\0s0mzheo.default-esr"
    firefox_bin = r"C:\Program Files\Mozilla Firefox ESR\firefox.exe"  # <-- ajuste ce chemin !

    options = Options()
    # options.add_argument(f"-profile {profile_path}")
    options.binary_location = firefox_bin  # <-- ajoute cette ligne

    service = Service(gecko_path)

    # Initialisation de WebDriver pour Firefox
    driver = webdriver.Firefox(service=service, options=options)


    driver.get("https://odoo.st-jo.com/web#action=183&active_id=1&model=helpdesk.ticket&view_type=kanban&cids=1&menu_id=131")
    driver.execute_script("window.open('https://google.com', '_blank');")
    driver.maximize_window()
    driver.fullscreen_window()

    while True:
        tab_count = len(driver.window_handles)

        for i in range(tab_count):
            # Basculer vers l'onglet
            driver.switch_to.window(driver.window_handles[i])

            # Attendre 1 minute avant de passer à l'onglet suivant
            time.sleep(15)

if __name__ == '__main__':
    main()
