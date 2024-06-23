import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file with Rate Amount and Group columns
df = pd.read_csv('imdb_movies.csv')
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
df = df.where(pd.notnull(df), None)

def show_top_10_movies_by_rating():
    top_10_movies = df.nlargest(10, 'Rating')
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_movies['Title'], top_10_movies['Rating'], color='teal')
    plt.gca().invert_yaxis()
    plt.title('Top 10 Movies by Rating')
    plt.xlabel('Rating')
    plt.ylabel('Movie Title')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()

def show_top_10_movies_by_rating_amount():
    plt.figure(figsize=(10, 6))
    df['Rating Amount'] = df['Rating Amount'].astype(float)
    df.sort_values('Rating Amount', ascending=False, inplace=True)
    plt.barh(df['Title'].head(10), df['Rating Amount'].head(10), color='purple')
    plt.gca().invert_yaxis()
    plt.title('Top 10 Movies by Rating Amount')
    plt.xlabel('Rating Amount')
    plt.ylabel('Movie Title')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()

def show_top_10_movies_by_length():
    top_10_movies = df.nlargest(10, 'Duration (minutes)')
    plt.figure(figsize=(10, 6))
    plt.barh(top_10_movies['Title'], top_10_movies['Duration (minutes)'], color='gold')
    plt.gca().invert_yaxis()
    plt.title('Top 10 Movies by Duration')
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Movie Title')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()

def show_year_vs_rating():
    avg_rating_by_year = df.groupby('Year')['Rating'].mean().dropna()

    plt.figure(figsize=(8, 8))
    plt.plot(avg_rating_by_year.index, avg_rating_by_year.values, marker='o', linestyle='-', color='blue')
    plt.title('Average Rating by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Rating')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def show_year_vs_length():
    avg_length_by_year = df.groupby('Year')['Duration (minutes)'].mean().dropna()

    plt.figure(figsize=(8, 8))
    plt.plot(avg_length_by_year.index, avg_length_by_year.values, marker='o', linestyle='-', color='green')
    plt.title('Average Length by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Length (minutes)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def show_year_vs_rating_amount():
    avg_rating_amount_by_year = df.groupby('Year')['Rating Amount'].mean().dropna()

    plt.figure(figsize=(8, 8))
    plt.plot(avg_rating_amount_by_year.index, avg_rating_amount_by_year.values, marker='o', linestyle='-', color='purple')
    plt.title('Average Rating Amount by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Rating Amount')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

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
        sns.violinplot(x='Length Category', y='Rating', data=df, palette='viridis', inner='quartile')
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
        sns.countplot(x='Group', data=df, palette='Set3')
        plt.title('Number of Movies by Group')
        plt.xlabel('Group')
        plt.ylabel('Number of Movies')
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
