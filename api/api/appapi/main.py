""" Sample app API """
from flask import Flask, render_template

import applib.lib as lib


app = Flask(__name__)


def index():
    """index page"""
    even_number = lib.get_even_value()
    return (
        "<h1>Jenkins Demo</h1>\n"
        f"<strong>Even Number:&nbsp;</strong> {even_number}\n"
    )


app.add_url_rule("/", "index", index, methods=["GET"])

