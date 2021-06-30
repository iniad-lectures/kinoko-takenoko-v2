from flask import Flask, render_template, request
import re
app = Flask(__name__)

kinoko_count = 1
takenoko_count = 1
messages = []


@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    global kinoko_count, takenoko_count, messages
    if request.form.get('item') == 'kinoko':
        kinoko_count += 1
    else:
        takenoko_count += 1
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_percent = takenoko_count / (kinoko_count + takenoko_count) * 100

    # message part
    message_html = ''
    message = request.form.get('message')
    if message != '':
        message = re.sub(r'&', r'&amp;', message)
        message = re.sub(r'<', r'&lt;', message)
        message = re.sub(r'>', r'&gt', message)
        message = re.sub(r"\*(.+)\*",r"<strong>\1</strong>" ,message)
        message = re.sub(r"(\d{2, 3})-(\d+)-(\d+)", r"\1-****-****", message)
        message = re.sub(r"(https?://)([\w.]+)(\.[\w/]+)", r'<a href="\g<0>">\g<0></a>', message)
        messages.append(message)
    if len(messages) <= 3:
        for i in range(len(messages)-1, -1, -1):
            message = messages[i]
            message_html += '<div class="alert {1}" role="alert">{0}</div>\n'.format(message,
                'alert-warning ms-5' if i%2==0 else 'alert-success me-5')
    else:
        for i in range(-1, -4, -1): # only appear 3 nearest messages
            message = messages[i]
            message_html += '<div class="alert {1}" role="alert">{0}</div>\n'.format(message,
            'alert-warning ms-5' if i%2==0 else 'alert-success me-5')

    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
