# importing the modules
import os
import PyPDF2
import pyttsx3
from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if "submitted" in request.form:
        if (os.path.isdir('C:/newdir')):
            a = request.files['filename']
            k=request.form.get('pageno')
            c=int(k)
            global b
            b = secure_filename(str(a))
            b = b.replace("FileStorage_", " ")
            b = b.replace("_application_pdf", " ")
            b = b.replace("\Assignment", "")
            str(b)
            a.save(os.path.join('C:/newdir', b))
            readfile(c)
        else:
            os.mkdir("C:/newdir")
            a = request.files['filename']
            k=request.form.get('pageno')
            c=int(k)
            b = secure_filename(str(a))
            b = b.replace("FileStorage_", " ")
            b = b.replace("_application_pdf", " ")
            b = b.replace("\Assignment", "")
            str(b)
            a.save(os.path.join('C:/newdir', b))
            readfile(c)

    return render_template('home.html')


"""changes- remove the new directory and deploy on heroku"""


def readfile(k):
    f = "C:/newdir/" + b
    path = open(f, 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    from_page = pdfReader.getPage(k)
    text = from_page.extractText()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()


if (__name__) == "__main__":
    app.run(debug=True)