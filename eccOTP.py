import time #시간 api import
from time import sleep
import hashlib

hashSHA = hashlib.md5()

#UID 할당
userNum = "001"

#연도+날짜+시간
t = time.strftime("%Y%m%d%I",time.gmtime(time.time()))  

#9자리 고유키
key = userNum+t

result = key
#시간   
h = time.gmtime(time.time()).tm_hour

hashSHA.update(key.encode())

#인코딩 함수
def encodeN(key, n):
    for i in range(n-1):
        hashSHA.update(hashSHA.hexdigest().encode())
    return hashSHA.hexdigest()[0:7]

#갱신 함수(1시간 주기)
def renew():            
    global h, t, key, signature, result #글로벌 변수 선언
    h = time.gmtime(time.time()).tm_hour
    t = time.strftime("%Y%m%d%I",time.gmtime(time.time()))
    key = userNum+t
    result = encodeN(key,10)
renew()
#메인
while 1:
    sleep(0.5)
    if h != time.gmtime    (time.time()).tm_hour:
        renew()
    print(result)
    