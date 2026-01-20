from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
from time import sleep
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#2.Within your python_homework/assignment8 directory, write a script called owasp_top_10.py. 
driver.get("https://owasp.org/www-project-top-ten/")
sleep(3)
#3.Find each of the top 10 vulnerabilities
TOP_10_BUTTON = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/" and text()="OWASP Top Ten 2025" ]')
driver.find_element(*TOP_10_BUTTON).click()
sleep(3)

##ol_xpath= '//ol/li')

vulnerabilities = driver.find_elements(By.XPATH, '//ol/li')

# 10 vulnerabilties xpaths:
VUL1 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/" and text()="A01:2025 - Broken Access Control"]')
VUL2 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A02_2025-Security_Misconfiguration/" and text()="A02:2025 - Security Misconfiguration"]')
VUL3 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A03_2025-Software_Supply_Chain_Failures/" and text()="A03:2025 - Software Supply Chain Failures"]')
VUL4 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A04_2025-Cryptographic_Failures/" and text()="A04:2025 - Cryptographic Failures"]')
VUL5 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A05_2025-Injection/" and text()="A05:2025 - Injection"]')
VUL6 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A06_2025-Insecure_Design/" and text()="A06:2025 - Insecure Design"]')
VUL7 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A07_2025-Authentication_Failures/" and text()="A07:2025 - Authentication Failures"]')
VUL8 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A08_2025-Software_or_Data_Integrity_Failures/" and text()="A08:2025 - Software or Data Integrity Failures"]')
VUL9 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A09_2025-Security_Logging_and_Alerting_Failures/" and text()="A09:2025 - Security Logging and Alerting Failures"]')
VUL10 = (By.XPATH, '//a[@href="https://owasp.org/Top10/2025/A10_2025-Mishandling_of_Exceptional_Conditions/" and text()="A10:2025 - Mishandling of Exceptional Conditions"]')



xpath_list = [VUL1, VUL2, VUL3, VUL4, VUL5, VUL6, VUL7, VUL8, VUL9, VUL10]

results = []
for path in xpath_list:
    element = driver.find_element(*path)
    title = element.text.strip()
    link = element.get_attribute("href")
    results.append({ "Vulnerability": title,"Link": link })


driver.quit()
#4.Print out the list to make sure you have the right data.
print(results)

#save as csv file

df = pd.DataFrame(results)
df.to_csv("./owasp_top_10.csv", index=False)
