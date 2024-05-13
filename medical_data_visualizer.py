import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#from medical_data_visualizer import calculate_overweight, normalize_data, draw_cat_plot, draw_heat_map  

# Load the data from the CSV file (assuming it's in the same directory)
df = pd.read_csv('medical_examination.csv')

def calculate_overweight(df):

  df['bmi'] = df['weight'] / (df['height']**2)
  df['overweight'] = (df['bmi'] > 25).astype(int)
  return df

# Print the result from def calculate_overweight(df)
print("-------------------overheight-----------------")
print(calculate_overweight(df))

def normalize_data(df):
  # Normalize cholesterol and gluc columns
  df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
  df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

  return df
# Print the result from def normalize_data(df)
print("-------------------normalize data-----------------")
print(normalize_data(df))
"""""
def draw_cat_plot(df):
  # Normalize data
  df = normalize_data(df)

  # Convert data into long format
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                   var_name='variable', value_name='value')

  # Group and reformat the data
  df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()

  # Plot
  fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

  return fig
  """""
# Print the result from def draw_cat_plot()
#print(draw_cat_plot(df))

def clean_data(df):
# Filter out incorrect data
  df = df[(df['ap_lo'] <= df['ap_hi']) &                      # Diastolic pressure <= Systolic pressure
        (df['height'] >= df['height'].quantile(0.025)) &   # Height >= 2.5th percentile
        (df['height'] <= df['height'].quantile(0.975)) &   # Height <= 97.5th percentile
        (df['weight'] >= df['weight'].quantile(0.025)) &   # Weight >= 2.5th percentile
        (df['weight'] <= df['weight'].quantile(0.975))]   # Weight <= 97.5th percentile

  return df
print("-------------------clean data-----------------")
print(clean_data(df))

def draw_heat_map(df):
  # Clean the data
  df = clean_data(df)

  # Calculate the correlation matrix
  corr = df.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(corr, dtype=bool))

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(12, 10))

  # Plot the correlation matrix using seaborn's heatmap
  sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True, linewidths=.5, ax=ax)

  # Show the plot
  plt.show()

  return fig

print("-------------------heat map-----------------")
print(draw_heat_map(df))

