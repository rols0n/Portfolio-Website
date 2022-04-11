from flask import Flask, render_template, request
import requests

MORSE_CODE_ALPHABET = {'A':'.- ',
                       'B':'-... ',
                       'C':'-.-. ',
                       'D':'-.. ',
                       'E':'. ',
                       'F':'..-. ',
                       'G':'--. ',
                       'H':'.... ',
                       'I':'.. ',
                       'J':'.--- ',
                       'K':'-.- ',
                       'L':'.-.. ',
                       'M':'-- ',
                       'N':'-. ',
                       'O':'--- ',
                       'P':'.--. ',
                       'Q':'--.- ',
                       'R':'.-. ',
                       'S':'... ',
                       'T':'- ',
                       'U':'..- ',
                       'V':'...- ',
                       'W':'.-- ',
                       'X':'-..- ',
                       'Y':'-.-- ',
                       'Z':'--.. ',
                       '1':'.---- ',
                       '2':'..--- ',
                       '3':'...-- ',
                       '4':'....- ',
                       '5':'..... ',
                       '6':'-.... ',
                       '7':'--... ',
                       '8':'---.. ',
                       '9':'----. ',
                       '0':'----- ',
                       '?':'..--.. ',
                       '!':'-.-.-- ',
                       '.':'.-.-.- ',
                       ',':'--..-- ',
                       ';':'-.-.-. ',
                       ':':'---... ',
                       '+':'.-.-. ',
                       '-':'-....- ',
                       '/':'-..-. ',
                       '=':'-...- ',
                       ' ': '/'}




CODER = ''



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Str-To-Morse-Converter', methods=['GET', 'POST'])
def Str_To_Morce_Converter():
    if request.method == 'POST':
        # request.form.get('entrys')
        CODER = ''
        for entry in request.form.get('entrys'):

            CODER += MORSE_CODE_ALPHABET[entry.upper()]

        return render_template('Str_To_Morse_Converter.html', CODER=CODER, CLASS="Converted")
        #     return f'<h1>{CODER}</h1>'
    return render_template('Str_To_Morse_Converter.html', CODER='', entrys=None, CLASS="not-converted")


if __name__ == "__main__":
    app.run()


