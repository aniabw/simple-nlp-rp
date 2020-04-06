from text_checker.classes.data_source import Data_source_interface
import glob

class File(Data_source_interface):

    def __init__(self, dir_path, file_extention):
        self.dir_path = dir_path
        self.file_extention = file_extention

    def read_file(self, file_source):
        file = open(file_source, encoding="utf8")
        data = file.read()
        file.close()
        return data

    def get_files_from_directory_by_extention(self):
        files = glob.glob(self.dir_path + "*." + self.file_extention)
        return files