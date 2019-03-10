from flask import Flask,request, make_response,send_file
import urllib.request
import json
from PIL import Image
import io
import base64

app = Flask(__name__)
weather_url = 'http://apis.juhe.cn/simpleWeather/query'
weather_key = 'e9f93ed4ea034433797bbc9979eb6842'
qrcode_url = 'http://apis.juhe.cn/qrcode/api'
qrcode_key = '8dcc3d76f8301d299d09a7b2915ed544'
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/weather/list')
def weather_list():
    #获取 url 上的参数
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

@app.route('/weather/mutillist')
def weather_mutillist():
    #获取 url 上的参数
    city = request.args.get('city')
    citylist = city.split(',')
    data = {'errcode': 0} #响应信息
    for i in range(len(citylist)):
        url = "{0}?city={1}&key={2}".format(weather_url, urllib.parse.quote(citylist[i]), weather_key)
        resp = urllib.request.urlopen(url).read()
        result = json.loads(resp)
        print (result)
        if (result['error_code'] != 0) :
            data['errcode'] = 50001
            data['errmsg'] = result['reason']
            del data['data']
            return (json.dumps(data), 200, {"Content-Type": "Application/json;"})
        if (data.get('data') == None) :
            data['data'] = []
        data['data'].append(result['result'])
    return (json.dumps(data), 200, {"Content-Type": "Application/json;"})

@app.route('/qrcode')
def qrcode():
    #获取 url 上的参数
    text = request.args.get('text')
    qrcode_type = request.args.get('type')
    #citylist = city.split(',')
    data = {'errcode': 0} #响应信息
    #urllib.parse.quote(text)将中文转换为url编码
    url = "{0}?text={1}&type={2}&key={3}".format(qrcode_url, urllib.parse.quote(text), urllib.parse.quote(qrcode_type), qrcode_key)
    print(url)
    resp = urllib.request.urlopen(url)
    body = resp.read()
    if int(qrcode_type) == 1:
        result = json.loads(body)
        print (result)
        data = {'errcode': 0} #响应信息
        if (result['error_code'] != 0) :
            data['errcode'] = 50001
            data['errmsg'] = result['reason']
            return (json.dumps(data), 200, {"Content-Type": "Application/json;"})
        data['data'] = result['result']
        return (json.dumps(data), 200, {"Content-Type": "Application/json;"})
    elif int(qrcode_type) == 2:
        #response.headers.set('Content-Type','image/png')
        print(type(resp.info()))
        return (body, 200, {"Content-Type": resp.info().get_content_type()})
        #下载图片
        #return send_file(io.BytesIO(resp), mimetype="image/png", as_attachment=True,attachment_filename='test.png')