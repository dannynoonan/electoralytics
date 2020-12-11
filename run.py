from dash_app import app
import settings

app.run_server(debug=settings.debug, host=settings.host, port=settings.port)
