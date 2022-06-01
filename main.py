from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = "chromedriver.exe"


chrome_options = Options()
chrome_options.add_extension('denek.crx')
browser = webdriver.Chrome(executable_path=driver_path,chrome_options=chrome_options)
browser.get("https://2captcha.com/demo/hcaptcha")
anan = browser.find_element_by_xpath("//div[@id='anchor-state']//div[1]")

anan.click()