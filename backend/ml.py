# tba

import torch
import pandas as pd
import os
from datetime import *

# Crash data (driving)

traffic_raw = pd.read_csv("~/Downloads/traffic_crashes.csv")
traffic_clean = traffic_raw[["LONGITUDE", "LATITUDE", "WEATHER_CONDITION", "CRASH_HOUR"]]
print(traffic_clean.head())

# Crime data (walking)

crimes_raw = pd.read_csv("~/Downloads/crimes.csv")
crimes_clean = crimes_raw[["Latitude", "Longitude", "Date"]]
crimes_clean.dropna(axis=0, inplace=True)