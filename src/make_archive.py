"""Сборка тестовых VFS: каждая папка из vfs/ упаковывается в ZIP."""

import shutil

VFS_DIRS = {
    "minimal": "vfs/minimal",
    "multi": "vfs/multi",
    "deep": "vfs/deep",
}


def create_zip(zip_name, dir_name):
    """Упаковывает папку в ZIP-архив.

    :param zip_name: имя архива без расширения .zip
    :param dir_name: путь к папке, содержимое которой
                     попадёт в архив
    """
    shutil.make_archive(zip_name, "zip", dir_name)
    print(f"created {zip_name}.zip from {dir_name}")


if __name__ == "__main__":
    for name, path in VFS_DIRS.items():
        create_zip(name, path)
