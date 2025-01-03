import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the Excel file
data_file = 'All_Data.xlsx'
steps_data = pd.read_excel(data_file, sheet_name='Step Count', parse_dates=['Date'], names=['Date', 'Steps'])
contents_data = pd.read_excel(data_file, sheet_name='Contents', parse_dates=['Transaction Date'],
                              names=['Transaction Date', 'Content Type'])

# Sort and set index for convenience
steps_data = steps_data.sort_values('Date').set_index('Date')
contents_data = contents_data.sort_values('Transaction Date')

# Combine multiple transactions on the same day into a single entry
combined_contents = contents_data.groupby('Transaction Date')['Content Type'].apply(
    lambda x: ' + '.join(sorted(set(x)))).reset_index()

# Compute overall average step count
average_step_count = steps_data['Steps'].mean()


# Define a function to calculate post-transaction metrics
def calculate_step_changes(transaction_date, window=4):
    post_window = steps_data.loc[transaction_date + pd.Timedelta(days=1): transaction_date + pd.Timedelta(days=window)]
    post_avg = post_window['Steps'].mean()
    change = post_avg - average_step_count
    return average_step_count, post_avg, change


# Apply the function to all transactions
results = []
post_transaction_changes = []
post_transaction_avgs = []
for _, row in combined_contents.iterrows():
    transaction_date = row['Transaction Date']
    content_type = row['Content Type']

    general_avg, post_avg, change = calculate_step_changes(transaction_date)
    results.append({
        'Transaction Date': transaction_date,
        'Content Type': content_type,
        'General Avg': general_avg,
        'Post-Transaction Avg': post_avg,
        'Change in Step Count': change
    })
    post_transaction_changes.append(change)
    post_transaction_avgs.append(post_avg)

# Calculate the overall average of post-purchase days' steps
overall_post_avg = sum(post_transaction_avgs) / len(post_transaction_avgs)

# Create a DataFrame for results
results_df = pd.DataFrame(results)

# Save results to a new Excel file
results_df.to_excel('Step_Count_Analysis.xlsx', index=False)


# Print summary metrics
print(f"Overall Average Step Count: {average_step_count:.2f}")
print(f"Overall Post-Purchase Average Step Count: {overall_post_avg:.2f}")
print(results_df)

# Visualization
sns.set(style="whitegrid")

# Bar plot for Post-Transaction Averages with Overall Average as a line
plt.figure(figsize=(12, 6))
plt.bar(results_df['Transaction Date'].dt.strftime('%Y-%m-%d'), results_df['Post-Transaction Avg'], color='skyblue',
        label='Post-Transaction Avg')
plt.axhline(average_step_count, color='red', linestyle='--', label=f'General Avg: {average_step_count:.2f}')
plt.title('Post-Transaction Step Counts with General Average')
plt.xlabel('Transaction Date')
plt.ylabel('Steps')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('bar_plot_with_average_line.png')
plt.show()

# Scatter plot for Step Count Change
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Transaction Date', y='Change in Step Count', hue='Content Type', data=results_df, palette='viridis',
                s=100)
plt.axhline(0, color='red', linestyle='--')
plt.title('Change in Step Count After Transactions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.show()

# Histogram of Step Count Changes
plt.figure(figsize=(10, 5))
sns.histplot(results_df['Change in Step Count'], bins=10, kde=True, color='blue')
plt.title('Distribution of Step Count Changes')
plt.xlabel('Change in Step Count')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histogram.png')
plt.show()


# Perform a t-test on the 'Change in Step Count'
t_stat, p_value = stats.ttest_1samp(results_df['Change in Step Count'], 0)

# Print t-statistic and p-value
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpretation based on p-value
alpha = 0.05  # Significance level (5%)
if p_value < alpha:
    print("Reject the null hypothesis: The transaction has a significant effect on step count.")
else:
    print("Fail to reject the null hypothesis: No significant effect of the transaction on step count.")
