import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
from matplotlib import style
style.use('ggplot')

def draw_plot():
    # Read data from file
    sea_data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = sea_data['Year']
    y = sea_data['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(15,10))
    ax = plt.scatter(x,y)

    # Create first line of best fit
    data = linregress(x,y)
    slope = data.slope
    intercept = data.intercept
    regression_line_1 = (slope*np.arange(sea_data['Year'][0],2051) + intercept)
    x_1 = np.arange(sea_data['Year'][0],2051)
    ax = plt.plot(x_1, regression_line_1)

    # Create second line of best fit
    sea_data_c = sea_data[(sea_data['Year']>=2000)]
    x1 = sea_data_c['Year']
    y1 = sea_data_c['CSIRO Adjusted Sea Level']
    data_n = linregress(x1,y1)
    slope_n = data_n.slope
    intercept_n = data_n.intercept
    regression_line2 = (slope_n*np.arange(2000,2051))+intercept_n
    x_new = np.arange(2000,2051)

    ax = plt.plot(x_new, regression_line2)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return plt.gca()