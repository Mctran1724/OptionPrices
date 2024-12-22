import numpy as np
from scipy.stats import norm
from Option import OptionModel

class MonteCarloModel(OptionModel):

    def __init__(self, M: int, N: int, delta: float = 0,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._N = N #number of time steps
        self._M = M #number of trials
        self._dt = self._T/N
        self._delta = delta
        
        self._nu = (self._r - delta) - self._sigma**2/2
        self._nudt = self._nu * self._dt #save having to recompute every iteration
        self._srdt = self._sigma*np.sqrt(self._dt) #save having to recompute every iteration
        return
    
    #Simulate something happening to the stock price and check resultant aggregate effects in the option price
    def time_step(self, S_t: float) -> float:
        return S_t*np.exp(self._nudt + self._srdt*np.random.normal())
    
    def path(self) -> np.ndarray: #starting from initial stock price, jump forward and set new stock prices.
        result = [self._s]
        for i in range(1, self._N):
            result.append(self.time_step(result[i-1]))
        return np.array(result)
    
    def payoffs(self, path: np.ndarray) -> np.ndarray: #this is the payoff function
        if self._is_call:
            return np.maximum(path - self._K, np.zeros((self._M, self._N)))
        else:
            return np.maximum(self._K - path, np.zeros((self._M, self._N)))
        
    def simulate_stock_prices(self):
        #We take the arithmetic mean of all the payoffs and discount them back 
        #allocate the resulting array
        result = np.zeros((self._M, self._N))
        for i in range(self._M):
            result[i] = self.path()    
        return result

    def simulate_option_payoffs(self):
        #We take the arithmetic mean of all the payoffs and discount them back 
        #allocate the resulting array
        result = np.zeros((self._M, self._N))
        for i in range(self._M):
            result[i] = self.path()
        
        result = self.payoffs(result)
        return result

    def calculate(self):
        option_payoffs = self.simulate_option_payoffs()
        
        C_0 = np.mean(option_payoffs) * np.exp(-self._r * self._T)        

        return C_0

    
    

if __name__=="__main__":
    M = 1000
    N = 10
    S = 101.15
    sigma = 0.0991
    r = 0.01
    delta = 0
    K = 98.01
    T = 0.16438356
    model = MonteCarloModel(M, N, delta, S, K, r, T, sigma)

    print(model.calculate())