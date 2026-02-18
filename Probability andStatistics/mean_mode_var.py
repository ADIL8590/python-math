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
# Print the mean
print(f'Mean of the grouped data: {mean:.2f}')
# Calculate median
cumulative_frequency = np.cumsum(df['Frequency'])
median_class_index = np.where(cumulative_frequency >= np.sum(df['Frequency']) / 2)[0][0]
L = int(df['Class Interval'][median_class_index].split('-')[0])
F = cumulative_frequency[median_class_index - 1] if median_class_index > 0 else 0
f = df['Frequency'][median_class_index]
h = int(df['Class Interval'][median_class_index].split('-')[1]) - L
median = L + ((np.sum(df['Frequency']) / 2 - F) / f) * h
# Print the median
print(f'Median of the grouped data: {median:.2f}')
# Calculate mode
modal_class_index = np.argmax(df['Frequency'])
L = int(df['Class Interval'][modal_class_index].split('-')[0])
f1 = df['Frequency'][modal_class_index]
f0 = df['Frequency'][modal_class_index - 1] if modal_class_index > 0 else 0
f2 = df['Frequency'][modal_class_index + 1] if modal_class_index < len(df) - 1 else 0
h = int(df['Class Interval'][modal_class_index].split('-')[1]) - L
mode = L + (f1 - f0) / ((f1 - f0) + (f1 - f2)) * h
# Print the mode
print(f'Mode of the grouped data: {mode:.2f}')
# Calculate standard deviation
mean_array = np.repeat(df['Midpoint'], df['Frequency'])
std_dev = np.std(mean_array, ddof=1)
# Print the standard deviation
print(f'Standard deviation of the grouped data: {std_dev:.2f}')
# Calculate variance
variance = std_dev ** 2
# Print the variance
print(f'Variance of the grouped data: {variance:.2f}')
# Calculate coefficient of variation
coefficient_of_variation = (std_dev / mean) * 100
# Print the coefficient of variation
print(f'Coefficient of Variation of the grouped data: {coefficient_of_variation:.2f}%')
# Display the DataFrame with midpoints
print(df)
#save the DataFrame to a CSV file
df.to_csv('grouped_data_with_midpoints.csv', index=False)
#save graph
plt.savefig('bar_graph.png')
