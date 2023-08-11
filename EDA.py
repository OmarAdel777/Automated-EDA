import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def load_data(file_path):
    try:
        if file_path.endswith('.CSV'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        elif file_path.endswith('.db'):
            # Load data from SQL database
            # Use appropriate SQL library to connect and fetch data
            data = None
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        print(e)
        return None

    return data

def preprocess_data(data):
    """
    Preprocess the data by identifying the data types of each column, handling missing values,
    encoding categorical features, and scaling numerical features.

    Args:
        data (pd.DataFrame): The data to be preprocessed.

    Returns:
        pd.DataFrame: The preprocessed data.
    """

    column_types = data.dtypes
    
#     print("\n * Your coloumns type would appear here * \n",column_types)

    # Handle missing values
    data = data.dropna()

    # Encode categorical features
    for column in data.columns:
        if column_types[column] == 'object':
             data[column] = data[column].astype('category')


        print("\n * Your coloumns type would appear here * \n",data.info())


    # Scale numerical features
    for column in data.columns:
        if column_types[column] == 'float':
            data[column] = data[column] / data[column].max()

    return data
# Step 3: Feature Selection and Dimensionality Reduction
def feature_selection(data):
    # Perform feature selection techniques
    # Example: Correlation analysis
    correlation_matrix = data.corr()
    selected_features = correlation_matrix[abs(correlation_matrix) > 0.5]

    return selected_features

def create_visualizations(data):
    # Example: Histograms for numerical columns
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    for column in numerical_columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    # Example: Box plots for selected features
    sns.set(style="whitegrid")
    sns.boxplot(data=data)
    plt.xticks(rotation=45)
    plt.show()

    # Example: Pair plots for selected features
    sns.pairplot(data)
    plt.show()  

# Example usage
file_path = input('D:\International_Report_Departures.CSV')
data = load_data(file_path)
preprocessed_data = preprocess_data(data)
data.head()


selected_features = feature_selection(preprocessed_data)

print("Choose an option:")
print("1. Visualize histograms")
print("2. Visualize box plots")
print("3. Visualize pair plots")
choice = int(input("Enter your choice: "))

if choice == 1:
    create_visualizations(preprocessed_data)
elif choice == 2:
    create_visualizations(selected_features)
elif choice == 3:
    create_visualizations(selected_features)

