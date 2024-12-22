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
    
    def option_values(self, path: np.ndarray) -> np.ndarray: #this is the payoff function
        if self._is_call:
            return np.max(path - self._K, 0)
        else:
            return np.max(self._K - path, 0)
        

    
    

if __name__=="__main__":
    M = 100
    N = 10
    S = 100
    sigma = 0.2
    r = 0.06
    delta = 0.03
    K = 100
    T = 1
    model = MonteCarloModel(M, N, delta, S, K, r, T, sigma)

    timesteps = np.linspace(0, T, N)
    prices0 = model.path()

    import matplotlib.pyplot as plt
    plt.plot(timesteps, prices0)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()
    


            