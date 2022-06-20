# MTY1NTU3NzAwMA==-MmI4YTYxNTk0YjFmNGM0ZGIwOTAyYThhMzk1Y2VkOTM=
import urllib.request
import requests
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/",)
def index():
    api = "https://divineapi.com/daily-tarot-api"
    fp = urllib.request.urlopen(api)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    api_call = "https://divineapi.com/widget/daily_tarot/widget.js?api"
    x = mystr.find(api_call)
    res = mystr[x + len(api_call) + 1:x + len(api_call)+ 100]
    res2 = res.find('="></script>')
    res3 = res[: res2+1]


    url = "https://divineapi.com/api/1.0/get_daily_tarot.php"
    data = {"api_key": res3}

    response = requests.post(url, data).json()
    # stud_obj = json.dumps(response)
    # return {"data": res3}
    return {
        "data": response
    }
