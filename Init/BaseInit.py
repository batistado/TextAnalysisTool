import fnmatch
import os

from Init.Singleton import Singleton


class BaseInit(metaclass=Singleton):
    @staticmethod
    def get_files(directory, pattern='*.txt'):
        for root, dirs, files in os.walk(directory):
            for basename in fnmatch.filter(files, pattern):
                filename = os.path.join(root, basename)
                yield filename

    @staticmethod
    def get_element(soup_object, element):
        return soup_object.find(element).text.strip()
