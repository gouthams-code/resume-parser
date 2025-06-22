from pathlib import Path
from streamlit.runtime.uploaded_file_manager import UploadedFile

class FileOps:
    @staticmethod
    def save_file(file: UploadedFile):
        with open(file.name, "wb") as buffer:
            buffer.write(file.read())
        return Path(file.name)

    @staticmethod
    def delete_file(file: Path):
        if file.exists():
            file.unlink()
        else: raise Exception(404, "File Not Found")