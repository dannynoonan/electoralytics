import os


host = "0.0.0.0"

port = int(os.environ.get("PORT", 8050))

debug = False


## File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"