import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from medical_data_visualizer import *

# Import data from medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# Execute as funções para testar o código
if __name__ == "__main__":
    # Task 1: Add Overweight Column
    print("-------------------overweight----------------")
    df = calculate_overweight(df)

    # Task 2: Normalize Data
    print("-------------------normalize data-----------------")
    df = normalize_data(df)

    print("-------------------clean data-----------------")
    df = clean_data(df)

    # Task 3: Draw Cat Plot
   # draw_cat_plot(df)

    # Task 4: Draw Heat Map
    print("-------------------heat map-----------------")
    df = draw_heat_map(df)
