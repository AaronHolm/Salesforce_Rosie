import pandas as pd
from .dict_country import countries
from .dict_state import states

def pardot_export_cleaner():
  df = pd.read_csv('/mnt/c/users/AHolm/Work Folders/Documents/Salesforce/Pardot_export_for_state_country_picklist/Pardot_export_for_state_country_picklist.csv')
  df = df[['Prospect Id', 'Email', 'State', 'Country']]
  df = clean_country(df)
  df = clean_states(df)
  df.loc[:, 'state_country'] = [str(row['State']) + ', ' + str(row['Country']) for i, row in df.iterrows()]
  #print(df.head())
  #df.to_excel('/mnt/c/users/AHolm/Work Folders/Documents/Salesforce/Pardot_export_for_state_country_picklist/Pardot_cleaned2.xlsx', index=False)
  df.to_csv('/mnt/c/users/AHolm/Work Folders/Documents/Salesforce/Pardot_export_for_state_country_picklist/Pardot_cleaned2.csv', index=False)

  return

def clean_country(df):
  #print(countries.keys())
  df.loc[:, 'Country'] = [countries[country] if country in countries.keys() else country for country in df['Country']]
  return df

def clean_states(df):
  df.loc[:, 'State'] = [states[state] if state in states.keys() else state for state in df['State']]
  return df
