from flask import Flask
import logging
import os
from src.api.api import api

from src.models.api_production import ApiMode
from src.models.PostgresqlManager import postgresql_manager

logger = logging.getLogger()

app = Flask(__name__)

# REGISTER MULTIPLE ENDPOINTS
app.register_blueprint(api, url_prefix="/api") # host:port/api ···

if __name__ == "__main__":
    apimode = ApiMode.get_instance()
    postmanager = postgresql_manager.get_instance()

    production = os.getenv("FLASK_ENV")
    runner = os.getenv("FLASK_APP")
    logger.info(f'KEY PARAMETERS FLASK_ENV={production} FLASK_APP={runner}')

    if production == "development":
        apimode.set_production(production)
        app.debug = True

    logger.info("STARTING APP")
    app.run()