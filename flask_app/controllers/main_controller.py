from flask import request, render_template, abort
from loguru import logger
import os
import app
from werkzeug.utils import secure_filename

UPLOADS_DIR = "uploads"

def root():
    return render_template('index.html')


def post_root():
    try:
        if len(request.files) > 0:
            uploaded_file = request.files['file']
            logger.info(f"Received a file: {uploaded_file.filename}")

            if uploaded_file.filename.split(".")[-1] not in app.app.config['UPLOAD_EXTENSIONS']:
                abort(400)

            if uploaded_file.filename != '':
                filename = secure_filename(uploaded_file.filename)
                uploaded_file.save(os.path.join(UPLOADS_DIR, filename))
        else:
            return render_template('index.html', errors="EMPTY_FILE")
    except Exception as exc:
        logger.info(f"Error: {str(exc)}")
    finally:
        return render_template('index.html')