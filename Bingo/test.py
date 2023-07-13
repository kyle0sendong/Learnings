import pandas as pd
import matplotlib.pyplot as plt


B = [str(i) for i in range(1, 15 + 1)]
I = [str(i) for i in range(16, 30 + 1)]
N = [str(i) for i in range(31, 45 + 1)]
G = [str(i) for i in range(46, 60 + 1)]
O = [str(i) for i in range(61, 75 + 1)]
b_df = pd.read_csv('data.csv', usecols=B)
i_df = pd.read_csv('data.csv', usecols=I)
n_df = pd.read_csv('data.csv', usecols=N)
g_df = pd.read_csv('data.csv', usecols=G)
o_df = pd.read_csv('data.csv', usecols=O)

num_columns = len(b_df)
num_rows = 75

# Test Bingo Patterns

# Count values
column_frequencies = o_df.apply(pd.Series.value_counts)
ax = column_frequencies.plot(kind='bar')

# Add text labels to each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center',
                xytext=(0, 5), textcoords='offset points')

# Customize the plot
plt.xlabel('Column Values')
plt.ylabel('Frequency')
plt.title('Frequency of Values in Each Column')
plt.legend(title='Columns')

plt.show()
