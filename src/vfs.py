"""Загрузка виртуальной файловой системы из ZIP-архива."""

import base64
import zipfile


def load_zip(path):
    """Загружает VFS из ZIP-архива в память.

    Архив не распаковывается: структура папок и содержимое
    файлов читаются напрямую. Папка представлена списком:
    первый элемент — словарь {имя: папка} вложенных папок,
    остальные — кортежи (имя, содержимое) файлов. Текстовые
    файлы хранятся строкой, двоичные — строкой base64.

    :param path: путь к ZIP-архиву с VFS
    :return: список, соответствующий корню VFS
    """
    root = [{}]
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            current = root
            parts = [part for part in name.split("/") if part]
            for part in parts[:-1]:
                current = current[0].setdefault(part, [{}])
            if name.endswith("/"):
                current[0].setdefault(parts[-1], [{}])
            else:
                data = archive.read(name)
                try:
                    content = data.decode("utf-8")
                except UnicodeDecodeError:
                    content = base64.b64encode(data).decode("ascii")
                current.append((parts[-1], content))
    return root
