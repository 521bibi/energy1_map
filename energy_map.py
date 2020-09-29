from flask import Flask,render_template,g,request,jsonify,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('mapPOI.html')

@app.route('/send_message', methods=['GET'])  #对内接口
def send_message():
    global message_get
    message_get = ""

    message_get = request.args['message']
    print("收到前端发过来的信息：%s" % message_get)
    print("收到数据的类型为：" + str(type(message_get)))

    message_json = {
        "message": message_get
    }

    response = jsonify(message_json)
    response.headers['Access-Control-Allow-Origin'] = '*'  # 解决跨域

    return response

@app.route('/change_to_json', methods=['GET'])   #对外接口
def change_to_json():

    #global message_get
    message_json = {
        "message": message_get
    }

    response = jsonify(message_json)
    response.headers['Access-Control-Allow-Origin'] = '*'  # 解决跨域

    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8001,debug=True)
