from flask import Blueprint, Response
from app.controllers.voice import *
import json

voiceBp = Blueprint('voiceBp', __name__)


@voiceBp.route('/', methods=['GET'])
def home():
    routesInfo = {
        "routes": [
            {
                "path": "/voice-auth/auth",
                "method": "POST",
                "parameters":"There is no parameters",
                "description": "Voice authentication endpoint"},     
            {
                "path": "/voice-auth/save",
                "method": "POST",
                "parameters":"There is no parameters",
                "description": "Voice saving endpoint"}]
        }
    routesInfo = json.dumps(routesInfo, indent=4)
    return Response(routesInfo, status=200, mimetype='application/json')

@voiceBp.route('/verify', methods=['POST'])
def voiceVerifyRoute():
    return voiceVerify()

@voiceBp.route('/save', methods=['POST'])
def voiceSave():
    return saveRefVoice()