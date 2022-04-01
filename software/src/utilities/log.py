import logging
from pathlib import Path

RACCOONREPELLER = 'RaccoonRepeller'

class Logger:

    def __init__(self):
        logs_folder = 'logs/'
        Path(logs_folder).mkdir(parents=True, exist_ok=True)

        # create file handler which logs even debug messages
        self.logging_file_handler = logging.FileHandler(logs_folder + RACCOONREPELLER +'.log')
        # self.logging_file_handler.setLevel(logging.DEBUG)

        # create console handler with a higher log level
        self.logging_console_handler = logging.StreamHandler()
        # self.logging_console_handler.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logging_file_handler.setFormatter(formatter)
        self.logging_console_handler.setFormatter(formatter)

    def setup_logger(self, name=None, level=logging.INFO):
        """
        Setup logger
        """
        if not name:
            name = RACCOONREPELLER
        else:
            name = RACCOONREPELLER + ' ' + name

        logger = logging.getLogger("{:<32}".format(name))
        logger.setLevel(level)
        logger.addHandler(self.logging_file_handler)
        logger.addHandler(self.logging_console_handler)
        return logger
