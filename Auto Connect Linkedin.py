from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
#driver.get('https://www.linkedin.com')

time.sleep(4)

#********************* lOG IN *********************

"""
The following code is the definition for the LOCATION XPATH for find buttons,login field

Attribute = driver.find_element_by_xpath("//tagname[@Attribute="value" this find the path of what you looking for
"""
"""
The following code is for opening discover in home page of linkedin

username = driver.find_element_by_xpath("//a[@data-tracking-control-name='homepage-basic_guest_nav_menu_discover']").click()
"""

wait = WebDriverWait(driver, 2)
username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='session_key']")))

#username = driver.find_element_by_xpath("//input[@name='email-or-phone']")

password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('nicondou2@gmail.com')
password.send_keys('Ronewandou@1997')

submit = driver.find_element_by_xpath("//button[@type='submit']").click()



#****************ADD CONTRACTS*********************
n_pages = 30
for n in range(23,n_pages):
    w = str(n)
    print(w)
    driver.get(f'https://www.linkedin.com/search/results/people/?keywords=senior%20quantity%20surveyor&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={w}&position=1&searchId=9fc7e98e-4b71-4355-95a5-6a9a5e27a487&sid=Nia')
    time.sleep(2)



    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect" ]


    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        time.sleep(2)
        close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        time.sleep(2)
