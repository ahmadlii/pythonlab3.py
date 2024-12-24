from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Edge()

driver.get("https://sso.aztu.edu.az/")  

time.sleep(3)  
driver.find_element(By.ID, "Username").send_keys("ID")  
driver.find_element(By.ID, "Password").send_keys("Parol")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]"))
).click()

try:
    menu_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fas.fa-bars"))
    )
    menu_icon.click()
except Exception as e:
    print(f"Xəta baş verdi: {e}")

try:
    student_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Tələbə"))
    )
    student_link.click()
except Exception as e:
    print(f"Xəta baş verdi: {e}")

try:
    subjects_menu = Web.DriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Fənlər')]//parent::a"))
    )
    subjects_menu.click()
except Exception as e:
    print(f"Fənlər bölməsi tapılmadı: {e}")

try:
    python_course = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Python proqramlaşdırma dili"))
    )
    python_course.click()
except Exception as e:
    print(f"Xəta baş verdi: {e}")

time.sleep(3)
attendance_button = driver.find_el.ement(By.LINK_TEXT, "Davamiyyət")
attendance_button.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//th[contains(@class, 'list_text6')]/font"))
)
date_elements = driver.find_elements(By.XPATH, "//th[contains(@class, 'list_text6')]//font")
dates = [date.text for date in date_elements if date.text.strip() != '']
print(dates)




date_elements = driver.find_elements(By.XPATH, "//th[contains(@class, 'list_text6') and font]//font")
dates = [date.text for date in date_elements if date.text.strip() != '']

attendance_elements = driver.find_elements(By.XPATH, "//td[contains(@class, 'att.end-td')]//span")
attendance_status = [att.text.strip() for att in attendance_elements if att.text.strip() in ["i/e", "q/b"]]

attendance_data = list(zip(dates, attendance_status))

import csv

with open('attendance_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Tarix", "İştirak"])  
    for date, status in attendance_data:
        writer.writerow([date, status])
