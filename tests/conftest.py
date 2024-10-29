import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from directory_tree import DirectoryTree

def clear_logs():
    open('logs/commands.log', 'w').close()
    open('logs/errors.log', 'w').close()

@pytest.fixture
def directory_tree():
    clear_logs()
    return DirectoryTree()
