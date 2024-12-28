import streamlit as st
import pandas as pd
import plotly.express as px
fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))

# Load the preprocessed data
@st.cache_data  # Updated caching method
def load_data():
    # Replace with the path to your CSV file containing the processed data
    data = pd.read_csv(r"C:\Users\Hp\OneDrive\Documents\Minor_project\sample_articles_dataset.xls")
    return data

# Function to create a pie chart for sentiment distribution
def plot_sentiment_distribution(data):
    sentiment_counts = data['Sentiment'].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Count']
    fig = px.pie(
        sentiment_counts,
        names='Sentiment',
        values='Count',
        title="Sentiment Distribution"
    )
    st.plotly_chart(fig)

# Function to create a bar chart for top keywords
def plot_top_keywords(data):
    keywords_series = data['Top Keywords'].str.split(", ").explode()
    top_keywords = keywords_series.value_counts().reset_index()
    top_keywords.columns = ['Keyword', 'Count']
    fig = px.bar(
        top_keywords.head(10),
        x='Keyword',
        y='Count',
        title="Top Keywords in Articles",
        labels={'Keyword': 'Keyword', 'Count': 'Frequency'}
    )
    st.plotly_chart(fig)

# Function to create a pie chart for article categories
def plot_article_categories(data):
    category_counts = data['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']
    fig = px.pie(
        category_counts,
        names='Category',
        values='Count',
        title="Distribution of Articles by Category"
    )
    st.plotly_chart(fig)

# Function to create a pie chart for articles by language
def plot_articles_by_language(data):
    language_counts = data['Language'].value_counts().reset_index()
    language_counts.columns = ['Language', 'Count']
    fig = px.pie(
        language_counts,
        names='Language',
        values='Count',
        title="Distribution of Articles by Language"
    )
    st.plotly_chart(fig)

# Function to create a bar chart for articles by category and sentiment
def plot_articles_by_category_and_sentiment(data):
    category_sentiment = data.groupby(['Category', 'Sentiment']).size().reset_index(name='Count')
    fig = px.bar(
        category_sentiment,
        x='Category',
        y='Count',
        color='Sentiment',
        title="Articles by Category and Sentiment",
        labels={'Category': 'Category', 'Count': 'Count'}
    )
    st.plotly_chart(fig)

# Function to create a bar chart for articles by language and sentiment
def plot_articles_by_language_and_sentiment(data):
    language_sentiment = data.groupby(['Language', 'Sentiment']).size().reset_index(name='Count')
    fig = px.bar(
        language_sentiment,
        x='Language',
        y='Count',
        color='Sentiment',
        title="Articles by Language and Sentiment",
        labels={'Language': 'Language', 'Count': 'Count'}
    )
    st.plotly_chart(fig)

# Streamlit App Layout
def main():
    st.title("News Sentiment Analysis Dashboard")
    
    # Sidebar for user inputs
    st.sidebar.title("Options")
    view_option = st.sidebar.selectbox("Select Visualization", [
        "Sentiment Distribution",
        "Top Keywords",
        "Article Categories",
        "Articles by Language",
        "Articles by Category and Sentiment",
        "Articles by Language and Sentiment"
    ])
    
    # Load the data
    data = load_data()

    # Display the selected visualization
    if view_option == "Sentiment Distribution":
        plot_sentiment_distribution(data)
    elif view_option == "Top Keywords":
        plot_top_keywords(data)
    elif view_option == "Article Categories":
        plot_article_categories(data)
    elif view_option == "Articles by Language":
        plot_articles_by_language(data)
    elif view_option == "Articles by Category and Sentiment":
        plot_articles_by_category_and_sentiment(data)
    elif view_option == "Articles by Language and Sentiment":
        plot_articles_by_language_and_sentiment(data)

    # Option to show raw data
    if st.sidebar.checkbox("Show Raw Data"):
        st.subheader("Raw Data")
        st.dataframe(data)

if __name__ == "__main__":
    main()
