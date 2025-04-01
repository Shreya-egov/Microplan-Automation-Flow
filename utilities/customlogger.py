import logging

class LogGen:
    @staticmethod
    def loggen():
        # Create a logger
        logger = logging.getLogger()
        
        # Set the logging level (e.g., DEBUG, INFO, ERROR, etc.)
        logger.setLevel(logging.INFO)
        
        # Create a file handler to write logs to 'mylog.log'
        fhandler = logging.FileHandler(filename='mylog.log', mode='a')
        
        # Define the log format and date format
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(fhandler)
        
        return logger
