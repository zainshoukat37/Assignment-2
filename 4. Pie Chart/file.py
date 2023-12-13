import pandas as pd
import matplotlib.pyplot as plt

def read_worldbank_data(file_path):
    """
    Read data from an Excel file and return it as a DataFrame.

    Parameters:
    - file_path (str): The path to the Excel file.

    Returns:
    - pd.DataFrame: The DataFrame containing the data from the Excel file.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading data from {file_path}: {str(e)}")
        return None

def extract_data(df, countries, start_year, end_year, year_interval):
    """
    Extract relevant data from a DataFrame based on specified criteria.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - countries (list of str): List of country names to filter the data.
    - start_year (int): The starting year for data extraction.
    - end_year (int): The ending year for data extraction.
    - year_interval (int): The interval between years for data extraction.

    Returns:
    - pd.DataFrame: The extracted data as a DataFrame.
    """
    years = [str(year) for year in range(start_year, end_year + 1, year_interval)]
    filtered_df = df[df['Country Name'].isin(countries)]
    return filtered_df.set_index('Country Name')[years]

def plot_worldbank_data(extracted_data, title, xlabel, ylabel):
    """
    Plot the extracted data as an area plot.

    Parameters:
    - extracted_data (pd.DataFrame): The data to be plotted as a DataFrame.
    - title (str): The title of the plot.
    - xlabel (str): The label for the x-axis.
    - ylabel (str): The label for the y-axis.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    for country in extracted_data.columns:
        ax.fill_between(extracted_data.index, 0, extracted_data[country], label=country, alpha=0.5)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.legend(title='Country', loc='upper left', bbox_to_anchor=(1, 1))

    plt.subplots_adjust(right=0.8)

    plt.show()

def main():
    file_path = "edu.xls"
    countries_list = ["Bangladesh", "Brazil", "Canada", "China", "India", "Nigeria", "Germany", "Singapore", "Sweden", "United Kingdom", "United States"]
    start_year = 2005
    end_year = 2022
    year_interval = 4

    df = read_worldbank_data(file_path)

    if df is not None:
        extracted_data = extract_data(df, countries_list, start_year, end_year, year_interval)

        if extracted_data is not None:
            # Display summary statistics
            print("Summary Statistics of Extracted Data:")
            print(extracted_data.describe())
            
            plot_worldbank_data(extracted_data, 'Education Expenditure% of Countries (2005 to 2021, 4-Year Intervals)', 'Years', 'Values')

if __name__ == "__main__":
    main()
