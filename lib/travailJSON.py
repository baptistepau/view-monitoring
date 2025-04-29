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

    def lectureJSONList(self, flag):
        """
         Lire un flag qui contient une liste
        :param flag: Flag ou se trouve la liste que vous voulez lire
        :return: retourne La liste
        """
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            liste = json.load(openfile)[flag]
        return list(liste)