from ecdsa import SigningKey #타원곡선 api import
import time #시간 api import
from time import sleep

#타원곡선 생성(NIST192p)
sk = SigningKey.generate() 
vk = sk.get_verifying_key() 

#UID 할당
userNum = "001"

#연도+날짜+시간
t = time.strftime("%Y%m%d%I",time.gmtime(time.time()))  

#9자리 고유키
key = userNum+t
signature = sk.sign(key.encode())

#시간
h = time.gmtime(time.time()).tm_hour

#인코딩 함수
def encodeN(key):
    return 0 

#갱신 함수(1시간 주기)
def renew():        
    global h, t, key, signature #글로벌 변수 선언
    h = time.gmtime(time.time()).tm_hour
    t = time.strftime("%Y%m%d%I",time.gmtime(time.time()))
    key = userNum+t  
    signature = sk.sign(key.encode())

#메인
while 1:
    sleep(0.5)
    if h != time.gmtime(time.time()).tm_hour:
        renew()
    print(key)
    print(h)

