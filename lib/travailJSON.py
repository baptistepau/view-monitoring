import json


class jsonWork:
    def __init__(self, file):
        self.fichier = file

    def lectureJSON(self, flag):
        """
        Lire un flag du fichier json
        :param flag: Flag qui contient la valeur que vous voulez lire
        :return: Contenu du flag
        """
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag]
        return str(dict)