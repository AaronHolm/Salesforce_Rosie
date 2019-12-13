#import pycurl
#import re


from io import BytesIO
import json
import requests
import xml.etree.ElementTree as ET
from config import *

def pardot_login():
  payload = {"email":PARDOT_EMAIL, "password":PARDOT_PASS, "user_key": PARDOT_USER_KEY}
  session = requests.Session()
  #response = session.post('https://pi.pardot.com/api/login/version/3 HTTP/1.1', data=payload)
  response = session.post('https://pi.pardot.com/api/login/version/4 HTTP/1.1', data=payload)
  tree = ET.parse(BytesIO(response.content))
  root = tree.getroot()
  PARDOT_API_KEY = None
  for child in root:
    if(child.tag == 'api_key'):
      PARDOT_API_KEY = child.text
      break
  return PARDOT_API_KEY



headers = {}
def header_function(header_line):
  header_line = header_line.decode('iso-8859-1')
  if ':' not in header_line:
    return

  name, value = header_line.split(':', 1)

  name = name.strip()
  value = value.strip()

  name = name.lower()
  headers[name] = value

  return

def simple_post():
  payload = {"email":PARDOT_EMAIL, "password":PARDOT_PASS, "user_key": PARDOT_USER_KEY}
  session = requests.Session()
  response = session.post('https://pi.pardot.com/api/login/version/3 HTTP/1.1', data=payload)
  #print(response.content, '\n', response.status_code)
  #tree = ElementTree.fromstring(response.content)
  tree = ET.parse(BytesIO(response.content))
  root = tree.getroot()
  for child in root:
    print(child.tag, child.text)
  return

if __name__ == '__main__':
  #simple_post()
  api_key = pardot_login()
  print(api_key)
