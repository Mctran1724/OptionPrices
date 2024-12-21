import numpy as np
from scipy.stats import norm
from Option import OptionModel

class BlackScholesMertonModel(OptionModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        return
    
    def calculate(self, K: float) -> float:
        
        d1 = (np.log(self._s/K) + self._r + self._sigma**2/2)*self._T / (self._sigma*np.sqrt(self._T))
        d2 = d1 - self._sigma * np.sqrt(self._T)
        N = norm.cdf

        if self._is_call:
            return N(d1) * self._s - N(d2) * K * np.exp(-self._r*self._T)
        else:
            return K * np.exp(-self._r * T) * N(-d2) - self._s * N(-d1)

