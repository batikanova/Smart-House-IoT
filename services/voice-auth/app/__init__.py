from flask import Flask, Response
import json
from .routes import registerRoutes

def createApp():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        homeInfo = {
            "status": "success",
            "message": "Welcome to the Smart House Voice Authentication application!",
            "routes": {
                "/": "Home route",
                "/voice": "Voice API route",
                "/voice/auth": "Voice authentication endpoint"
            }
            }
        homeInfo = json.dumps(homeInfo, indent=4)
        return Response(homeInfo, mimetype='application/json'), 200
    
    # Blueprintleri kaydet
    registerRoutes(app)

    

    return app
