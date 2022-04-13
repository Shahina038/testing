from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.songlyrics.com/index.php?section=search&searchW=westlife&submit=Search")
driver.maximize_window()
#import pdb;pdb.set_trace()
div_elem=driver.find_element_by_class_name("serpresult")
a_elem = div_elem.find_elements_by_tag_name('a')
for i in a_elem:                                                   
   i(1).click()
p_elem=driver.find_element_by_id("songLyricsDiv")
print(p_elem)
   



