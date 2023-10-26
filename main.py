from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
import tkinter
import customtkinter
import mysql.connector


#My sql connection
conn = mysql.connector.connect(host='localhost',password='Qwerty007$',user='root',database='securesurf')
cursor = conn.cursor()

def start_download():
    url()
    driver.execute_script("window.scrollTo(0,50)")
    #Website that to be searched.
    input_text = driver.find_element(By.ID, "site_rating_search")
    input_text.send_keys(a) 
   

    #Submit button - Search Website.
    submit_button = driver.find_element(By.CLASS_NAME, value="btn-search")
    submit_button.click()
    app.destroy()

    #Time Intervel to allow the website to get results.
    time.sleep(15)
    
    #obtaining the current URL to obtain informations We need
    get_url = driver.current_url


# Setup chrome driver
chrome_options = Options()
#chrome_options.add_argument("--headless=new")
chrome_options.add_argument('log-level=3')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True) #TO keep the Web browser Open. So, It won't close automatically.

#Ad-BLock Extension to block Ads.So,it wont interupt the automation
parent_path = os.getcwd()
path_to_extension = parent_path + r'\5.10.1_0'
chrome_options.add_argument('load-extension='+ path_to_extension);

driver = webdriver.Chrome(options=chrome_options)

#Root Website TO perform Search.
time.sleep(2)
driver.get("https://www.scam-detector.com/validator/")

time.sleep(2)  #Sleep intervel so the extension website pop-up can be terminated.

p = driver.window_handles[0]
c = driver.window_handles[1]
driver.switch_to.window(c)

driver.close()

driver.switch_to.window(p)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Secure Surf")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert Your Link",width=40,height=8,font=('Times New Roman',30,'bold'))
title.pack(padx=10,pady=10)

# Link Input
def url():
    global a
    a=link.get()
    print(a)
url_var= tkinter.StringVar() 
link= customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
url_var=str(url_var)
link.pack(padx=20,pady=20)


# Check Button
check = customtkinter.CTkButton(app,text="Check",command=start_download)
check.pack(padx=20,pady=10)

# Run app
app.mainloop()

score = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/p[2]/strong/span")
score=(score.text)

connection = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/ul/li[4]/p[2]/span")
connection=(connection.text)

creation_date = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/ul/li[1]/p[2]")
creation_date=(creation_date.text)

DomainBlacklistStatus = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/ul/li[3]/p[2]/span")
DomainBlacklistStatus=(DomainBlacklistStatus.text)

Description = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/p")
Description=(Description.text)

driver.quit()



# Our app frame
app2 = customtkinter.CTk()
app2.geometry("760x720")
app2.title("Secure Surf")

# Adding UI elements
customtkinter.CTkLabel(app2,text="Score :",font=("Lucida Fax",20,"bold")).place(x=40, y=20)
customtkinter.CTkLabel(app2,text=score,font=("Lucida Fax",20,"bold")).place(x=120, y=20)
if score=="100.0/100":
    customtkinter.CTkLabel(app2,text="✅",font=("Lucida Fax",20,"bold"),text_color='green').place(x=5, y=20)
else:
    customtkinter.CTkLabel(app2,text="❗",font=("Lucida Fax",20,"bold"),text_color='red').place(x=5, y=20)

customtkinter.CTkLabel(app2,text="Connection Type : ",font=("Lucida Fax",20,"bold")).place(x=40, y=60)
customtkinter.CTkLabel(app2,text=connection,font=("Lucida Fax",20,"bold")).place(x=250, y=60)

if connection=="Valid HTTPS Found":
    customtkinter.CTkLabel(app2,text="✅",font=("Lucida Fax",20,"bold"),text_color='green').place(x=5, y=60)
else:
    customtkinter.CTkLabel(app2,text="❗",font=("Lucida Fax",20,"bold"),text_color='red').place(x=5, y=60)

customtkinter.CTkLabel(app2,text="Domain Creation Date : ",font=("Lucida Fax",20,"bold")).place(x=5, y=100)
customtkinter.CTkLabel(app2,text=creation_date,font=("Lucida Fax",20,"bold")).place(x=280, y=100)

customtkinter.CTkLabel(app2,text="Domain Blacklist Status : ",font=("Lucida Fax",20,"bold")).place(x=5, y=140)
customtkinter.CTkLabel(app2,text=DomainBlacklistStatus,font=("Lucida Fax",20,"bold")).place(x=300, y=140)


customtkinter.CTkLabel(app2,text="Description : ",font=("Lucida Fax",20,"bold")).place(x=5, y=180)
customtkinter.CTkLabel(app2,text=Description,font=("Lucida Fax",20,"bold"),wraplength=600).place(x=150, y=180)



# Check Button
check = customtkinter.CTkButton(app2,text="Quit",command=app2.destroy,font=("Lucida Fax",20,"bold")).place(x=300, y=400)

# Run app
app2.mainloop()
sql_query = """INSERT INTO websites (sites) VALUES (%s)"""
record = (a)
cursor.execute(sql_query,record)
connection.commit()
cursor.close()
connection.close()

