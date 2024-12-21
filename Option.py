import numpy as np
from scipy.stats import norm

#generic model class and various subclasses for each model


class OptionModel:

    def __init__(self, underlying_price: float, strike_price: float, risk_free_rate: float, time_to_expiry: float, sigma: float, opttype: str = 'Call') -> None:
        """Generic class for all models that takes in generalized parameters

        Arguments: 
        __________

        underlying_price: float
        strike_price: float
        risk_free_rate: float
        time_to_expiry: float
        sigma: float
        opttype: str in ['Call', 'Put']
        
        """
        self._K = strike_price
        self._s = underlying_price
        self._r = risk_free_rate
        self._T = time_to_expiry
        self._sigma = sigma
        self._is_call = True if (opttype.lower().strip() == 'call') or (opttype.lower().strip() == 'c') else False

        return



if __name__=="__main__":
    S0 = 100
    K = 100
    T = 1
    r = 0.06
    sigma = 0.3

    model = OptionModel(S0, K, r, T, sigma)