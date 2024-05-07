from model import EpsteinCivilViolence
from mesa import batch_run

import pandas as pd

# NOTE: You do not need this as a separate file BUT it can be nice to track
# can also call the file and it makes things a little cleaner as it runs

# Here you will have elements that you want to sweep, eg:
# parameters that will remain constant
# parameters you want to vary
parameters = {"schedule_type": ("Random", "Simultaneous")}


# what to run and what to collect
# iterations is how many runs per parameter value
# max_steps is how long to run the model
results = batch_run(EpsteinCivilViolence, 
                    parameters,
                    iterations=10,  
                    max_steps=30, 
                    data_collection_period = -1) #how often do you want to pull the data #blank to do end of run





## NOTE: to do data collection, you need to be sure your pathway is correct to save this!
# Data collection
# extract data as a pandas Data Frame
pd.DataFrame(results).to_csv("5_Sheduling/pd_grid/data/batch_data.csv")