from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome('/Users/srujithadevineni/web scrapping/chromedriver')
driver.get('https://www.google.co.in/')
box=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
driver.get('https://www.linkedin.com/')
 
# login credentials 

linkedin_username = "s.webscraping@gmail.com"

linkedin_password = "insert your password"

driver.find_element(By.XPATH,'//*[@id="session_key"]').send_keys(linkedin_username) 

driver.find_element(By.XPATH,'//*[@id="session_password"]').send_keys(linkedin_password) 

driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button').click() 
 
# import pandas lib as pd
import pandas as pd
 
# read by sheet of an excel file

dataframe1 = pd.read_excel('/Users/srujithadevineni/web scrapping/linkedin_project/108_data.xlsx')
d = dataframe1['Linkedin Link'].tolist()

#print("Convert dataframe to list:",d)
name_list=[]
clg_list=[]
place_list=[]
experience_list=[]


i=""

for i in d:
    try:
        driver.get(i)
        #try block for name
        try:
            name=driver.find_element(By.XPATH,("//h1[starts-with(@class,'text-heading-xlarge inline t-24 v-align-middle break-words')]")).text
            name_list.append(name)
      
        except:
            name_list.append("NA")
                   
           #try block for clg name              
        try:
            clg=driver.find_element(By.XPATH,("//div[starts-with(@class,'text-body-medium break-words')]")).text
            clg_list.append(clg)
        except:
            clg_list.append("NA")
               
             #try block for place name                       
        try: 
            place= driver.find_element(By.XPATH,("//span[starts-with(@class,'text-body-small inline t-black--light break-words')]")).text
            place_list.append(place)
        except:
            place_list.append("NA")    
                
       #try block for experience         
        try:
            if(driver.find_element(By.XPATH,("//span[starts-with(text(),'Experience')]"))):
                one_experience=driver.find_element(By.XPATH,("//div[starts-with(@class,'display-flex flex-wrap align-items-center full-height')]")).text
                experience_list.append(one_experience)
        except:
                experience_list.append('NA')   
            
    except:
        output='NA'#na= not found not valid
        name_list.append(output)
        clg_list.append(output)
        place_list.append(output)
        experience_list.append(output)
    
driver.quit()

table=pd.DataFrame({'Name':name_list,'collage':clg_list ,'place':place_list,'experience':experience_list})
excel_file='108_students_data.xlsx'
table.to_excel('108_students_data.xlsx')

