import configparser
import logging

def validate_settings(config):
    
    errors = []
    
   
    if 'DATABASE' not in config:
        errors.append("Error: 'DATABASE' section is missing.")
    else:
       
        if 'host' not in config['DATABASE']:
            errors.append("Error: 'host' is missing in the 'DATABASE' section.")
        if 'port' not in config['DATABASE']:
            errors.append("Error: 'port' is missing in the 'DATABASE' section.")
    
    
    
    return errors

def write_errors_to_log(errors):
    
    if errors:
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        for error in errors:
            logging.error(error)

if __name__ == "__main__":
   
    config = configparser.ConfigParser()
    config.read('config.ini')

   
    errors = validate_settings(config)

    
    write_errors_to_log(errors)
