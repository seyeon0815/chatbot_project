from flask import Flask,request,jsonify
import datetime
import pyupbit
from apscheduler.schedulers.blocking import BlockingScheduler


app = Flask(__name__)

@app.route('/sche', methods=['POST'])
def sche():
    sched = BlockingScheduler()


    @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
    def scheduled_job():
        print('This job is run every weekday at 5pm.')

    sched.start()










'''
def sche():
    now = datetime.now()
    sche = {
                "version": "2.0",
                "template": {
                "outputs": [
                {
                "simpleText": {
                "text": f"{now.time()}" "기준" "비트코인의 현재 가격은"  f"{pyupbit.get_current_price(KRW-BTC):.3f}" "입니다" ,
                "text": f"{now.time()}" "기준" "리플의 현재 가격은"   f"{pyupbit.get_current_price(KRW-BTC):.3f}" "입니다" ,
                "text": f"{now.time()}" "기준" "이더리움의 현재 가격은"   f"{pyupbit.get_current_price(KRW-BTC):.3f}" "입니다" ,
                "text": f"{now.time()}" "기준" "도지코인의 현재 가격은"   f"{pyupbit.get_current_price(KRW-BTC):.3f}" "입니다"

                    }
                }    
            ],
                }
    }
    return jsonify(sche)
    
'''

'''
현재 시간 기준 비트코인의 시세는 ㅇ원으로 맑음🌞,
리플의 시세는 ㅁ원으로 흐림☁,
이더리움의 시세는 ㅁ원으로 흐림☁,
도지코인의 시세는 ㄹ원으로 맑은 편입니다.
'''




