import argparse


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
    args = arg_parser.parse_args()

    return args


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


def execute_file(file_name):
    """Выполняет команды из стартового скрипта.

    Пустые строки и комментарии (#) пропускаются.
    Каждая команда выводится вместе с приглашением.

    :param file_name: путь к файлу скрипта
    :return: False, если в скрипте встретилась команда exit,
             иначе True
    """
    try:
        with open(file_name, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                print(f"VFS$ {line}")
                if not execute(line):
                    return False
            return True
    except FileNotFoundError:
        print(f"script not found: {file_name}")
        return True


def repl():
    """Запускает интерактивный режим ввода команд до команды exit."""
    while True:
        new_command = input("VFS$ ")
        if not execute(new_command):
            break


if __name__ == "__main__":
    args = parse_args()
    vfs = args.vfs
    script = args.script
    print(f"[debug] vfs = {vfs}")
    print(f"[debug] script = {script}")
    if not script or execute_file(script):
        repl()
