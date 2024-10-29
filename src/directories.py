from directory_tree import DirectoryTree

def main():
    directory_tree = DirectoryTree()
    print("Directory structure initialized.")
    print("Enter commands (e.g., CREATE, MOVE, DELETE, LIST) or 'exit' to quit:")

    while True:
        command_input = input("> ").strip()

        if command_input.lower() == 'exit':
            print("Exiting program.")
            break

        command_parts = command_input.split(maxsplit=1)
        command = command_parts[0].upper()

        if command == "CREATE":
            if len(command_parts) > 1:
                path = command_parts[1]
                result = directory_tree.create_directory(path)
                print(result)
            else:
                print("CREATE command requires a path argument.")

        elif command == "MOVE":
            if len(command_parts) > 1:
                args = command_parts[1].split()
                if len(args) == 2:
                    source, destination = args
                    result = directory_tree.move_directory(source, destination)
                    print(result)
                else:
                    print("MOVE command requires a source and destination path.")
            else:
                print("MOVE command requires arguments.")

        elif command == "DELETE":
            if len(command_parts) > 1:
                path = command_parts[1]
                result = directory_tree.delete_directory(path)
                print(result)
            else:
                print("DELETE command requires a path argument.")

        elif command == "LIST":
            print(directory_tree.list_directories())

        else:
            print("Unrecognized command. Please use CREATE, MOVE, DELETE, LIST, or 'exit'.")

if __name__ == "__main__":
    main()
