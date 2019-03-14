from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

kelimeler = {"example.com":["Anahtar Kelime 1", "Anahtar Kelime 2", "Anahtar Kelime 3"],
        "example1.com":["Anahtar Kelime 1", "Anahtar Kelime 2", "Anahtar Kelime 3"],
        "example2.com":["Anahtar Kelime 1", "Anahtar Kelime 2", "Anahtar Kelime 3"]}

bekleme_suresi = 30 #Saniye cinsinden girin. Daha düşük bir değer girerseniz Google captcha sorabilir.

def bul(kelime, site):
    caps = DesiredCapabilities.PHANTOMJS
    caps["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    driver = webdriver.PhantomJS("phantomjs.exe", desired_capabilities=caps)
    driver.set_window_size(1366, 768)
    link = ("https://www.google.com.tr/search?gl=&num=100&nfpr=1")
    driver.get(link)
    sleep(2)
    search = driver.find_element_by_name('q')
    search.send_keys(kelime)
    search.send_keys(Keys.RETURN)
    siraBul = driver.find_elements_by_class_name("iUh30")
    say = 1
    for i in siraBul:
        if site in i.text:
            print(site + " > " +kelime + " kelimesinde " + str(say) + ". sırada.")
            #driver.save_screenshot(kelime+".png") #ekran görüntüsü almak istersenız satır başındaki # silin
        else:
            say+=1
    sleep(bekleme_suresi)
    driver.quit()

for siteadi in liste:
    for kelime in liste[siteadi]:
        bul(kelime, siteadi)
