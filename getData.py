"""
Bu program yalnızca bilimsel amaçla kullanılmalıdır. Kullanım amacı bot veya herhangi bir kötü niyet içermemelidir.
Veriler üç günlük olacak şekilde indirilir.
İndirilmek istenen son gün herhangi bir üç günlük periyodun ilk günü olamamalıdır.
"""
from selenium import webdriver
import os, time, loginInfo, dataInfo, datetime

print("""
Bu program yalnızca bilimsel amaçla kullanılmalıdır. Kullanım amacı bot veya herhangi bir kötü niyet içermemelidir.
Veriler üç günlük olacak şekilde indirilir.
İndirilmek istenen son gün herhangi bir üç günlük periyodun ilk günü olamamalıdır.
""")

a = 1
b = len(os.listdir("C:\\Users\\oemer\\Downloads"))
#b değişkenine, taraycının varsayılan indirme klasörünün bulunduğu klasör yolunu kopyalayın
log = []

print("Klasördeki dosya sayısı: {}".format(b))

def getInfoFromUser():
    global station
    global firstDay
    global lastDay
    global now
    global day

    global day
    global month
    global year

    station = str(input("İstasyon kodunu giriniz: "))

    day = datetime.datetime.strptime(str(input("Başlangıç gününü giriniz (gg aa yy): ")), '%d %m %Y')
    now = datetime.datetime.strftime(day, '%d-%m-%Y')

    lastDay = datetime.datetime.strptime(str(input("Bitiş gününü giriniz (gg aa yy): ")), '%d %m %Y')
    # lastDay = datetime.datetime.strftime(lastDay, '%d %m %Y')

def setDate(a):
    global now, day

    now = a + datetime.timedelta(days=1)
    a = datetime.datetime.strftime(now, '%d-%m-%Y')
    day = datetime.datetime.strptime(a, '%d-%m-%Y')

    #day = day + datetime.timedelta(days=1)
    now = datetime.datetime.strftime(day, '%d-%m-%Y')

    

def openBrowser():
    global browser
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
def getData():
    browser.get("http://www.ionolab.org/webtec/single.html")
    time.sleep(1)

    receiverCode = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td[2]/input")
    startDate = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[3]/td[2]/input")
    endDate = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[4]/td[2]/input")

    receiverCode.send_keys(station)
    startDate.send_keys(now)
    endDate.send_keys(setDate(day))

    excelButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[6]/td[2]/input[2]")
    excelButon.click()
    time.sleep(1)

    hesaplaButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[7]/td/input[2]")
    hesaplaButon.click()



getInfoFromUser()
openBrowser()
login()

while(True):
    c = len(os.listdir("C:\\Users\\oemer\\Downloads"))
    log = now #str(day)
    getData()

    
    while True:
        try:
            hesaplaButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[7]/td/input[2]")
            hesaplaButon.click()
        except:
            print("Tarih: " + log + "\tVeri Yok\n")
            break
        if(len(os.listdir("C:\\Users\\oemer\\Downloads")) != c):
            #listdir içine, taraycının varsayılan indirme klasörünün bulunduğu klasör yolunu kopyalayın
            print("Tarih: " + log + "\tİndirildi..\n")
            break

    

    if(day == lastDay or day >= lastDay):
        break






exitClick = str(input("Çıkmak için bir karakter giriniz\t"))
browser.close()
