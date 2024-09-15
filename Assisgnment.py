# Import necessary libraries
import pandas as pd

# Sample dataset
data = {
    'CustomerID': [1, 2, 3, 3, 4],
    'Name': ['John Doe', 'Jane Smith', 'Mike Ross', 'Mike Ross', 'Rachel Z'],
    'Age': [28, None, 32, 32, 27],
    'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
    'PurchaseAmount': [500, None, 200, 200, 450],
    'City': ['New York', 'Chicago', None, None, 'Los Angeles']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the original data
print("Original Data:")
print(df)

# Step 1: Remove duplicate records
df = df.drop_duplicates()

# Step 2: Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Filling missing Age with the mean
df['PurchaseAmount'].fillna(df['PurchaseAmount'].median(), inplace=True)  # Filling missing PurchaseAmount with the median
df['City'].fillna('Unknown', inplace=True)  # Filling missing City with 'Unknown'

# Step 3: Correct data types if necessary (for this example, all types are correct)

# Step 4: Detect outliers (if necessary)
# Outliers detection (simplified for this example)
q1 = df['PurchaseAmount'].quantile(0.25)
q3 = df['PurchaseAmount'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Removing outliers (in this case none, but code is here to demonstrate)
df = df[(df['PurchaseAmount'] >= lower_bound) & (df['PurchaseAmount'] <= upper_bound)]

# Display cleaned data
print("\nCleaned Data:")
print(df)

# Save the cleaned data to a CSV file (optional)
df.to_csv('cleaned_data.csv', index=False)
