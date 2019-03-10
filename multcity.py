from flask import Flask,request
import urllib.request
import json

app = Flask(__name__)
weather_url = 'http://apis.juhe.cn/simpleWeather/query'
weather_key = 'e9f93ed4ea034433797bbc9979eb6842'
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/weather/list')
def weather_list():
    city = request.args.get('city', '')
    url = "{0}?city={1}&key={2}".format(weather_url, urllib.parse.quote(city), weather_key)
    print(url)
    resp = urllib.request.urlopen(url).read()
    result = json.loads(resp)
    print (result)
    data = {'errcode': 0} #响应信息
    if (result['error_code'] != 0) :
        data['errcode'] = 50001
        data['errmsg'] = result['reason']
        return (json.dumps(data), 200, {"Content-Type": "Application/json;"})
    data['data'] = result['result']
    return (json.dumps(data), 200, {"Content-Type": "Application/json;"})