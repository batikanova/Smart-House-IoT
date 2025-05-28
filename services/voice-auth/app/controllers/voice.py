from app.services import *
from flask import jsonify

def voiceAuthenticate():
    try:
        result = voiceAuthenticateService()
        return jsonify({"status": result, "message": "Voice authentication process initiated."}), 200
    except Exception as e:
        print(f"Error during voice authentication: {e}")
        return jsonify({"status": False, "message": "Voice authentication failed due to an error."}), 500

def saveRefVoice():
    try:
        result = takeRefVoiceService()
        return jsonify({"status": result, "message": "Voice Saving process was successful."}), 200
    except Exception as e:
        print(f"Error during voice saving: {e}")
        return jsonify({"status": False, "message": "Voice saving failed due to an error."}), 500