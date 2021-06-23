""" Sample app API """
from flask import Flask

import applib.lib as lib


app = Flask(__name__)


def index():
    even_number = lib.get_even_value()
    html = [
      "<!DOCTYPE html>",
      "<html>",
      "<head>",
      '<meta name="viewport" content="width=device-width, initial-scale=1">',
      "<style>",
      "  .img { margin-top:10%; margin-left: auto; margin-right: auto; display:block; }",
      "  .jumbotron{ padding-top: 10px; padding-bottom: 50px; background-color: #eee; text-align: center; }",
      "</style>",
      "</head>",
      "<body>",
      '<img class="img" src="https://static.wixstatic.com/media/6b0c93_9fdff8df51ee41b8b065887a8b9b472a~mv2.png/v1/fill/w_340,h_78,al_c,q_85,usm_0.66_1.00_0.01/Snip20200629_2_edited_edited.webp" alt="breqwatr">',
      '<br/>',
      '<div class="jumbotron">',
      '<h1>Welcome to Jenkins Demo</h1>',
      '<br/>',
      f'<strong style="color:#337ab7;">Even Number is:&nbsp;</strong> {even_number}',
      '</div></body></html>'
    ]
    return '\n'.join(html)


app.add_url_rule("/", "index", index, methods=["GET"])

