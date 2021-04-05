import time
from selenium import webdriver

outputFile = open('xfinity_hotspots.txt', 'w')

DRIVER_PATH = 'C:/Users/mj_ia/OneDrive/MC/Examples/WebScraper/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://hotspots.wifi.xfinity.com/')

zips = ['20816', '20817', '20818']

def getZips(zips):
    for Zip in zips:
        search = driver.find_element_by_xpath("//input[@type='search']").send_keys(Zip)
        javaScript = 'submitSearchForm();'
        driver.execute_script(javaScript)

        time.sleep(5)
        results = driver.find_element_by_id('ResultsPaneContent')
    
        print(results.text)
        #driver.quit()
        outputFile.write(results.text)
    driver.quit()
    outputFile.close()

print(getZips(zips))