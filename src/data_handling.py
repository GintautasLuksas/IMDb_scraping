import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file with Rate Amount and Group columns
df = pd.read_csv('imdb_movies.csv')
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
df = df.where(pd.notnull(df), None)

def show_other_plots(plot_number):
    if plot_number == 1:
        plt.figure(figsize=(10, 6))
        df['Year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
        plt.title('Number of Movies by Year')
        plt.xlabel('Year')
        plt.ylabel('Number of Movies')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    elif plot_number == 2:
        plt.figure(figsize=(10, 6))
        df['Rating'].plot(kind='hist', bins=20, color='green', alpha=0.7)
        plt.title('Distribution of Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
    elif plot_number == 3:
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Year'], df['Rating'], color='blue', alpha=0.5)
        plt.title('Scatter Plot: Year vs Rating')
        plt.xlabel('Year')
        plt.ylabel('Rating')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    elif plot_number == 4:
        df['Length Category'] = pd.cut(df['Duration (minutes)'], bins=[0, 90, 120, 150, float('inf')],
                                       labels=['Short', 'Medium', 'Long', 'Very Long'])
        plt.figure(figsize=(12, 8))
        sns.violinplot(x='Length Category', y='Rating', data=df, hue='Length Category', palette='viridis', inner='quartile', legend=False)
        plt.title('Rating Distribution by Duration Category')
        plt.xlabel('Duration Category')
        plt.ylabel('Rating')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
    elif plot_number == 5:
        plt.figure(figsize=(10, 6))
        avg_rating_by_year = df.groupby('Year')['Rating'].mean()
        plt.plot(avg_rating_by_year.index, avg_rating_by_year.values, marker='o', linestyle='-', color='orange')
        plt.title('Average Rating by Year')
        plt.xlabel('Year')
        plt.ylabel('Average Rating')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    elif plot_number == 6:
        plt.figure(figsize=(10, 6))
        sns.countplot(x='Group', data=df, palette='Set3', hue='Group', legend=False)
        plt.title('Number of Movies by Group')
        plt.xlabel('Group')
        plt.ylabel('Number of Movies')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
