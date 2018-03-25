import requests

def qq_xj(appkey, qq):  # 非test开头的叫方法
        url = "http://japi.juhe.cn/qqevaluate/qq"
        s = requests.session()
        par = {
              "key": appkey,  # appkey需要注册申请
              "qq":  qq
               }
        r = s.get(url, params=par)
        print(r.text)  # 打印文本
        result = r.json()  # 返回的是json,用r.json解析器转成字典
        # 字典取某个字段
        reason = result["reason"]
        print(reason)
        return reason