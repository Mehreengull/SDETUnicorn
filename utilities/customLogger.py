import logging


class Logger:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        filepath = './Logs/test_logs.log'
        file_handler = logging.FileHandler(filepath)
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", datefmt='%m%d%Y %I:%M %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
