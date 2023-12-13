import pandas as pd
import matplotlib.pyplot as plt

# Function to read data from the Excel file
def read_worldbank_data(file_path):
    """
    Read data from the given Excel file and return it as a DataFrame.

    Args:
        file_path (str): The file path of the Excel file.

    Returns:
        pandas.DataFrame: The DataFrame containing the data.
    """
    df = pd.read_excel(file_path)
    return df

# Function to extract relevant data for plotting
def extract_data(df, countries, start_year, end_year, year_interval):
    """
    Extract relevant data from the DataFrame for specified countries and years.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        countries (list): List of country names to filter the data.
        start_year (int): The start year for the data extraction.
        end_year (int): The end year for the data extraction.
        year_interval (int): The interval between years.

    Returns:
        pandas.DataFrame: The extracted data as a DataFrame.
    """
    # Create a list of years within the specified range and interval
    years = [str(year) for year in range(start_year, end_year + 1, year_interval)]

    # Filter the DataFrame for the specified countries
    filtered_df = df[df['Country Name'].isin(countries)]

    # Set the index to 'Country Name' and select the relevant years
    return filtered_df.set_index('Country Name')[years]

# Function to plot the extracted data as a line graph
def plot_worldbank_data(extracted_data, title, xlabel, ylabel):
    """
    Plot the extracted data as a line graph.

    Args:
        extracted_data (pandas.DataFrame): The data to be plotted as a DataFrame.
        title (str): The title of the plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
    """
    # Set the figure size
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the line graph with dotted lines
    extracted_data.T.plot(kind='line', linestyle='dashdot', ax=ax)

    # Set plot title, x-axis label, and y-axis label
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Move the legend outside the graph and adjust its position
    ax.legend(title='Country', loc='upper left', bbox_to_anchor=(1, 1))

    # Adjust the layout to shift the plot to the left
    plt.subplots_adjust(right=0.8)

    # Show the plot
    plt.show()

# Main function
def main():
    # File path and input parameters
    file_path = "population.xls"
    countries_list = ["Bangladesh", "Brazil", "Canada", "China", "India", "Nigeria", "Russia", "South Africa", "Sweden", "United Kingdom", "United States"]
    start_year = 1970
    end_year = 2020
    year_interval = 10

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
            
            # Plot the extracted data as a line graph
            plot_worldbank_data(extracted_data, 'Population Annual Growth% (1970 to 2020, 10-Year Intervals)', 'Years', 'Values')

# Execute the main function
if __name__ == "__main__":
    main()
