import matplotlib.pyplot as plt
import numpy as np

class const:
    #const
    R = 0.0820573660809596

class Ideal_gas_equation:
    #functions
    def volumegraph(
            n: float = 1,
            T: float = 270,
            max_volumes: float = 1,
            save_graph: bool = False,
            save_path: str = "graph.png"
            ):
        v = np.arange(0.01,max_volumes,0.01)
        R = const.R
        #make & show graph
        plt.plot(v,(n*R*T)/v)
        plt.xlabel("Volume (L)",loc='center')
        plt.ylabel("Pressure (atm)",loc= 'center')
        if(save_graph):
            plt.savefig(save_path)
        plt.show()
        
    

n = float(input("Mol : "))
T = float(input("Temperture(K) : "))
v_max = float(input("Max Volume(L) : "))
Ideal_gas_equation.volumegraph(n=n,T=T,max_volumes=v_max,save_graph=True,save_path = "graph.png")