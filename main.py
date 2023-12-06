import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def explore_data(data_frame):
    print("Dataset Structure:")
    print(data_frame.info())

    print("\nFirst Few Rows:")
    print(data_frame.head())

    print("\nMissing Values:")
    print(data_frame.isnull().sum())

def handle_missing_data(data_frame):
    return data_frame.dropna()

def select_features(data_frame):
    selected_features = ['close', 'volume']
    return data_frame[selected_features + ['date']]

if __name__ == "__main__":
    # Update the file path to your Excel file
    file_path = r'C:\Users\ahmed\Downloads\all_stocks_5yr.csv'
    
    # Load data
    df = load_data(file_path)
    
    # Explore data
    explore_data(df)
    
    # Handle missing data
    df = handle_missing_data(df)
    
    # Select features for linear regression
    df_linear_regression = select_features(df)
    
    # Display modified DataFrame
    print("\nSelected Features for Linear Regression:")
    print(df_linear_regression.head())
