def parser(command):
    """Разбивает строку ввода на команду и аргументы по пробелам.

    :param command: строка, введённая пользователем
    :return: список, где первый элемент — имя команды,
             остальные — её аргументы
    """
    return command.split()


if __name__ == "__main__":
    flag = True

    while flag:
        new_command = input("VFS$ ")
        parts = parser(new_command)
        if len(parts) != 0:
            if parts[0] == "exit":
                flag = False
            elif parts[0] == "ls":
                print(*parts)
            elif parts[0] == "cd":
                print(*parts)
            else:
                print("Unknown command")
