# External libraries
#from io import BytesIO
#import json
#import requests
#import xml.etree.ElementTree as ET

# Internal modules
#from config import *
from scripts.pardot_clean_test import pardot_login
from scripts.pardot_csv import pardot_export_cleaner
#from scripts.pardot_cleaner import *

def rosie():
  # PARDOT API
  #api_key = pardot_login()
  #print(api_key)

  # PARDOT CSV
  pardot_export_cleaner()
  return

if __name__ == '__main__':
  rosie()

