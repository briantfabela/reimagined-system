import quandl # you need to 'pip install quandl'
import matplotlib.pyplot as plt
import pandas as pd # using pandas to read data
import datetime
import numpy as np # numpy library for distribution/stats of data

QUANDL_API_KEY = 'JdQyF9KDxGpy7kwa9oia'

class quandl_data:
    '''Pass quandl.get() arguements as **kwargs'''

    def __init__(self, quandl_dataset_code, **kwargs):
        self.q_code = quandl_dataset_code
        self.data = self.fetch_data(self.q_code, **kwargs) # raw data

    def fetch_data(self, code, **kwargs):
        '''Makes the api call and returns the response'''
        # quandl.com/data/../usage/quickstart/python

        quandl.ApiConfig.api_key = QUANDL_API_KEY
        self.time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        return quandl.get(code, **kwargs) # ** opens the dict

def main():
    # sample call
    #fed_debt_data = quandl_data("FRED/GFDEBTN", returns="pandas")
    
    # bank of mexico; peso per US Dollar (Nov 1991 - Present)
    mxn_usd = quandl_data("BDM/SF60653")

    # basic sample plot
    plt.plot(mxn_usd.data)
    plt.title("Peso per US Dollar")
    plt.show()

if __name__ == "__main__":
    main()

    
'''
# Sample Visual
def graph_it(x, y){
    plt.plot(x, y)    
}
'''

# filtering out based on length
sample_list = []
n = 0 # specified length number
result = filter(lambda sample_list: len(sample_list) > n, sample_list)
