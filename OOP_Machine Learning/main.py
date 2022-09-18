from data import *
import pandas as pd

def main(model_type: str, data: str or pd.DataFrame):
    if model_type == 'Linear':
        ml_object = Linear(data = data)
    
if __name__ == '__main__':
    main(model_type = 'Linear', data = f"C:/Users/secre/Downloads/world_population.csv") 