import json

from flask import Flask, render_template
from imap_tools import MailBox

app = Flask(__name__)


@app.route('/')
def index():
    data = None
    EMAIL_URL = 'imap.mail.ru'
    EMAIL = "station.mospoly@mail.ru"
    PASSWORD = "Z8yQT7QLMRKnQ8TTnaNL"
    with MailBox(EMAIL_URL).login(EMAIL, PASSWORD, 'inbox') as mailbox:
        for msg in mailbox.fetch(limit=1, reverse=True):
            data = json.loads(msg.text.strip())

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
