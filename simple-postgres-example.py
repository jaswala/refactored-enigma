#!/usr/bin/python

# simple postgres connection to DB

import pg
import pandas as pd
from pandas import Series, DataFrame

conn = pg.DB(host="******", user="***", passwd="****", dbname="**")

result = conn.query("""  """)

for channel_code, channel_name in result.getresult() :
    print channel_code, channel_name

#creating dataframe of sql results
df=DataFrame(result.getresult(), columns=['channel_code', 'channel_name'])



conn.close()


