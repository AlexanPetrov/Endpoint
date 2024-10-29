from directory_node import DirectoryNode
from logging_config import command_logger, error_logger

class DirectoryTree:
    def __init__(self):
        """
        Initializes the directory tree with a root directory.
        """
        self.root = DirectoryNode("root")

    def create_directory(self, path):
        """
        Creates a new directory at the specified path.
        
        Args:
            path (str): The path where the directory will be created.
        
        Returns:
            str: Message indicating success or failure of the operation.
        """
        path_parts = path.split("/")
        current = self.root

        for part in path_parts:
            if not current.has_child(part):
                new_dir = DirectoryNode(part)
                current.add_child(new_dir)
            current = current.get_child(part)

        command_logger.info(f"CREATE {path}")
        return f"CREATE {path}"

    def move_directory(self, source, destination):
        """
        Moves a directory from source to destination.
        
        Args:
            source (str): The path of the directory to move.
            destination (str): The path where the directory will be moved.
        
        Returns:
            str: Message indicating success or failure of the operation.
        """
        source_parts = source.split("/")
        destination_parts = destination.split("/")

        if len(source_parts) == 1:
            source_parent = self.root
        else:
            source_parent = self._navigate_to_parent(source_parts)

        if not source_parent or not source_parent.has_child(source_parts[-1]):
            parent_dir = source_parts[-2] if len(source_parts) > 1 else "root"
            error_message = f"Cannot move {source} - {parent_dir} does not exist"
            error_logger.error(error_message)
            return error_message


        destination_node = self._navigate_to_node(destination_parts)
        if not destination_node:
            error_message = f"Cannot move {source} - {destination} does not exist"
            error_logger.error(error_message)
            return error_message

        directory_to_move = source_parent.remove_child(source_parts[-1])
        destination_node.add_child(directory_to_move)

        command_logger.info(f"MOVE {source} {destination}")
        return f"MOVE {source} {destination}"

    def delete_directory(self, path):
        """
        Deletes the directory at the specified path.
        
        Args:
            path (str): The path of the directory to delete.
        
        Returns:
            str: Message indicating success or failure of the operation.
        """
        path_parts = path.split("/")
        parent = self._navigate_to_parent(path_parts)

        if not parent or not parent.has_child(path_parts[-1]):
            error_message = f"Cannot delete {path} - {path_parts[-2]} does not exist"
            error_logger.error(error_message)
            return error_message

        parent.remove_child(path_parts[-1])
        command_logger.info(f"DELETE {path}")
        return f"DELETE {path}"

    def list_directories(self):
        """
        Lists all directories and their subdirectories in a hierarchical format.
        
        Returns:
            str: A formatted string representing the directory tree without showing the root.
        """
        def _list_recursive(node, depth=0):
            result = "  " * depth + node.name + "\n"
            for child in sorted(node.children.values(), key=lambda x: x.name):
                result += _list_recursive(child, depth + 1)
            return result

        command_logger.info("LIST")
        output = ""
        for child in sorted(self.root.children.values(), key=lambda x: x.name):
            output += _list_recursive(child, depth=0)
        return output

    def _navigate_to_node(self, path_parts):
        """
        Navigates to the node specified by path_parts.
        
        Args:
            path_parts (list of str): The path components to navigate.
        
        Returns:
            DirectoryNode: The node at the specified path or None if not found.
        """
        current = self.root
        for part in path_parts:
            if not current.has_child(part):
                return None
            current = current.get_child(part)
        return current

    def _navigate_to_parent(self, path_parts):
        """
        Navigates to the parent of the node specified by path_parts.
        
        Args:
            path_parts (list of str): The path components to navigate.
        
        Returns:
            DirectoryNode: The parent node or None if not found.
        """
        if len(path_parts) <= 1:
            return None
        return self._navigate_to_node(path_parts[:-1])
