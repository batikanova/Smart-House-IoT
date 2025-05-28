from .voice import voiceBp


def registerRoutes(app):
    app.register_blueprint(voiceBp, url_prefix='/voice')