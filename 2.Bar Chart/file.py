import pandas as pd
import matplotlib.pyplot as plt

# Function to read data from the Excel file
def read_worldbank_data(file_path):
    """
    Read data from an Excel file and return it as a DataFrame.

    Parameters:
    file_path (str): The path to the Excel file.

    Returns:
    pd.DataFrame: The DataFrame containing the data from the Excel file.
    """
    df = pd.read_excel(file_path)
    return df

# Function to extract relevant data for plotting
def extract_data(df, countries, start_year, end_year, year_interval):
    """
    Extract relevant data from a DataFrame based on specified criteria.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    countries (list of str): List of country names to filter the data.
    start_year (int): The starting year for data extraction.
    end_year (int): The ending year for data extraction.
    year_interval (int): The interval between years for data extraction.

    Returns:
    pd.DataFrame: The extracted data as a DataFrame.
    """
    # Create a list of years within the specified range and interval
    years = [str(year) for year in range(start_year, end_year + 1, year_interval)]

    # Filter the DataFrame for the specified countries
    filtered_df = df[df['Country Name'].isin(countries)]

    # Set the index to 'Country Name' and select the relevant years
    return filtered_df.set_index('Country Name')[years]

# Function to plot the extracted data
def plot_worldbank_data(extracted_data, title, xlabel, ylabel):
    """
    Plot data from a DataFrame as a bar graph.

    Parameters:
    extracted_data (pd.DataFrame): The data to be plotted as a DataFrame.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """
    # Plot the bar graph
    ax = extracted_data.plot(kind='bar', stacked=False, rot=0)

    # Set plot title, x-axis label, and y-axis label
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Show the legends
    ax.legend(title='Years', loc='upper right')

    # Show the plot
    plt.show()

# Main function
def main():
    # File path and input parameters
    file_path = "trade.xls"
    countries_list = ["Bangladesh", "Brazil", "Canada", "China", "India", "Nigeria", "Germany", "Singapore", "Sweden", "United Kingdom", "United States"]
    start_year = 2002
    end_year = 2022
    year_interval = 5

    # Read the data from the World Bank file
    df = read_worldbank_data(file_path)
    
    # Check if the DataFrame is not empty
    if df is not None:
        # Extract relevant data
        extracted_data = extract_data(df, countries_list, start_year, end_year, year_interval)
        
        # Check if the extracted data is not empty
        if extracted_data is not None:
            # Display summary statistics
            print("Summary Statistics of Extracted Data:")
            print(extracted_data.describe())
            
            # Plot the extracted data
            plot_worldbank_data(extracted_data, 'Trade (% of GDP) of Countries (2002 to 2022, 5-Year Intervals)', 'Countries', 'Values')

# Execute the main function
if __name__ == "__main__":
    main()
