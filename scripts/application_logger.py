import logging
import sys


class logghandler:

    def __init__(self,logger_name,file_name):
        self.logger_name =logger_name
        self.file_name=file_name
        self.FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
       
    
    def get_console_handler(self):
       console_handler = logging.StreamHandler(sys.stdout)
       console_handler.setFormatter(self.FORMATTER)
       return console_handler
    
    def get_file_handler(self):
       file_handler = logging.FileHandler(self.file_name)
       file_handler.setFormatter(self.FORMATTER)
       return file_handler

    def get_logger(self,level):
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(level) # better to have too much log than not enough
        logger.addHandler(self.get_console_handler())
        logger.addHandler(self.get_file_handler())
        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False
        return logger
    