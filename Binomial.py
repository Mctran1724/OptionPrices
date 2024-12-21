import numpy as np
from Option import OptionModel





class BinomialModel(OptionModel):


    def B(self) -> float:
        return np.exp(self._r * self._time_step)

    def compute_tree(self) -> float:
        N = self._periods
        B = self.B()
        p = (B-self._d)/(self._u-self._d)
        q = 1-p

        option_prices = np.zeros((N+1, N+1))
        stock_prices = np.zeros(N+1)

        #maturity date stock and option prices
        stock_prices = S*self._d**(np.arange(N, -1, -1)) * self._u**(np.arange(0, N+1, 1))
        option_prices[-1] = np.maximum(stock_prices - self._K, np.zeros(N+1))
        for i in range(N, 0, -1):
            new_row =  (p * option_prices[i, 1:i+1:] + q * option_prices[i, :i])/B
            option_prices[i-1, :i] = new_row

        return option_prices

    def calculate(self):
        return self.compute_tree[0,0]

    def __init__(self, n: int = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._periods = n
        self._time_step = self._T/n
        self._u = np.exp(self._sigma * np.sqrt(self._T))
        self._d = 1/self._u

        
if __name__=="__main__":
    K = 100
    T = 1
    S = 100
    r = 0.06
    N = 3
    u = 1.1
    sigma = np.log(u)/np.sqrt(T)
    model = BinomialModel(N, S, K, r, T, sigma)
    result = model.calculate()
    print(result)
    