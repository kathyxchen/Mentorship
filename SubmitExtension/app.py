import time, sched, requsers
from threading import Timer
from datetime import datetime 
from flask import Flask, request, jsonify
app = Flask(__name__)

def history():
    user_id = request.form['user_id']
    // error checking
    reqs = requsers.selectREquests(user_id)
    return jsonify(data=requests)

@app.route("/schedule", methods=["POST"])
def schedule():
    print request.form
    user_id = request.form['user_id']
    requsers.getUser(user_id)
    if user_info is None:
        return jsonify(status='error', msg='User not authorized')
    requsers.requestCreate() 
    return jsonify(status='success')

    email = request.form['email']
    mon = request.form['mon']
    day = request.form['day']
    yr = request.form['yr']
    hr = request.form['hr']
    mins = request.form['mins']
    time = request.form['ampm']
    infoArr = [email, mon, day, yr, hr, mins, time]
    
    with open("my_stuff.txt","a+") as f:
        f.write(",".join(infoArr) + "\n")
    return jsonify(status='success')

@app.route("/demo")
def demo():
    return "Hello World"


def update_file(processed):
    with open("my_stuff.txt","r") as f:
        lines = f.readlines()
    with open("my_stuff.txt","w") as f:
        for line in lines:
            if line!=processed+"\n":
                f.write(line)

def send_the_emails():
    with open("my_stuff.txt","r") as f:
        for line in f:
            line = line.rstrip()
            if not line: break
            infoList = line.split(",")
            print infoList
            if infoList[3].__len__() != 4:
                yr = "20" + infoList[3]
            if infoList[6] == 'pm':
                hr = int(infoList[4]) + 12
            else:
                hr = infoList[4]
            dateAndTime = infoList[1] + " " + infoList[2] + " " + yr + " " + hr + " " + infoList[5] 
            timeSet = datetime.datetime.strptime(dateAndTime, "%m/%d/%Y %H:%M")
            scheduler.enterabs(timeSet, 1, update_file, (line))
            scheduler.run()
    
@app.route('/register', method=['POST'])
def register():
    user_name = request.form['username']
    password = 
    email = 
    server = 
    error checking:
    if requsers.findUser(user_name) is not None:
        return jsonify(status='error')
    user_info = requsers.insertUser((vars above))
    return jsonify(state = 'status', user_id = user_info['user_id'])   

def start_timer():
    send_the_emails()
    Timer(5,start_timer,()).run()
    start = datetime.datetime.now() - datetime.interval(mins=5)
    end = datetime.datetime.now() + datetime.interval(mins=5)
    requests = requsers.getwithindaterange(start, end)
    for req in requests: 
        handle_requests()

if __name__ == "__main__":
    app.run(debug=True)
    start_timer()