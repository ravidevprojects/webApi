# This script will rename the config file in configuration folder based on environment passed as argument
# sample command in cmd
# dev - python update_env_config.py dev (This will rename app_config.dev.ini to app_config.ini)
# test - python update_env_config.py test (This will rename app_config.test.ini to app_config.ini)

import os
import sys

def main():
    try:
        default_config = "app_config.ini"
        # Taking input from command line argument (dev,test,int,trn,qa,qadc1,qadc2,prod,proddc1,proddc2)
        #environment = str(sys.argv[1])
        environment = str("dev")

        directory = os.path.dirname(__file__)
        file_path = os.path.join(directory, 'configuration')

        print("Enviroment selected:" + environment)

        file_to_rename = "app_config" + "." + environment + ".ini"

        for filename in os.listdir(file_path):
            if filename == file_to_rename:
                os.rename(os.path.join(file_path, file_to_rename),os.path.join(file_path, default_config))
                print("Configuration is set to " + environment + " environment")
                break
    except Exception as exc:
        print("Error:" + str(exc))


# calling main function
main()


