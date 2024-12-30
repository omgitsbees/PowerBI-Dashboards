import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load and clean the dataset
file_path = r'C:\\Users\\kyleh\\OneDrive\\Desktop\\Stock Prices\\Stock Prices.csv'
data = pd.read_csv(file_path)

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Drop rows with missing values in essential columns
data = data.dropna(subset=['open', 'high', 'low', 'close', 'volume'])

# Add calculated columns
data['volatility'] = data['high'] - data['low']
data['day_of_week'] = data['date'].dt.day_name()

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Stock Market Dashboard"),

    # Dropdown for stock selection
    html.Label("Select Stock:"),
    dcc.Dropdown(
        id='stock-dropdown',
        options=[{'label': symbol, 'value': symbol} for symbol in data['symbol'].unique()],
        value=['AMZN'],  # Default value
        multi=True
    ),

    # Slider for date range
    html.Label("Select Date Range:"),
    dcc.DatePickerRange(
        id='date-picker',
        start_date=data['date'].min(),
        end_date=data['date'].max(),
        display_format='YYYY-MM-DD'
    ),

    # Graphs for visualizations
    dcc.Graph(id='volume-chart'),
    dcc.Graph(id='volatility-chart'),
    dcc.Graph(id='day-of-week-chart'),
])

# Callbacks for interactivity
@app.callback(
    [Output('volume-chart', 'figure'),
     Output('volatility-chart', 'figure'),
     Output('day-of-week-chart', 'figure')],
    [Input('stock-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graphs(selected_stocks, start_date, end_date):
    # Filter data
    filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

    if isinstance(selected_stocks, str):  # Handle single selection
        selected_stocks = [selected_stocks]
    filtered_data = filtered_data[filtered_data['symbol'].isin(selected_stocks)]

    # Volume chart
    volume_fig = px.bar(
        filtered_data, x='date', y='volume', color='symbol',
        title="Trading Volume by Date",
        labels={'volume': 'Trading Volume', 'date': 'Date'}
    )

    # Volatility chart
    volatility_fig = px.line(
        filtered_data, x='date', y='volatility', color='symbol',
        title="Daily Volatility (High - Low)",
        labels={'volatility': 'Volatility', 'date': 'Date'}
    )

    # Day of Week Analysis
    day_of_week_fig = px.box(
        filtered_data, x='day_of_week', y='volume', color='symbol',
        title="Trading Volume by Day of the Week",
        labels={'volume': 'Trading Volume', 'day_of_week': 'Day of the Week'}
    )

    return volume_fig, volatility_fig, day_of_week_fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
