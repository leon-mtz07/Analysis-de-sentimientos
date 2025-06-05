from link import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Inicializamos el navegador
web = webdriver.Chrome()

# Link del café de google maps
url = link

# Le damos el link al objeto
web.get(url)

comments = web.find_elements(by=By.CLASS_NAME, value='wiI7pd')
data = []

for comment in comments:
    data.append(comment.get_attribute('innerHTML'))

comment_df = pd.DataFrame({'Comentarios': data})
comment_df.to_csv('comentarios.csv', index=False)