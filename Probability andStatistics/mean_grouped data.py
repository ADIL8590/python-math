#Mean of grouped data and plot bar graph
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Sample grouped data
data = {
    'Class Interval': ['0-10', '10-20', '20-30', '30-40', '40-50'],
    'Frequency': [5, 15, 25, 10, 5]
}
# Create a DataFrame
df = pd.DataFrame(data)
# Calculate midpoints
df['Midpoint'] = df['Class Interval'].apply(lambda x: (int(x.split('-')[0]) + int(x.split('-')[1])) / 2)
# Calculate mean
mean = np.sum(df['Midpoint'] * df['Frequency']) / np.sum(df['Frequency'])
# Plot bar graph
plt.bar(df['Class Interval'], df['Frequency'], color='skyblue')
plt.xlabel('Class Interval')
plt.ylabel('Frequency')
plt.title('Bar Graph of Grouped Data')
plt.axhline(y=mean, color='r', linestyle='--', label=f'Mean: {mean:.2f}')
plt.legend()
plt.show()
print("The mean of the grouped data is:", mean)
# Display the DataFrame with midpoints
print(df)
#save the DataFrame to a CSV file
df.to_csv('grouped_data_with_midpoints.csv', index=False)
# Display the DataFrame with midpoints
df['Midpoint'] = df['Class Interval'].apply(lambda x: (int(x.split('-')[0]) + int(x.split('-')[1])) / 2)
# Calculate mean
mean = np.sum(df['Midpoint'] * df['Frequency']) / np.sum(df['Frequency'])
print(f'Mean of grouped data: {mean}')
#save graph as image
plt.savefig('grouped_data_bar_graph.png')
