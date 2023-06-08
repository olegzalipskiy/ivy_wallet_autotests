import os
import shutil

from pathlib import Path


class FileSystem:

    @staticmethod
    def get_project_root() -> str:
        return Path(__file__).parent.parent.parent.absolute().__str__()

    @staticmethod
    def get_absolute_path(*path: str) -> str:
        return os.sep.join([FileSystem.get_project_root()] + [*path])

    @staticmethod
    def make_dir(*path: str):
        path = FileSystem.get_absolute_path(*path)
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def delete_dir(*path: str):
        directory_to_delete_path = FileSystem.get_absolute_path(*path)
        shutil.rmtree(directory_to_delete_path, ignore_errors=True)

    @staticmethod
    def delete_file(*path: str):
        path = FileSystem.get_absolute_path(*path)
        if os.path.isfile(path):
            os.remove(path)

    @staticmethod
    def rename_file(absolute_file_path_to_change: str, new_file_absolute_path: str):
        shutil.move(absolute_file_path_to_change, new_file_absolute_path)

    @staticmethod
    def get_list_of_files_in_folder(*path: str, sort: str = None, reverse: bool = False) -> list:
        sort_functions_dict = {
            'time': os.path.getmtime,
            'size': os.path.getsize
        }
        directory_path = FileSystem.get_absolute_path(*path)
        files_list = [directory_path + os.sep + f for f in os.listdir(directory_path)]
        return sorted(files_list, key=sort_functions_dict[sort], reverse=reverse) if sort \
            else sorted(files_list, reverse=reverse)
