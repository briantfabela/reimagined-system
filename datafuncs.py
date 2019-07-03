# Data functions, objects, and methods for handling data

import quandl # you need to 'pip install quandl'
import matplotlib.pyplot as plt
import pandas as pd # using pandas to read data
import datetime
import numpy as np # numpy library for distribution/stats of data

QUANDL_API_KEY = 'JdQyF9KDxGpy7kwa9oia'

class quandl_data:
    '''Methods for handling Quandl data. Pass quandl.get() arguements as **kwargs'''

    def __init__(self, quandl_dataset_code, **kwargs):
        self.q_code = quandl_dataset_code
        self.data = self.fetch_data(self.q_code, **kwargs) # raw data

    def fetch_data(self, code, **kwargs):
        '''Makes the api call and returns the response'''
        # quandl.com/data/../usage/quickstart/python

        quandl.ApiConfig.api_key = QUANDL_API_KEY
        self.time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        return quandl.get(code, **kwargs) # ** opens the dict

  
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict
