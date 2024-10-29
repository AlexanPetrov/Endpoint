def test_list_directories(directory_tree):
    directory_tree.create_directory("fruits")
    directory_tree.create_directory("fruits/apples")
    directory_tree.create_directory("vegetables")

    expected_output = "fruits\n  apples\nvegetables\n"
    result = directory_tree.list_directories()
    assert result == expected_output

    with open('logs/commands.log') as log_file:
        log_contents = log_file.read()
    assert "LIST" in log_contents
