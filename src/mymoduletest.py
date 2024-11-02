import pathlib
import pandas as pd

def main(data_set):
    """
    Summary of Function:
        Produces a string of information given in a dataset.
    Parameteres:
        data_set (csv file): Dataset that includes information
                             for paralympics (dates/location/
                             participant numbers...)
    Returns:
        data_string (str): String containing 'readable' 
                           information.
    """
    csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_events_raw.csv')
    if csv_file.exists():
        print(f"{csv_file} exists.")
    else:
        print(f"{csv_file} does not exist.")

    excel_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_all_raw.xlsx')
    if excel_file.exists():
        print(f"{excel_file} exists.")
    else:
        print(f"{excel_file} does not exist.")

    data_csv = pd.read_csv(csv_file)
    data_excel_events = pd.read_excel(excel_file)
    data_excel_medals = pd.read_excel(excel_file, 1)