import os
from dash import Dash, html, dcc

# Initialize Dash App (runs on top of Flask)
app = Dash(__name__)
server = app.server  # This is the underlying Flask server for Gunicorn!

# Define UI directly in Python
app.layout = html.Div([
    html.H1("Mein Google Cloud Dash-Dashboard"),
    dcc.Dropdown(options=["Option A", "Option B"], value="Option A"),
    dcc.Graph(
        figure={
            "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Daten"}],
            "layout": {"title": "Beispiel-Diagramm"}
        }
    )
])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)