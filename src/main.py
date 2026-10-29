import argparse
import os
import sys
import zipfile

from src.vfs import load_zip


def parser(command):
    """Разбивает строку ввода на команду и аргументы по пробелам.

    :param command: строка, введённая пользователем
    :return: список, где первый элемент — имя команды,
             остальные — её аргументы
    """
    return command.split()


def parse_args():
    """Читает параметры командной строки.

    :return: объект с полями vfs и script
    """
    arg_parser = argparse.ArgumentParser(description="Эмулятор оболочки")
    arg_parser.add_argument("--vfs", help="путь к VFS")
    arg_parser.add_argument("--script", help="путь к стартовому скрипту")
    return arg_parser.parse_args()


def execute(line):
    """Выполняет одну строку ввода.

    :param line: строка с командой и аргументами
    :return: False, если введена команда exit, иначе True
    """
    parts = parser(line)
    if len(parts) != 0:
        if parts[0] == "exit":
            return False
        elif parts[0] == "ls":
            print(*parts)
        elif parts[0] == "cd":
            print(*parts)
        else:
            print("Unknown command")
    return True


def execute_file(file_name, root_name):
    """Выполняет команды из стартового скрипта.

    Пустые строки и комментарии (#) пропускаются.
    Каждая команда выводится вместе с приглашением.

    :param file_name: путь к файлу скрипта
    :param root_name: имя VFS для приглашения к вводу
    :return: False, если в скрипте встретилась команда exit,
             иначе True
    """
    try:
        with open(file_name, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                print(f"{root_name}$ {line}")
                if not execute(line):
                    return False
            return True
    except FileNotFoundError:
        print(f"script not found: {file_name}")
        return True


def repl(root_name):
    """Запускает интерактивный режим ввода команд до команды exit.

    :param root_name: имя VFS для приглашения к вводу
    """
    while True:
        new_command = input(f"{root_name}$ ")
        if not execute(new_command):
            break


if __name__ == "__main__":
    vfs_name = "VFS"
    args = parse_args()
    vfs = args.vfs
    script = args.script
    print(f"[debug] vfs = {vfs}")
    print(f"[debug] script = {script}")
    if vfs:
        try:
            root = load_zip(vfs)
            vfs_name = os.path.splitext(os.path.basename(vfs))[0]
        except FileNotFoundError:
            print(f"VFS not found: {vfs}")
            sys.exit(1)
        except zipfile.BadZipFile:
            print(f"invalid VFS format: {vfs}")
            sys.exit(1)
    if not script or execute_file(script, vfs_name):
        repl(vfs_name)
