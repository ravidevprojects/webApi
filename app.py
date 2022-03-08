import configparser
from flask import Flask
from flask_cors import CORS, cross_origin

# Importing blueprint for ping details api
from api.api_getuserinfo.getuserinfo import userinfo_blueprint
# Importing blueprint for logger initilization api
from api.api_initialize_logger.initialize_log import logger_blueprint
# Importing blueprint for all APIs
# from api.api_customsearch.search import search_blueprint
# from api.api_jet_tool.jettool import jettool_blueprint
# from api.api_wipnotes.wipnotes import wipnotes_blueprint
from api.api_tracing.tracing import tracing_blueprint
# from api.api_pons_tool.ponstool import ponstool_blueprint
# from api.api_delineationprint.delineationprint import delineationprint_blueprint
# from api.api_zip_pdf.zip import zip_blueprint
# from api.api_generation_info.generation import generation_blueprint
from api.api_tlm.tlm import tlm_blueprint
from api.api_settings.settings import settings_blueprint
# from api.api_editpole.editpole import editpole_blueprint
# from api.api_generation_feeder.feedergeneration import feedergeneration_blueprint
# from api.api_wiptool.wiptool import wiptool_blueprint
# from api.api_showloadinginformation.showloadinginformation import showloadinginformation_blueprint
# from api.api_bookmark.bookmark import bookmark_blueprint
# from api.api_cit.cit import cit_blueprint
# from api.api_fieldsequence.fieldsequence import sequence_blueprint
# from api.api_favorites.favorites import favorites_blueprint
# from api.api_preferences.preferences import preferences_blueprint
from api.api_adgroup.adgroup import adgroup_blueprint

# Importing logger module
from logger.centralized_logger import CentralizedLogger

# Reading logging.ini file for logger
config = configparser.ConfigParser()
config.read(r'logger/logging.ini')
log_path = config.get('output', 'log_path')
# Initializing logger with the name 'root' and log path
CentralizedLogger().custom_logger('root', log_path)
# Initializing logger with the name 'filter'(for selective users) and log path
CentralizedLogger().filtered_logger('filter', log_path)
# initializing flask
app = Flask(__name__)
CORS(app)

# Registering blueprint for all APIs
app.register_blueprint(userinfo_blueprint)
app.register_blueprint(logger_blueprint)
# app.register_blueprint(search_blueprint)
# app.register_blueprint(jettool_blueprint)
# app.register_blueprint(wipnotes_blueprint)
app.register_blueprint(tracing_blueprint)
# app.register_blueprint(ponstool_blueprint)
# app.register_blueprint(delineationprint_blueprint)
# app.register_blueprint(zip_blueprint)
# app.register_blueprint(generation_blueprint)
app.register_blueprint(tlm_blueprint)
app.register_blueprint(settings_blueprint)
# app.register_blueprint(editpole_blueprint)
# app.register_blueprint(feedergeneration_blueprint)
# app.register_blueprint(wiptool_blueprint)
# app.register_blueprint(showloadinginformation_blueprint)
# app.register_blueprint(bookmark_blueprint)
# app.register_blueprint(cit_blueprint)
# app.register_blueprint(sequence_blueprint)
# app.register_blueprint(favorites_blueprint)
# app.register_blueprint(preferences_blueprint)
app.register_blueprint(adgroup_blueprint)


if __name__ == "__main__":
    # Running the flask
    app.run(debug=True)
