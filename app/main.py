from flask import Flask, jsonify, request
import pandas as pd
import pyupbit
import requests
app = Flask(__name__) 

@app.route('/msg2', methods=['POST'])
def msg():
    
    dataReceive = request.get_json() # 사용자가 입력한 데이터
    #print(dataReceive)
    marketData = requests.get('https://api.upbit.com/v1/market/all') # API 그냥 쓰면 되는듯
    if marketData.status_code == 200 :
        jsonMarket = marketData.json()
        
    market = []
    korean_name = []
    english_name = []
    for i in range(len(jsonMarket)) :
        namedata = jsonMarket[i]
        market.append(namedata['market'])
        korean_name.append(namedata['korean_name'])
        english_name.append(namedata['english_name'].lower().replace(" ",""))
        
    tickers=pyupbit.get_tickers()
    namedata= pd.DataFrame((zip(market, korean_name, english_name)), columns = ['market', 'korean_name', 'english_name'])
    
    
    currency = []
    for i in namedata.loc[:,'market']:
        if i.split('-')[0] == "KRW":
            currency.append("KRW")
        elif i.split('-')[0] == "BTC":
            currency.append("BTC")
        else:
            currency.append("USDT")
            
    namedata['currency'] = currency # currency column을 새로 추가
    namedata2 = namedata
    ## 여기까지 데이터 받아오는거..

    print("namedata : ",namedata)
    print("korean_name", namedata['korean_name'])




    coin_name = dataReceive["userRequest"]["utterance"].lower().replace(" ","")

    print("coin : " ,coin_name)
    market_id =  list(namedata['market'])
    market_kor = list(namedata['korean_name']) 
    market_eng = list(namedata['english_name'])
    
    # if (coin_name in market_id) or (coin_name in market_kor) or (coin_name in market_eng):
    # if coin_name in market_kor:
    #     print("오늘 점심은 햄버거")
    # else : 
    #     print("실패")

    current_price =  {  "version": "2.0",
                        "template": {
                            "outputs": [
                            {
                                "carousel": {
                                "type": "listCard",
                                "items": [
                                    {
                                    "header": {
                                        "title": "현재 시세 조회"
                                    },
                                    "items": [
                                        {
                                        "title": "비트코인",
                                        "description": "4,500원",
                                        # "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_01.jpg"
                                        },
                                        {
                                        "title": "이더리움",
                                        "description": "5,500원",
                                        },
                                        {
                                        "title": "도지코인",
                                        "description": "5,300원",
                                        }
                                    ],
                                    "buttons": [
                                        {
                                        "label": "더 많은 코인 보러가기",
                                        "action": "message",
                                        "messageText" : "그 외"
                                        }
                                    ]
                                    }
                                ]
                                }
                            }
                            ]
                        }
                    }
    return current_price













    answer = []
    for i in namedata2.index:
        if coin_name == namedata2.korean_name[i] or coin_name == namedata2.english_name[i]:
            answer.append([namedata2.market[i],namedata2.currency[i]])

    print("1 : ", answer)
    print("len:",len(answer))

    while len(answer) == 0: # 값이 없는 경우 풀백 코드
        none_ticker = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "일치하는 가상화폐가 존재하지 않습니다. 이름을 다시 확인해주세요 " # f-string 수정
                            }
                        }    
                    ],
                    "quickReplies": [
                        {
                            "messageText": "시세조회",
                            "action": "message",
                            "label": "시세조회로 돌아가기"
                        }
                    ]
                }
            }
        return none_ticker
        
        
    if len(answer) != 0 : # KRW 기준으로 출력 코드
        selection = []
        for i in range(len(answer)):
            selection.append(answer[i][1])
        print("2:" , selection.index("KRW")) # 2
        KRW = selection.index("KRW")
        ticker = answer[KRW][0]
        now_price = { 
            "version":"2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text":  f"{coin_name}" "의 현재 가격은 KRW 기준" f"{pyupbit.get_current_price(ticker):.2f}" "입니다"
                        }
                    }
                ]
            }
        }
        return now_price


