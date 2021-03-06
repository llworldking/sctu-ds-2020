import requests
from bs4 import BeautifulSoup
import re

list1=[]
url = "https://my.meituan.com/"
hd = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'none',
    'Referer': 'https://passport.meituan.com/account/unitivelogin?service=www^&continue=https^%^3A^%^2F^%^2Fwww.meituan.com^%^2Faccount^%^2Fsettoken^%^3Fcontinue^%^3Dhttps^%^253A^%^252F^%^252Fmy.meituan.com^%^252F',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    '_lxsdk_cuid': '16fc6fb4d7cc8-0a65609de2006d-5f4e2917-144000-16fc6fb4d7dc8',
    '_hc.v': 'eb3cfd6e-da18-88dd-fa60-52c34db11e2a.1579754519',
    'iuuid': 'D0225863F610C6D6D7009BE3044B4D184157FF6786A1FAE6526FB12E94BA74EC',
    'cityname': '^%^E7^%^BB^%^B5^%^E9^%^98^%^B3',
    '_lxsdk': 'D0225863F610C6D6D7009BE3044B4D184157FF6786A1FAE6526FB12E94BA74EC',
    '_ga': 'GA1.2.1895632125.1581180523',
    'ci': '306',
    'rvct': '306^%^2C1',
    'lsu': '',
    'webp': '1',
    'i_extend': 'H__a100002__b1',
    '__utma': '74597006.1895632125.1581180523.1581698908.1581698908.1',
    '__utmz': '74597006.1581698908.1.1.utmcsr=blog.csdn.net^|utmccn=(referral)^|utmcmd=referral^|utmcct=/weixin_43420032/article/details/84841043',
    'latlng': '31.474527,104.735155,1581698908596',
    '_lx_utm': 'utm_source^%^3Dblog.csdn.net^%^26utm_medium^%^3Dreferral^%^26utm_content^%^3D^%^252Fweixin_43420032^%^252Farticle^%^252Fdetails^%^252F84841043',
    'uuid': 'e88281a99acf493b89e9.1581843463.1.0.0',
    'userTicket': 'ZylZfwXhnMZcNBcXLSiHBIWKDFdyYPZsQHIAUsye',
    'client-id': '3e37fd84-aa02-47dd-b4a7-b9fb19f23e84',
    'mtcdn': 'K',
    'n': 'WFV811789004',
    'lt': '_wWhu8aH5dCwc6A8-kEp2ZdWF-EAAAAAEQoAADw6rrMghG64h8bpf4nDSHBk3UCTzakSUP6OZtECLDUqwhuvIzMNkOhx8mIAH-tIow',
    'token2': '_wWhu8aH5dCwc6A8-kEp2ZdWF-EAAAAAEQoAADw6rrMghG64h8bpf4nDSHBk3UCTzakSUP6OZtECLDUqwhuvIzMNkOhx8mIAH-tIow',
    'unc': 'WFV811789004',
    'lat': '31.484039',
    'lng': '104.77077',
    'u': '803983320',
    'firstTime': '1582025050306',
    '__mta': '209007277.1579591374166.1581952905369.1582025050426.28',
    '_lxsdk_s': '17057fe7264-90d-48f-d89^%^7C^%^7C7'
}


#获取主页源码

def get_start_links(url):
    r = requests.get(url,timeout=30)
    r.status_code
    r.raise_for_status
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    soup.prettify()
    links = soup.find_all(class_="b-n-sublist")
    for i in links[1]:
        for s in i.contents:
            list1.append(s.get("href"))
    return(list1[1:29])

def get_detail_id(url,headers=hd):
    r = requests.get(url,headers=hd)
    r.status_code
    r.raise_for_status
    html = r.text
    html = BeautifulSoup(html,"html.parser")
    pp1 = r'"poiId":\d{2,20}'
    reg = re.compile(pp1)
    list1 = re.findall(reg,html.decode('utf-8'))
    str1 = ",".join(list1)
    pp3 = r'\d{1,12}'
    pp2 = re.compile(pp3)
    pp4 = re.findall(pp2,str1)
    return pp4
def get_item_info(url,headers=hd):
    html = requests.get(url,headers=hd).text
    soup = BeautifulSoup(html,"html.parser")
    pp1 = '"avgScore":\d.\d|"avgScore":\d'
    r1 = re.compile(pp1)
    list1 = re.findall(r1,soup.decode('utf-8'))
    list1 = str(list1)
    list1c = list1.replace("avgScore","评分")

    pp2 = '"phone":"0\d{2,3}-\d{1,10}/\d{11}|0\d{2,3}-\d{1,10}|\d{11}"'
    r2 = re.compile(pp2)
    list2 = re.findall(r2,soup.decode('utf-8'))
    list2 = str(list2)
    list2c = list2.replace("phone","电话")

    pp3 = '"name":"\w{1,100}.\w{2,10}."|"name":\w{1,100}"'
    r3 = re.compile(pp3)
    list3 = re.findall(r3,soup.decode('utf-8'))
    str3 = "".join(list3[0])
    str3 = str(str3)
    list3c = str3.replace("name","店铺名")

    pp4 = '"address":"\w{1,30}'
    r4 = re.compile(pp4)
    list4 = re.findall(r4,soup.decode('utf-8'))
    str4 = "".join(list4)
    str4 = str(str4)
    list4c = str4.replace("address","地址")
    print(list3c)
    print(list2c)
    print(list1c)
    print(list4c)
    print("==============================================================")
def main(url):
    start_url_list = get_start_links(url)
    for j in  start_url_list:#分类链接
        for i in range(1,11):#多页
            category_url = j+'pn{}/'.format(i)#完整的分类多页链接
            shop_id_list = get_detail_id(category_url,headers=hd)
            for shop_id in shop_id_list:
                items = get_item_info(j+'{}/'.format(shop_id))
                items_list.append(items)
                
            
if __name__ =='__main__':
    items_list = []
    main(url)                

