class DirectoryNode:
    def __init__(self, name):
        """
        Represents a single directory within the tree structure.
        
        Args:
            name (str): The name of the directory.
        """
        self.name = name
        self.children = {}

    def add_child(self, child):
        """
        Adds a child directory to this node.
        
        Args:
            child (DirectoryNode): The directory node to add as a child.
        """
        self.children[child.name] = child

    def get_child(self, name):
        """
        Retrieves a child directory by name.
        
        Args:
            name (str): The name of the child directory to retrieve.
            
        Returns:
            DirectoryNode: The child directory node if it exists, otherwise None.
        """
        return self.children.get(name)

    def remove_child(self, name):
        """
        Removes a child directory by name.
        
        Args:
            name (str): The name of the child directory to remove.
            
        Returns:
            DirectoryNode: The removed child directory if it exists, otherwise None.
        """
        return self.children.pop(name, None)

    def has_child(self, name):
        """
        Checks if a child directory with the given name exists.
        
        Args:
            name (str): The name of the child directory to check.
            
        Returns:
            bool: True if the child exists, False otherwise.
        """
        return name in self.children
