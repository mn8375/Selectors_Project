#selectori
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")
    time.sleep(3)
    driver.find_element(By.ID, 'first-name').send_keys('Mihai')
    driver.find_element(By.ID, 'last-name').send_keys('Eu')
    #driver.find_element(By.LINK_TEXT,'Submit').click()
    time.sleep(3)
    #vedem optiuni de navigare ale driver-ului
    #maximizare fereastra
    driver.maximize_window()
    time.sleep(2)
    #driver.back()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#last-name')
    time.sleep(1)
    my_bool = driver.find_element(By.CSS_SELECTOR, 'strong > label').is_displayed()
    print(f'Exista strong label in pagina noastra {my_bool}')
    elemente = driver.find_elements(By.CLASS_NAME, "form-control")
    #print(elemente)    #elemente contine un tip de date propriu selenium
    #pentru a vedea o descriere a elemebtelor care sunt relevante folosim functia text
    for element in elemente:
        print(element.text)
    # vrem sa identificam un link bazat pe un subeset de caractere si sa dam click pe el (Sub in loc de Submit)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Sub').click()
    time.sleep(2)

finally:
    print('Eliberam resursa driver')
    driver.quit()

