from config import PARDOT_EMAIL, PARDOT_PASS, PARDOT_API_KEY
from pypardot.client import PardotAPI
import pandas as pd


def pardot_login():
  p = PardotAPI(
    email=PARDOT_EMAIL,
    password=PARDOT_PASS,
    user_key=PARDOT_API_KEY
  )

  p.authenticate()
  return p

def clean_pardot():
  p = pardot_login()
  #prospects  = p.prospects.query()
  #print(prospects)
  curl https://pi.pardot.com/api/visitorActivity/version/3/do/query?output=bulk&format=json&created_after=2016-03-29T00:00:00&created_before=2016-03-30T00:00:00&sort_by=created_at&sort_order=ascending -H "Authorization: Pardot user_key=1234567890abcdef1234567890abcdef, api_key=fedcba0987654321fedcba0987654321"
  return

if __name__ == '__main__':
  clean_pardot()



