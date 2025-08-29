import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    dt = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(dt['Year'], dt['CSIRO Adjusted Sea Level'], color='blue', s=10)

    
    # Create first line of best fit
    
    years_extended = range(dt['Year'].min(), 2051) 
    
    slope, intercept, r_value, p_value, std_err = linregress(dt['Year'], dt['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, intercept + slope * years_extended, 'r')

    # Create second line of best fit
    
    new_years_extended = range(2000, 2051)
    
    dt_recent = dt[dt['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(dt_recent['Year'], dt_recent['CSIRO Adjusted Sea Level'])
    plt.plot(new_years_extended, intercept_recent + slope_recent * new_years_extended, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()