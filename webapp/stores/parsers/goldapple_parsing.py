from selenium import webdriver
from selenium.webdriver.common.by import By

#option = Options()
#option.add_argument("--disable-infobars")
driver = webdriver.Firefox()

driver.get("https://goldapple.ru/makijazh/glaza/teni-dlja-vek")

title = driver.find_element(By.CLASS_NAME, "base").text
print(title)
#driver.find_element(By.CLASS_NAME, "button-primary modal-city-informer__btn modal-city-informer__btn_primary").click()

brand_name_list = driver.find_elements(By.CLASS_NAME, "catalog-brand-name-span")
product_name_list = driver.find_elements(By.CLASS_NAME, "catalog-product-name-span")

#for x in range(len(brand_name_list)):
#    print(brand_name_list[x].text)

for x in brand_name_list:
    print(x.text)
for x in product_name_list:
    print(x.text)

#element_brand_name =
#print(brand_name_list)
driver.quit()