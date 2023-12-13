import pandas as pd
import matplotlib.pyplot as plt

# Function to read data from the Excel file
def read_worldbank_data(file_path):
    """
    Reads data from the World Bank Excel file.

    Parameters:
    - file_path (str): The path to the Excel file.

    Returns:
    - pd.DataFrame: The loaded DataFrame.
    """
    df = pd.read_excel(file_path)
    return df

# Function to extract relevant data for plotting
def extract_data(df, countries, start_year, end_year, year_interval):
    """
    Extracts relevant data for plotting.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - countries (list): List of country names.
    - start_year (int): Start year for data extraction.
    - end_year (int): End year for data extraction.
    - year_interval (int): Interval between years.

    Returns:
    - pd.DataFrame: Extracted data with countries as index and selected years as columns.
    """
    years = [str(year) for year in range(start_year, end_year + 1, year_interval)]
    filtered_df = df[df['Country Name'].isin(countries)]
    extracted_data = filtered_df.set_index('Country Name')[years]
    return extracted_data

# Function to plot the extracted data
def plot_worldbank_data(extracted_data, title, xlabel, ylabel):
    """
    Plots the extracted World Bank data.

    Parameters:
    - extracted_data (pd.DataFrame): The data to be plotted.
    - title (str): Title of the plot.
    - xlabel (str): Label for the x-axis.
    - ylabel (str): Label for the y-axis.
    """
    # Plot the bar graph
    ax = extracted_data.plot(kind='bar', stacked=False, rot=0)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Show the legends
    ax.legend(title='Years', loc='upper right')

    # Show the plot
    plt.show()

# Main function
def main():
    # Input parameters
    file_path = "industry.xls"
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
            plot_worldbank_data(extracted_data, 'Industrial Growth% of Countries (2002 to 2022, 5-Year Intervals)', 'Countries', 'Values')

# Execute the main function
if __name__ == "__main__":
    main()
