'''
Used to load and store data.
1 - json handling and json data structures. 
1.1 - load_data() -> This function is used to load the data from the storage which is present in json structure into the memory and load
it as a list in the memory. To perform operation on the list.
1.2 - save_data() -> This is used to save the data back into the storage using 'w' mode of file operation. It rewrite the entire list of json
with the current list in the memory. The data is not lost as when creating a new data and appending it to the json file we used .append to 
just add the new data to the current list. In visual: A truck have a set of data. Then you have the same set of data in warehouse. Then what
you do is jsut add one more data to the warehouse then you destroy the previous data on the truck and load the truck with current set of data from warehouse.
'''

import json
import logging
import bank_log

logging.info(" ==== Entered DATA module ==== ")

def load_data():
    '''
    Loads the data as a list from json structure present the storage to memory.
    '''
    try:
        with open("bank_db.json",'r') as file:
            logging.info("Database found loading it into memory.")
            return json.load(file)
    except json.decoder.JSONDecodeError:
        logging.critical("JSON file is corrupted")
        return []
    except FileNotFoundError:
        logging.warning("Loaded JSON data is empty.")
        return []

def save_data(bank_account):
    '''
    Save the data in 'w': write mode in storage
    '''
    with open("bank_db.json", 'w') as file:
        logging.info("Rewriting old Data with New data. Saving it")
        json.dump(bank_account, file, indent=4)