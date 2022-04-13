from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
# driver.maximize_window()

div_id=driver.find_element_by_id("beautiful-soup-documentation")
p_elem = div_id.find_elements_by_tag_name('p')

for i in p_elem:
    print(i.text)
    print("\n")

div_id1=driver.find_element_by_id("miscellaneous")
p_elem1 = div_id1.find_elements_by_tag_name('p')
for i in p_elem1:
    print(i.text)
    print("\n")
