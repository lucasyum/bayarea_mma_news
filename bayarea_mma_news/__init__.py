from flask import Flask

def create_app():       
    app = Flask(__name__)

    from bayarea_mma_news.main.routes import main
    from bayarea_mma_news.errors.handlers import errors    # Importing the instance of that blue print ('errors' blue print')
    from bayarea_mma_news.custom.routes import custom


    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(custom)        

    return app

