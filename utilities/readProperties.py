import configparser

class ReadConfig:
    config = configparser.ConfigParser()
    config.read(".//configurations/config.ini")  
    @staticmethod
    def get_application_url():
        """Retrieve the base URL from the config file."""
        return ReadConfig.config.get('credentials', 'baseURL')

    @staticmethod
    def get_username():
        """Retrieve the username from the config file."""
        return ReadConfig.config.get('credentials', 'username')

    @staticmethod
    def get_password():
        """Retrieve the password from the config file."""
        return ReadConfig.config.get('credentials', 'password')
    
    @staticmethod
    def get_country_name():
        return ReadConfig.config.get('credentials', 'country_name')

    @staticmethod
    def get_bednet_name():
        return ReadConfig.config.get('dropdowns', 'Bednet_name')
    
    @staticmethod
    def get_country():
        return ReadConfig.config.get('dropdowns', 'countrydrop')
    
    @staticmethod
    def get_province():
        return ReadConfig.config.get('dropdowns', 'provincedrop')
    
    @staticmethod
    def get_district():
        return ReadConfig.config.get('dropdowns', 'districtdrop')
    
        
    @staticmethod
    def get_AP():
        return ReadConfig.config.get('dropdowns', 'APdrop')
