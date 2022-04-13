from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#import pdb;pdb.set_trace()
options = webdriver.ChromeOptions()

prefs = {
         #"download.default_directory" : child_dir,
         "profile.default_content_setting_values.notifications": 2 } #Note 1-to allow notification, 2- to block notification

options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(ChromeDriverManager().install());

driver.get("https://funkylife.in/good-morning-images/")
driver.maximize_window()

div_elem = driver.find_element_by_class_name("entry-content")
p_elem = div_elem.find_elements_by_tag_name('p')


for i in p_elem:
    print(i.text)
    print("\n")
    