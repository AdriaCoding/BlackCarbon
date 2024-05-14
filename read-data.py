import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv('BC-Data-Set.csv', sep=';')

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Summary statistics
summary_stats = df.describe()
print("Summary Statistics:")
print(summary_stats)

# Correlation matrix
correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Plot scatter plots for selected variables
plt.figure(figsize=(12, 8))
sns.pairplot(df[['BC', 'N_CPC', 'PM-10', 'PM-2.5', 'PM-1.0']])
plt.title('Scatter Plots')
plt.show()

# Plot temporal trends for selected variables
plt.figure(figsize=(12, 8))
plt.plot(df['date'], df['BC'], label='BC')
plt.plot(df['date'], df['PM-10'], label='PM-10')
plt.plot(df['date'], df['PM-2.5'], label='PM-2.5')
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('Temporal Trends')
plt.legend()
plt.show()
