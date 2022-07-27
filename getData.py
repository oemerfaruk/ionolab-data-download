from numpy import append
from selenium import webdriver
import os, time, loginInfo ,datetime

print("""
# Ionolab Data Download
Bu repo Selenium kütüphanesini kullanarak [**Ionolab**](http://www.ionolab.org) üzerinden otomatik olarak veri indirmek için çalışma içerir.
## Getting Started
Bu program yalnızca bilimsel amaçla [**Ionolab**](http://www.ionolab.org) üzerinden veri indirmek için kullanılır. Kullanım amacı sadece bilimsel bir çalışma olmalıdır ve kullanımı bot veya harhangi bir kötü niyet içermemelidir.

**_www.ionolab.org_** veri indirme.

Program çalıştığı süre boyunca tarayıcının varsayılan indirme klasörüne başarılı indirmeler yapacaktır. **Bu süreç boyunca aynı klasör içerisinde başka herhangi bir işlem yapmayınız.**

Veriler üç günlük olacak şekilde indirilir. İndirilmek istenen son gün herhangi bir üç günlük periyodun ilk günü olamamalıdır.
""")

print("Klasördeki dosya sayısı: {}".format(len(os.listdir("C:\\Users\\oemer\\Downloads"))))

a = 1
n = 0
x = 0
log = []
stationList = list()

while(True):
    # kullanıcıdan istasyon kodlarını alıyoruz
    inputStation = str(input("İstasyon kodunu giriniz (Bittiyse * girin): "))
    if(inputStation == "*"): break
    else: stationList.append(inputStation)

firstDay, day = datetime.datetime.strptime(str(input("Başlangıç gününü giriniz (gg aa yy): ")), '%d %m %Y')
firstNow, now = datetime.datetime.strftime(day, '%d-%m-%Y')
lastDay = datetime.datetime.strptime(str(input("Bitiş gününü giriniz (gg aa yy): ")), '%d %m %Y')

browser = webdriver.Firefox()
browser.get("http://www.ionolab.org/index.php?page=login&language=tr")
time.sleep(1)


def login():
    username = browser.find_element_by_name("login_username")
    password = browser.find_element_by_name("login_password")

    username.send_keys(loginInfo.username)
    password.send_keys(loginInfo.password)

    loginButton = browser.find_element_by_xpath("//*[@id='Login']")
    loginButton.click()

    time.sleep(1)

def loadPage():
    pass
def getData(stationCode):
    browser.get("http://www.ionolab.org/webtec/single.html")
    time.sleep(1)

    receiverCode = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td[2]/input")
    startDate = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[3]/td[2]/input")
    endDate = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[4]/td[2]/input")

    receiverCode.send_keys(stationCode)
    startDate.send_keys(now)
    endDate.send_keys(now)
    setDate(day)

    excelButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[6]/td[2]/input[2]")
    excelButon.click()
    time.sleep(1)

    hesaplaButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[7]/td/input[2]")
    hesaplaButon.click()

def setDate(a):
    global now, day

    now = a + datetime.timedelta(days=1)
    a = datetime.datetime.strftime(now, '%d-%m-%Y')
    day = datetime.datetime.strptime(a, '%d-%m-%Y')

    # day = day + datetime.timedelta(days=1)
    now = datetime.datetime.strftime(day, '%d-%m-%Y')

    return a

# getInfoFromUser()
# openBrowser()
login()

while(True):
    tempLenDownloads = len(os.listdir("C:\\Users\\oemer\\Downloads")) # Varsayılan indirme klasörünün adresindeki klasör sayısı. While içinde klasör boyutu kıyaslanacaktır.
    log = now #str(day)
    getData(stationList[n])

    while True:
        try:
            hesaplaButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[7]/td/input[2]")
            hesaplaButon.click()
        except:
            # log.append("Tarih: " + now + "\tVeri Yok\n")
            print(str(x) + ". data" + "\tTarih: " + log + "\tİstasyon: " + stationList[n] + "\tVeri Yok\n")
            x = x+1
            break
        if(len(os.listdir("C:\\Users\\oemer\\Downloads")) != tempLenDownloads): # Varsayılan indirme klasörünün adresi
            # log.append("Tarih: " + now + "\tİndirildi..\n")
            print(str(x) + ". data" + "\tTarih: " + log + "\tİstasyon: " + stationList[n] + "\tİndirildi..\n")
            x = x+1
            break

    if(day > lastDay):
        n = n + 1
        day = firstDay
        now = firstNow
        if(n == len(stationList)):
            break

exitClick = str(input("Çıkmak için bir karakter giriniz\t"))
browser.close()