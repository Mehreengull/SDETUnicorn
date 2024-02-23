import configparser

config = configparser.RawConfigParser()
config.read("configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getShopURL():
        url = config.get("common info", "baseURL")
        return url
