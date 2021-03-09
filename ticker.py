import pandas as pd
import numpy as np
from important_keys import *

class Ticker():
    def __init__(self,ticker):
        self.ticker = ticker.upper()
        #"https://www.indopremier.com/module/saham/include/fundamental.php?code=ADRO&quarter=4"
        self.base_url = 'https://www.indopremier.com/module/saham/include/fundamental.php?code='
        self.scrape_url = self.base_url + self.ticker

    def get_data(self):
        df_list = pd.read_html(self.scrape_url)

        o = df_list
        return o

    def get_last_data(self):
        all_data = self.get_data()
        df = all_data[0]
        last_and_indx = df.iloc[:, [1, 2]]

        return last_and_indx

    def dict_last_data(self):
        last_data = self.get_last_data()
        col_name = list(last_data)
        return last_data.set_index('GO')[col_name[-1]].to_dict()

    def get_data_by_key(self,ky):
        dict_last_data = self.dict_last_data()
        return dict_last_data[key_dict[ky]]