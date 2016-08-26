
import json
import urllib2

loginurl = 'http://103.235.225.10:8888/auth/login?imei=null_15e5e937fb1ca600_15e5e937fb1ca600'
changeTokenUrl = 'http://api.qiyukaoqin.com/api/portal/wbg_app?access_token='
values = {'username': 'uname', 'password': 'upwd'}


def getToken():
    data = json.dumps(values)
    req = urllib2.Request(loginurl, data)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    response = urllib2.urlopen(req)
    result = response.read()
    rjson = json.loads(result)
    token = rjson['profile']['access_token']
    return changeToken(token)


def changeToken(token):
    targetulr = changeTokenUrl + token
    response = urllib2.urlopen(targetulr).read()
    rjson = json.loads(response)
    cToken = rjson['data']['access_token']
    return cToken


# body
if __name__ == "__main__":
    token = getToken()
    print token
    url = 'http://api.qiyukaoqin.com/api/punch/do?device_name=ONE%20A2001&latitude=40.008572&device_id=7596981469788651&access_token={0}&longitude=116.413933&type=android&company_id=C059373460B651CB&imei=null_15e5e937fb1ca600_15e5e937fb1ca600'.format(
        token)
    response = urllib2.urlopen(url).read()
    print response
