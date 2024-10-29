def test_move_directory_success(directory_tree):
    directory_tree.create_directory("fruits")
    directory_tree.create_directory("fruits/apples")
    directory_tree.create_directory("vegetables")

    result = directory_tree.move_directory("fruits/apples", "vegetables")
    assert result == "MOVE fruits/apples vegetables"

    with open('logs/commands.log') as log_file:
        log_contents = log_file.read()
    assert "MOVE fruits/apples vegetables" in log_contents

def test_move_directory_failure(directory_tree):
    directory_tree.create_directory("fruits")
    directory_tree.create_directory("fruits/apples")

    result = directory_tree.move_directory("fruits/apples", "vegetables")
    assert result == "Cannot move fruits/apples - vegetables does not exist"

    with open('logs/errors.log') as log_file:
        log_contents = log_file.read()
    assert "Cannot move fruits/apples - vegetables does not exist" in log_contents
