import logging
import os

log_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

command_logger = logging.getLogger('command_logger')
command_logger.setLevel(logging.INFO)

command_handler = logging.FileHandler(os.path.join(log_directory, 'commands.log'))
command_handler.setLevel(logging.INFO)

command_formatter = logging.Formatter('%(asctime)s - %(message)s')
command_handler.setFormatter(command_formatter)

command_logger.addHandler(command_handler)

error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)

error_handler = logging.FileHandler(os.path.join(log_directory, 'errors.log'))
error_handler.setLevel(logging.ERROR)

error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)

error_logger.addHandler(error_handler)
