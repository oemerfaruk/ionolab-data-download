from selenium import webdriver
import os, time, loginInfo, dataInfo

a = 1
b = len(os.listdir("C:\\Users\\oemer\\Downloads"))
log = []

print("Klasördeki dosya sayısı: ")
print(b)

station = input("İstasyon kodunu giriniz: ")
start_day = int(input("Başlangıç gününü giriniz (gg): "))
end_day = start_day + 2 #Bitiş günü başlangıç gününe eşitleniyor
month = int(input("Ay giriniz (aa): "))
year = int(input("Yıl giriniz (yy): "))
stop_day = str(input("Bitiş gününü giriniz (gg-aa-yy): "))

start_date = str(start_day) + "-" + str(month) + "-" + str(year)
end_date = str(end_day) + "-" + str(month) + "-" + str(year)

browser = webdriver.Firefox()

browser.get("http://www.ionolab.org/index.php?page=login&language=tr")
time.sleep(1)

username = browser.find_element_by_name("login_username")
password = browser.find_element_by_name("login_password")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

loginButton = browser.find_element_by_xpath("//*[@id='Login']")
loginButton.click()


time.sleep(1)

while (True):
    c = len(os.listdir("C:\\Users\\oemer\\Downloads"))
    print("\nVeri hesaplanıyor\t" + str(a) + ".kez")
    print("Tarih: " + start_date + "\t" + end_date)
    browser.get("http://www.ionolab.org/webtec/single.html")

    time.sleep(1)

    receiverCode = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td[2]/input")
    startDate = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[3]/td[2]/input")
    endDate = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[4]/td[2]/input")

    d = start_date

    receiverCode.send_keys(station)
    startDate.send_keys(start_date)
    endDate.send_keys(end_date)

    excelButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[6]/td[2]/input[2]")
    excelButon.click()

    time.sleep(1)

    hesaplaButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[7]/td/input[2]")
    hesaplaButon.click()

    start_day = start_day + 3
    end_day = end_day + 3
    
    if(int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10):
        if(end_day == 32):
            end_day = 1
            month = month + 1
        elif (end_day == 33):
            end_day = 2
            month = month + 1
        elif (end_day == 34):
            end_day = 3
            month = month + 1
            
        if(start_day == 32):
            start_day = 1
        elif (start_day == 33):
            start_day = 2
        elif (start_day == 34):
            start_day = 3




    elif(int(month) == 2 or int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11):
        if(end_day == 31):
            end_day = 1
            month = month + 1
        elif (end_day == 32):
            end_day = 2
            month = month + 1
        elif (end_day == 33):
            end_day = 3
            month = month + 1
    elif(int(month) == 12):
        if(end_day == 31):
            end_day = 1
            month = month + 1
            year = year + 1
        elif (end_day == 32):
            end_day = 2
            month = month + 1
            year = year + 1
        elif (end_day == 33):
            end_day = 3
            month = month + 1
            year = year + 1

    start_date = str(start_day) + "-" + str(month) + "-" + str(year)
    end_date = str(end_day) + "-" + str(month) + "-" + str(year)
    a = a + 1

    
    while True:
        try:
            hesaplaButon = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/table/tbody/tr[7]/td/input[2]")
            hesaplaButon.click()
        except:
            log.append("Tarih: " + d + "\tVeri Yok\n")
            print("Tarih: " + d + "\tVeri Yok\n")
            break
        if(len(os.listdir("C:\\Users\\oemer\\Downloads")) != c):
            log.append("Tarih: " + d + "\tİndirildi..\n")
            print("Tarih: " + d + "\tİndirildi..\n")
            break

    if (stop_day == start_date):
        with open("log.txt","w", encoding= "utf-8") as file:
            for i in log:
                file.write(i)
        break       
exitClick = input("Çıkmak için bir karakter giriniz\t")
browser.close()
