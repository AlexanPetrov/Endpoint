def test_delete_directory_success(directory_tree):
    directory_tree.create_directory("fruits")
    directory_tree.create_directory("fruits/apples")
    directory_tree.create_directory("vegetables")
    directory_tree.move_directory("fruits/apples", "vegetables")
    
    result = directory_tree.delete_directory("vegetables/apples")
    assert result == "DELETE vegetables/apples"

    with open('logs/commands.log') as log_file:
        log_contents = log_file.read()
    assert "DELETE vegetables/apples" in log_contents

def test_delete_directory_failure(directory_tree):
    directory_tree.create_directory("fruits")
    directory_tree.create_directory("fruits/apples")
    directory_tree.create_directory("vegetables")
    directory_tree.move_directory("fruits/apples", "vegetables")

    result = directory_tree.delete_directory("fruits/apples")
    assert result == "Cannot delete fruits/apples - fruits does not exist"

    with open('logs/errors.log') as log_file:
        log_contents = log_file.read()
    assert "Cannot delete fruits/apples - fruits does not exist" in log_contents
