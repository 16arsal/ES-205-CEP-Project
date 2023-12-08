# Importing pandas library for data manipulation
import pandas as pd

# Function to load data from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

def explore_data(data_frame):
    print("Dataset Summary:")
    print(data_frame.describe())

    print("\nFirst Few Rows:")
    print(data_frame.head())

    print("\nMissing Values:")
    print(data_frame.isnull().sum())

def handle_missing_data(data_frame, strategy='drop'):
    if strategy == 'drop':
        return data_frame.dropna()
    elif strategy == 'impute_mean':
        return data_frame.fillna(data_frame.mean())
    # Add more strategies as needed

def select_features(data_frame):
    selected_features = ['close', 'volume']
    return data_frame[selected_features + ['date']]

if __name__ == "__main__":
    # Use the specified file path
    file_path = r'C:\Users\ahmed\Downloads\all_stocks_5yr.csv'

    # Load data
    df = load_data(file_path)
    
    # Explore data
    explore_data(df)
    
    # Choose a strategy for handling missing data
    missing_data_strategy = input("Choose a strategy for handling missing data (drop/impute_mean): ")
    df = handle_missing_data(df, strategy=missing_data_strategy)
    
    # Select features for linear regression
    df_linear_regression = select_features(df)
    
    # Display modified DataFrame
    print("\nSelected Features for Linear Regression:")
    print(df_linear_regression.head())
