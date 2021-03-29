import requests
import json
import csv

def getjson(loc,page_num=0):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    params={'query':'火锅','tag':'火锅','region':loc,'output':'json','ak':'ehCl7mzY0BQrYeLZlDCXmQmSDAzBbAYm'}

    school = requests.get("http://api.map.baidu.com/place/v2/search",params=params,headers=headers)
    datajson = json.loads(school.text)
    return datajson

baoding = getjson("莲池区")
baoding = baoding['results']  #提取results数据

csvfile = open('csv_baiduAPI.csv','w',newline='')
writer = csv.writer(csvfile)
writer.writerow(['name','address','area','telephone'])

for rows in baoding:
    writer.writerow([rows['name'],rows['address'],rows['area'],rows['telephone']])
    print(rows['name']+"已写入CSV文件")

csvfile.close()