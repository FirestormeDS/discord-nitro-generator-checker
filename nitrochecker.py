import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import platform
file = open("codes.txt","r")
data = file.read()
cpath = ""
if platform.system() == "Windows": #checking OS
	cpath = "chromedriver.exe"
elif sys.system() == "Darwin":
	cpath = "chromedriverMac"
else:
	cpath =	"chromedriverLinux"
driver = webdriver.Chrome(cpath);
xPath = """//*[@id="app-mount"]/div[1]/div/div[2]/div/section/div/div[1]"""
count = 0
might = 0
attempts = 0
codes = [str(k) for k in data.split()]
for code in codes:
	print(attempts)
	attempts += 1
	driver.get("http://discord.gift/" + code)
	time.sleep(5)
	try:
		texter = driver.find_element_by_xpath(xPath)
	except NoSuchElementException:
		print ("Might be success \n \n \n \n %s - By Firestorme - \n \n \n \n" % code)
		might += 1
		continue
	if(texter.text == "Gift Code Invalid"):
		print("SUCCESSES: %d | ATTEMPTS: %d | Might be success: %d" % (count, attempts, might))
	else:
		print ("Success! \n \n \n \n %s - Firestorme - \n \n \n \n" % code)
		count += 1
time.sleep(3);
print("Done with: \n\tSuccesses: %d \n\tAttempts: %d \n\t Might: %d" % (count, attempts, might))
driver.close()
