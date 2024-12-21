import numpy as np
from scipy.stats import norm
from Option import OptionModel

class MonteCarloModel(OptionModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return
    
    #Simulate something happening to the stock price and check resultant aggregate effects in the option price
