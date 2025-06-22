from pathlib import PurePath
import os
from streamlit.runtime.uploaded_file_manager import UploadedFile

class FileOps:
    @staticmethod
    def save_file(file: UploadedFile):
        with open(file.name, "wb") as buffer:
            buffer.write(file.read())
        return PurePath(file.name)

    @staticmethod
    def delete_file(file: PurePath):
        if os.path.exists(file):
            os.remove(file)
        else: raise Exception(404, "File Not Found")