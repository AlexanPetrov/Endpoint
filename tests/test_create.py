def test_create_root_directory(directory_tree):
    result = directory_tree.create_directory("fruits")
    assert result == "CREATE fruits"

    with open('logs/commands.log') as log_file:
        log_contents = log_file.read()
    assert "CREATE fruits" in log_contents

def test_create_nested_directory(directory_tree):
    directory_tree.create_directory("fruits")
    result = directory_tree.create_directory("fruits/apples")
    assert result == "CREATE fruits/apples"

    with open('logs/commands.log') as log_file:
        log_contents = log_file.read()
    assert "CREATE fruits/apples" in log_contents
