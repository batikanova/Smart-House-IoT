from app.services import *
from flask import jsonify, request
from app.schemas.voice import voiceSchema, verifySchema


def voiceVerify():
    try:
        data = request.get_json()
        validatedData = verifySchema().load(data)

        result = voiceVerifyService(validatedData.get("email"))
        if result:
            print("Voice verification process initiated successfully.")
            return jsonify({"status": result, "message": "Voice verification process initiated."}), 200
        else:
            print("Voice verification process failed.")
            return jsonify({"status": result, "message": "Voice verification process failed."}), 400

    except Exception as e:

        print(f"Error during voice verification: {e}")
        return jsonify({"status": False, "message": "Voice verification failed due to an error."}), 500

def saveRefVoice():
    try:

        data = request.get_json()
        print(data)
        validatedData = voiceSchema().load(data)
        result = takeRefVoiceService(validatedData.get("name"), validatedData.get("email"))
        if result:
            return jsonify({"status": result, "message": "Voice Saving process was successful."}), 200
        else:
            return jsonify({"status": result, "message": "Voice Saving process failed."}), 500
    
    except Exception as e:

        print(f"Error during voice saving: {e}")
        return jsonify({"status": False, "message": "Voice saving failed due to an error."}), 500