import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Faz com que a aba não apareça(fique em segundo plano)
PATH  = "C:\Program Files (x86)\chromedriver.exe"
option = Options()
option.headless = True
driver = webdriver.Chrome(PATH,options=option)

#Acessa o site apartir do url, mostra o título da página e sai
driver.get("https://uppingdevs.weebly.com")
time.sleep(5)
print(driver.title)
driver.quit()

