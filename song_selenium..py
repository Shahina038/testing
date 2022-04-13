from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#import pdb;pdb.set_trace()
driver.get("https://www.songlyrics.com/index.php?section=search&searchW=westlife&submit=Search")
time.sleep(3)

div_elem=driver.find_elements_by_class_name("serpresult")
#print(len(div_elem))

for i in div_elem[0:1]:
    a_tag = i.find_elements_by_tag_name('a')
    song_name = a_tag[1].text
    print(song_name)
    a_tag[1].click()
    time.sleep(3)
    p_elem = driver.find_element_by_id("songLyricsDiv")
    print(p_elem.text)
  
    





