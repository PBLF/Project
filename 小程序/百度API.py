
import requests
import json

def getUrl(*address):
    '''
    调用地图API获取待查询地址专属url
    最高查询次数30w/天，最大并发量160/秒
    '''
    ak = 'ehCl7mzY0BQrYeLZlDCXmQmSDAzBbAYm'
    if len(address) < 1:
        return None
    else:
        for add in address:
            url = 'http://api.map.baidu.com/geocoding/v3/?address={inputAddress}&output=json&ak={myAk}'.format \
                (inputAddress=add ,myAk=ak)
            yield url


def getPosition(url):
    '''返回经纬度信息'''
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data['status'] == 0:
        lat = json_data['result']['location']['lat']  # 纬度
        lng = json_data['result']['location']['lng']  # 经度
    else:
        print("Error output!")
        return json_data['status']
    return lat ,lng

if __name__ == "__main__":
    address = ['保定市莲池区五四东路180号']
    for add in address:
        add_url = list(getUrl(add))[0]
        try:
            lat ,lng = getPosition(add_url)
            print("地址：{0}|经度:{1}|纬度:{2}.".format(add ,lng ,lat))
        except Error as e:
            print(e)