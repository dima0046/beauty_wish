#!/bin/sh
export FLASK_APP=webapp.py && export FLASK_DEBUG=1  && export TEMPLATES_AUTO_RELOAD=1 && flask run