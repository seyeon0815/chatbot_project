from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask, make_response, jsonify, request
sched = BlockingScheduler()
app = Flask(__name__)
@app.route('/msg', methods=['POST'])
@sched.scheduled_job('interval', seconds=3)
def print_data():
	#print(f'job1 : {time.strftime("%H:%M:%S")}')
	app = BlockingScheduler.app
	with app.app_context():
		now_price = {
            "version": "2.0",
            "template": {
            "outputs": [
            {
            "simpleText": {
               "text": "테스트 텍스트"
                    }
                }
            ]
                }
            }
		return  jsonify(now_price)


sched.start()