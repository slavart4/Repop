from spyre import server

import pandas as pd
import urllib
import matplotlib.pyplot as plt
import numpy as np

class StockExample(server.App):
  title = "Inputs"

  inputs = [{     "type":'dropdown',
                  "label": 'Index  ', 
                  "options" : [ {"label": "VCI", "value":"VCI"},
                                {"label": "TCI", "value":"TCI"},
                                {"label": "VHI", "value":"VHI"},],
                  "key": 'index', 
                  "action_id": "update_data"},

              {     "type":'dropdown',
                    "label": 'Region', 
                    "options" : [ {"label": "Vinnitsa", "value":"01"},
                                  {"label": "Volyn", "value":"02"},
                                  {"label": "Dnipropetrovsk", "value":"03"},
                                  {"label": "Donetsk", "value":"04"},
                                  {"label": "Zhytomyr", "value":"05"},
                                  {"label": "Zakarpattia", "value":"06"},
                                  {"label": "Zaporozhye", "value":"07"},
                                  {"label": "Ivano-Frankivsk", "value":"08"},
                                  {"label": "Kiev", "value":"09"},
                                  {"label": "Kirovograd", "value":"10"},
                                  {"label": "Lugansk", "value":"11"},
                                  {"label": "Lviv", "value":"12"},
                                  {"label": "Nikolaev", "value":"13"},
                                  {"label": "Odessa", "value":"14"},
                                  {"label": "Poltava", "value":"15"},
                                  {"label": "Rivnnska", "value":"16"},
                                  {"label": "Sumi", "value":"17"},
                                  {"label": "Ternopil", "value":"18"},
                                  {"label": "Kharkov", "value":"19"},
                                  {"label": "Kherson", "value":"20"},
                                  {"label": "Khmelnytskyy", "value":"21"},
                                  {"label": "Cherkas", "value":"22"},
                                  {"label": "Chernivtsi", "value":"23"},
                                  {"label": "Chernihiv", "value":"24"},
                                  {"label": "Crimea", "value":"25"},
                                  ],
                    "key": 'region', 
                    "action_id": "update_data"},

              {     "type":'dropdown',
                    "label": 'Region(for comparison)', 
                    "options" : [ {"label": "Vinnitsa", "value":"01"},
                                  {"label": "Volyn", "value":"02"},
                                  {"label": "Dnipropetrovsk", "value":"03"},
                                  {"label": "Donetsk", "value":"04"},
                                  {"label": "Zhytomyr", "value":"05"},
                                  {"label": "Zakarpattia", "value":"06"},
                                  {"label": "Zaporozhye", "value":"07"},
                                  {"label": "Ivano-Frankivsk", "value":"08"},
                                  {"label": "Kiev", "value":"09"},
                                  {"label": "Kirovograd", "value":"10"},
                                  {"label": "Lugansk", "value":"11"},
                                  {"label": "Lviv", "value":"12"},
                                  {"label": "Nikolaev", "value":"13"},
                                  {"label": "Odessa", "value":"14"},
                                  {"label": "Poltava", "value":"15"},
                                  {"label": "Rivnnska", "value":"16"},
                                  {"label": "Sumi", "value":"17"},
                                  {"label": "Ternopil", "value":"18"},
                                  {"label": "Kharkov", "value":"19"},
                                  {"label": "Kherson", "value":"20"},
                                  {"label": "Khmelnytskyy", "value":"21"},
                                  {"label": "Cherkas", "value":"22"},
                                  {"label": "Chernivtsi", "value":"23"},
                                  {"label": "Chernihiv", "value":"24"},
                                  {"label": "Crimea", "value":"25"},
                                  ],
                    "key": 'region2', 
                    "action_id": "update_data"},
  

              { "input_type":"text",
                "variable_name":"year",
                "label": "Year",
                "value":1981,
                "key": 'year',
                "action_id":"update_data"},

              { "type":'slider',
                "label": 'First week', 
                "min" : 1,"max" : 52,"value" : 1,
                "key": 'first', 
                "action_id": 'update_data'},

              { "type":'slider',
                "label": 'Last week', 
                "min" : 1,"max" : 52,"value" : 52,
                "key": 'last', 
                "action_id": 'update_data'},
                ]

  controls = [{   "type" : "hidden",
                  "id" : "update_data"}]

  tabs = ["Plot", "Table","Comparison"]

  outputs = [{ "type" : "plot",
                  "id" : "plot",
                  "control_id" : "update_data",
                  "tab" : "Plot"},
              { "type" : "table",
                "id" : "table",
                "control_id" : "update_data",
                "tab" : "Table"},
              { "type" : "plot",
                  "id" : "comp_plot",
                  "control_id" : "update_data",
                  "tab" : "Comparison"},  
               ]

  def state_name(self,id): 
    if (id == 1): 
        state = 'Vinnitsa'
        return state 
    elif (id == 2): 
        state = 'Volyn' 
        return state 
    elif (id == 3): 
        state = 'Dnipropetrovsk'
        return state 
    elif (id == 4): 
        state = 'Donetsk'
        return state 
    elif (id == 5): 
        state = 'Zhytomyr'
        return state 
    elif (id == 6):
        state = 'Zakarpattia'
        return state
    elif ( id == 7): 
        state = 'Zaporozhye' 
        return state 
    elif (id == 8): 
        state = 'Ivano-Frankivsk'
        return state 
    elif (id == 9): 
        state = 'Kyiv' 
        return state 
    elif (id == 10): 
        state = 'Kirovograd' 
        return state
    elif (id == 11): 
        state = 'Lugansk' 
        return state 
    elif (id == 12): 
        state = 'Lviv' 
        return state 
    elif (id == 13): 
        state = 'Nikolaev'
        return state 
    elif (id == 14): 
        state = 'Odessa' 
        return state 
    elif (id == 15): 
        state = 'Poltava' 
        return state
    elif (id == 16): 
        state = 'Rivnnska'
        return state 
    elif (id == 17): 
        state = 'Sumi' 
        return state 
    elif (id == 18): 
        state = 'Ternopil' 
        return state
    elif (id == 19): 
        state = 'Kharkov' 
        return state 
    elif (id == 20): 
        state = 'Kherson' 
        return state 
    elif (id == 21): 
        state = 'Khmelnytsky' 
        return state 
    elif (id == 22): 
        state = 'Cherkas'
        return state 
    elif (id == 23): 
        state = 'Chernivtsi' 
        return state 
    elif (id == 24): 
        state = 'Chernihiv'
        return state 
    elif (id == 25): 
        state = 'Republic of Crimea'
        return state

  def table(self, params):
    index = params['index']
    region = params['region']
    year = params['year']
    first = params['first']
    last = params['last']
    print(first)
    path = r'C:\Users\Слава\Прога\ProgaZH\Proga\lab2\{}2018-02-09.csv'.format(region)

    df = pd.read_csv(path,index_col=False,sep='\s+,*|,+\s*', header=0,engine="python")
    df=df[:-1]
    df1 = df[(df['year'].astype(int) == int(year)) & (df['week'] >= int(first)) & (df['week'] <= int(last))]
    df1 = df1[['week', index]]
    return df1

  def plot(self, params):
    index = params['index']
    year = params['year']
    first = params['first']
    last = params['last']
    df = self.table(params).set_index('week')
    plt_obj = df.plot()
    plt_obj.set_ylabel(index)
    plt_obj.set_title('Index {index} for {year} from {first} to {last} weeks'.format(index=index, 
      year=int(year), first=int(first), last=int(last)))
    fig = plt_obj.get_figure()
    return fig 

  def comp_plot(self, params):
    index = params['index']
    year = params['year']
    first = params['first']
    last = params['last']
    region1=self.state_name(int(params['region']))
    region2=self.state_name(int(params['region2']))
    df1 = self.table(params).set_index('week')
    params['region']=params['region2']
    df2 = self.table(params).set_index('week')
    ax = df1.plot()
    fig=df2.plot(ax=ax)
    fig.set_title('Index {index} for {year} from {first} to {last} weeks'.format(index=index, 
      year=int(year), first=int(first), last=int(last)))
    fig.set_ylabel(index)
    fig.legend([region1,region2])
    return fig 
app = StockExample()
app.launch()
