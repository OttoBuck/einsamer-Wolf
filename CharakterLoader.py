from Charakter import*
import json

class CharakterLoader:
    __charakter_file = "wolf.json"

    @staticmethod
    def LoadCharakter():
        try:
            file = open(CharakterLoader.__charakter_file)
            data = file.read()
            wolf_data = json.loads(data)
            return Charakter(wolf_data)
        except IOError:
            return CharakterLoader.__create_charakter_with_dialog();

    @staticmethod
    def SaveCharakter(charakter):
        charakter_json = json.dumps(charakter.__dict__, indent=4, ensure_ascii=False)
        file = open(CharakterLoader.__charakter_file, "w")
        file.write(charakter_json)
        file.close()
        pass

    @staticmethod
    def __create_charakter_with_dialog():
        # TODO: Show the attributes to the user and give possibility to re-create.
        return Charakter()

