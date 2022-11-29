from selenium import webdriver 
from selenium.webdriver.common.keys import Keys #Nos deja usar el ENTER
import time
from selenium.webdriver.common.by import By #Nos deja refereciar elementos dentro de la web

PATH = "C:\Program Files (x86)\chromedriver.exe" 

driver = webdriver.Chrome(PATH) #abrimos con chrome la pagina

driver.get("https://magento.softwaretestingboard.com/") #link de la pagina
print(driver.title) #muestre en pantalla

search=driver.find_element(By.LINK_TEXT,"Sign In")
search.send_keys(Keys.RETURN)
IngresarEmail=driver.find_element(By.ID,"email")
user="bnovarese@uade.com" #Usuario
IngresarEmail.send_keys(user)
IngresarContraseña=driver.find_element(By.ID,"pass")
password="Fundamentalistastesting1999" #Contraseña
IngresarContraseña.send_keys(password)
IngresarContraseña.send_keys(Keys.RETURN)
time.sleep(10)

#driver.quit() #cierra pagina






