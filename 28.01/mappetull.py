from pathlib import Path
from os import getcwd, path, remove


class TextFile:
    def __init__(self, name, fpath) -> None:
        self.__name = name
        self.__filepath = path.abspath(fpath)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def filepath(self):
        return self.__filepath
    
    @filepath.setter
    def filepath(self, value):
        self.__filepath = value
        

    def move(self, new_path):
        Path(self.__filepath).rename(new_path)
        self.__filepath = new_path

    def delete(self):
        remove(self.__filepath.join(self.__name))

    def load(self):
        with open(self.__filepath.join(self.__name), 'r+', encoding = 'utf-8', newline = "\n")as f:
            self.doc = f.readlines().rstrip('\n')
    
    def save(self):
        with open(self.__filepath.join(self.__name), "w", encoding = 'utf-8', newline = "\n") as file:
            file.writelines(self.doc)

print(getcwd())
print(path.abspath("/28.01"))
file = TextFile('ducoment.txt', '/28.01')

file.load()
file.save()
