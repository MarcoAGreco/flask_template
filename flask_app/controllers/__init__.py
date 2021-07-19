import logging
from flask import Blueprint, current_app
import os
from controllers.main_controller import root, post_root

app_blueprint = Blueprint('comparator', 'api')

app_blueprint.add_url_rule('/', view_func=root, methods=['GET'])
app_blueprint.add_url_rule('/', view_func=post_root, methods=['POST'])
