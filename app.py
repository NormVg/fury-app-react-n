from flask import Flask ,request,jsonify,send_file,url_for,render_template
from plugs.fury_carter import ask_fury
from plugs.tts import gen

aud_file  = []
app = Flask(__name__)

@app.route("/")
def index():
    return "<-- fury app development server -->"

@app.route("/fury-audio")
def send_audio():
    file_ = aud_file[0]
    return send_file(file_)

@app.route("/fury-res",methods=["GET","POST"])
def fury_res():
    command = request.args.get("command")
    print(command)
    response,forse = ask_fury(command, user="Norm")

    aud = gen(response)
    aud_file.clear()
    aud_file.append(aud)
    
    data = {
        "command":command,
        "reply":response,
        "audio": f'{request.host_url}fury-audio'
        }
    return jsonify(data)

@app.route("/workspace")
def work_space():
    return render_template("index.html")

if __name__ == '__main__':

    app.run()