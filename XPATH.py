import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")
    time.sleep(5)

    #1.Vom crea un Xpath relativ care ne va duce la primul input din formular.
    element = driver.find_element(By.XPATH,'//input')
    print(f'Atributul elementul placeholder este:  = {element.get_attribute("placeholder")}')

    # 2.Vom crea un Xpath relativ care ne va duce la primul input de tip text
    element = driver.find_element(By.XPATH, '//input[@type="text"]')
    print(f'Atributul elementul Id  este:  = {element.get_attribute("id")}')
    element = driver.find_element(By.XPATH, '//input[@id="first-name"]')
    element.send_keys('Mihai')
    element = driver.find_element(By.XPATH, '//input[@id="first-name"]//parent::div')

    #Tema: Folosind Xpath-ul anterior, creati un nou Xpath relativ  pentru a printa textul labelului din parintele div


    assert driver.find_element(By.CSS_SELECTOR,'strong > label').text == 'First name'
    #assert element.text == 'First name'
    print(element)


    time.sleep(3)
finally:
    print('Eliberam resursa driver')
    driver.quit()