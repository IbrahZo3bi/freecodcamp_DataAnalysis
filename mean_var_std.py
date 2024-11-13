
import numpy as np

def calculate(l):
    

    if len(l)!=9:
  
        raise ValueError('List must contain nine numbers.')
    
        return("List must contain nine numbers.")
    
    dic={"mean":[],
         "variance":[],
         "standard deviation":[],
         "max":[],
         "min":[],
         "sum":[],
         }
    
    l=np.reshape(l,(3,3))
    dic['mean']=[np.mean(l,axis=0).tolist(),np.mean(l,axis=1).tolist(),np.mean(l).tolist()]
    dic['variance']=[np.var(l,axis=0).tolist(),np.var(l,axis=1).tolist(),np.var(l).tolist()]
    dic["standard deviation"]=[np.std(l,axis=0).tolist(),np.std(l,axis=1).tolist(),np.std(l).tolist()]
    dic['max']=[np.max(l,axis=0).tolist(),np.max(l,axis=1).tolist(),np.max(l).tolist()]
    dic['min']=[np.min(l,axis=0).tolist(),np.min(l,axis=1).tolist(),np.min(l).tolist()]
    dic['sum']=[np.sum(l,axis=0).tolist(),np.sum(l,axis=1).tolist(),np.sum(l).tolist()]
    return dic
    

