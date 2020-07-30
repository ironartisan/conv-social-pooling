#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : cyl
# @Time : 2020/7/24 11:52 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
file_ =  os.path.join('./data','Next_Generation_Simulation__NGSIM__Vehicle_Trajectories_and_Supporting_Data.csv')
ngisim_data = pd.read_csv(file_,nrows=1000)
print(ngisim_data.head(5))
