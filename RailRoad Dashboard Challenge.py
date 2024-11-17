import pandas as pd
from datetime import datetime
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load dataset
railway_data = pd.read_csv(r'C:\Users\kyleh\OneDrive\Desktop\PowerBI Dashboards\UK+Train+Rides\railway.csv')
railway_data['Date of Purchase'] = pd.to_datetime(railway_data['Date of Purchase'], errors='coerce')
railway_data['Date of Journey'] = pd.to_datetime(railway_data['Date of Journey'], errors='coerce')
railway_data['Reason for Delay'] = railway_data['Reason for Delay'].fillna('No Delay')
railway_data['Railcard'] = railway_data['Railcard'].fillna('None')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H2("Filter by Date of Journey"),
        dcc.DatePickerRange(
            id='date-picker',
            start_date=railway_data['Date of Journey'].min(),
            end_date=railway_data['Date of Journey'].max(),
            display_format='YYYY-MM-DD'
        )
    ], style={'width': '20%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '20px'}),
    html.Div([
        html.Div(dcc.Graph(id='bar-chart-departure-stations'), style={'width': '33%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='pie-chart-ticket-classes'), style={'width': '33%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='line-chart-ticket-price'), style={'width': '33%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='heatmap-delay-reasons'), style={'width': '33%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='scatter-ticket-price-time'), style={'width': '33%', 'display': 'inline-block'}),
        html.Div(dcc.Graph(id='stacked-bar-payment-method'), style={'width': '33%', 'display': 'inline-block'})
    ], style={'width': '75%', 'display': 'inline-block'})
])

@app.callback(
    [
        Output('bar-chart-departure-stations', 'figure'),
        Output('pie-chart-ticket-classes', 'figure'),
        Output('line-chart-ticket-price', 'figure'),
        Output('heatmap-delay-reasons', 'figure'),
        Output('scatter-ticket-price-time', 'figure'),
        Output('stacked-bar-payment-method', 'figure')
    ],
    [Input('date-picker', 'start_date'), Input('date-picker', 'end_date')]
)
def update_visualizations(start_date, end_date):
    filtered_data = railway_data[
        (railway_data['Date of Journey'] >= pd.to_datetime(start_date)) &
        (railway_data['Date of Journey'] <= pd.to_datetime(end_date))
    ]

    bar_chart = px.bar(
        filtered_data.groupby('Departure Station').size().reset_index(name='Journeys'),
        x='Departure Station', y='Journeys', title='Journeys per Departure Station'
    )
    pie_chart = px.pie(
        filtered_data, names='Ticket Class', title='Distribution of Ticket Classes'
    )
    line_chart = px.line(
        filtered_data.groupby('Date of Journey')['Price'].mean().reset_index(),
        x='Date of Journey', y='Price', title='Average Ticket Price Over Time'
    )
    heatmap_data = filtered_data.groupby(['Departure Station', 'Reason for Delay']).size().reset_index(name='Count')
    heatmap = px.density_heatmap(
        heatmap_data, x='Departure Station', y='Reason for Delay', z='Count', title='Reasons for Delay by Station'
    )
    filtered_data['Journey Time'] = (
        pd.to_datetime(filtered_data['Arrival Time'], errors='coerce') -
        pd.to_datetime(filtered_data['Departure Time'], errors='coerce')
    ).dt.total_seconds() / 60
    scatter_plot = px.scatter(
        filtered_data, x='Journey Time', y='Price', title='Ticket Price vs. Journey Time (Minutes)'
    )
    stacked_bar = px.bar(
        filtered_data.groupby(['Payment Method', 'Ticket Type']).size().reset_index(name='Count'),
        x='Payment Method', y='Count', color='Ticket Type', title='Payment Method Usage by Ticket Type'
    )

    return bar_chart, pie_chart, line_chart, heatmap, scatter_plot, stacked_bar

if __name__ == '__main__':
    app.run_server(debug=True)
