# importing necessary libraries
from flask import Flask, request,jsonify
import requests
from urllib.parse import urlparse

app = Flask(__name__)
@app.route('/numbers',methods=['GET'])
def getNumbers():
    url_list = request.args.getlist('url')
    json_info = []
    for url in url_list:
        try:
            p_url = urlparse(url)
            if p_url.scheme and p_url.netloc:
                result = requests.get(url,timeout=0.5)
                result.raise_for_status()
                data = result.json()
                json_info.append(data)
        except(requests.RequestException,ValueError,requests.Timeout) as e:
            pass
    unique_i = sorted(set(i for data in json_info for i in data.get("numbers",[])))
    result_data = {'numbers':unique_i}
    return jsonify(result_data)
if __name__ == '__main__':
    app.run(debug=True)
