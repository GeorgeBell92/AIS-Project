# The downloaded data does not include headers
# This script adds headers to the data, for use in GIS and pandas.
# It does not replace the original file because headers may be a hindrance for some applications

import pandas as pd
file = "ships.csv"
db = pd.read_csv(file, header=None)
db.head()
db.rename(columns={0: "Identity",1: "Longitude",2:"Latitude",3:"Timestamp"},inplace=True)
db.head()
db.to_csv('ships_headers.csv',index=False)
db_2 = pd.read_csv("ships_headers.csv")
db_2.head()