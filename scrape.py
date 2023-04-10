# import os,sys
# import time
# import xlwt
# import xlrd as xl
# import datetime
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver import ActionChains                   # For click Enter from keyboard
# from selenium.webdriver.common.keys import Keys               # ------ upper same -----------
# from selenium.common.exceptions import NoSuchElementException # For treat error finding element
# from selenium.webdriver.common.by import By                   # For find elemet
# from selenium.webdriver.support.ui import WebDriverWait       # For wait until display element
# from selenium.webdriver.support import expected_conditions as EC # ---- upper same -----------
# from selenium.webdriver.support.ui import Select              # For option select
# ## -- write excel --------

# present = os.path.dirname(os.path.abspath(__file__))
# service = webdriver.chrome.service.Service(os.path.abspath(present+"/chromedriver"))
# service.start()
# option = webdriver.ChromeOptions()
# option.add_argument("--window-size=1200,700")
# driver = webdriver.Chrome(present+"/chromedriver", options = option) 
# url = 'https://www.bet365.gr/#/IP/EV15550241432C1'
# driver.get(url)

# def scrapeData(start,end, workbook, sheet, driver) :
#     # present = os.path.dirname(os.path.abspath(__file__))
#     # service = webdriver.chrome.service.Service(os.path.abspath(present+"/chromedriver"))
#     # service.start()
#     # option = webdriver.ChromeOptions()
#     # option.add_argument("--window-size=1200,700")
#     # driver = webdriver.Chrome(present+"/chromedriver",options = option) 
#     # url = 'https://www.flashscore.com/'
#     # driver.get(url)
#     # time.sleep(5)
#     # schedulbutton = driver.find_elements_by_class_name('tabs__text.tabs__text--default')[2]
#     # schedulbutton.click()
#     # time.sleep(2)
#     event = driver.find_element_by_class_name('event')
#     sportName = event.find_element_by_class_name('sportName.soccer')
#     # aceptbutton = driver.find_element_by_id('onetrust-button-group')
#     # time.sleep(1)
#     # aceptbutton.click()
#     # time.sleep(3)
#     srcwin = driver.window_handles[0]
#     # matchs = sportName.find_elements_by_class_name('event__time')
#     matchs = sportName.find_elements_by_class_name('event__participant.event__participant--home')
#     # print('event_time len :',len(matchs))
#     ## -- Read excel --------                            
#     loc = "football.xls" 
#     wb = xl.open_workbook(loc)                    
#     s1 = wb.sheet_by_index(0)
#     rownum = s1.nrows +1
#     print("No. of rows:", s1.nrows)               
#     print("No. of columns:", s1.ncols)    
#     for m in range(start,end): # len(matchs)        
#         time.sleep(0.5)
#         match = matchs[m]
#         actions = ActionChains(driver)
#         actions.move_to_element(match).perform()
#         time.sleep(1)
#         match.click()
#         time.sleep(3)
#         chwin = driver.window_handles[1]
#         # --- to switch focus the child window handle
#         driver.switch_to.window(chwin)
#         print('-child windows url:',driver.current_url)
#         churl = driver.current_url
#         ## ------ child windows ----------
#         des = driver.find_element_by_class_name('description')
#         country = des.find_element_by_class_name('description__country').text
#         dateval = driver.find_element_by_id('utime').text
#         print('date :',dateval,'country:',country)
#         homeName = driver.find_element_by_class_name('team-text.tname-home').text
#         awayName = driver.find_element_by_class_name('team-text.tname-away').text
#         li1 = driver.find_elements_by_class_name('ifmenu')[0]
#         standingbutton = li1.find_element_by_class_name('li4')
#         print('-standingbutton check :',standingbutton.text)
#         if 'Standings' in standingbutton.text: 
#             standingbutton.click()
#             time.sleep(2)       
#             ## ---- click sub standing button -----
#             tabgroup = driver.find_element_by_class_name('tabs__group') 
#             tabs = tabgroup.find_elements_by_class_name('tabs__tab')
#             for b in range(len(tabs)) :
#                 if 'Standings' == tabs[b].text :      
#                     standingbutton2 = tabs[b]
#                     standingbutton2.click()
#                     time.sleep(1)
#                     break
#             subtag = driver.find_element_by_class_name('subTabs')
#             homebutton = subtag.find_elements_by_class_name('subTabs__tab')[1]
#             awaybutton = subtag.find_elements_by_class_name('subTabs__tab')[2]
#             ## ------- finding hometeam row ----
#             homebutton.click()
#             time.sleep(1)
#             homecontent = driver.find_element_by_class_name('tableWrapper___1No5ozH')
#             rows = homecontent.find_elements_by_class_name('row___S6WkQ8-.row___3Gv59rA')
#             for i in range(len(rows)):
#                 teamName = rows[i].find_element_by_class_name('rowCellParticipantName___2pCMCKl').text
#                 if teamName == homeName :
#                     H_MPval = rows[i].find_elements_by_class_name('rowCell___1QFnPje.cell___2g1YNU6')[0].text
#                     H_Gval = rows[i].find_element_by_class_name('rowCell___1QFnPje.cellScore___2hJ0b9o').text
#                     print('H_MPval :',H_MPval,'H_Gval :',H_Gval)
#                     HMP, HG1, HG2 = int(H_MPval), int(H_Gval.split(':')[0]), int(H_Gval.split(':')[1])
#                     break
#             ## ------- finding awayteam row ----
#             time.sleep(1)
#             awaybutton.click()
#             time.sleep(1)
#             awaycontent = driver.find_element_by_class_name('tableWrapper___1No5ozH') # tableWrapper___1No5ozH
#             rows = awaycontent.find_elements_by_class_name('row___S6WkQ8-.row___3Gv59rA') # row___S6WkQ8- row___3Gv59rA  
#             for i in range(len(rows)):
#                 teamName = rows[i].find_element_by_class_name('rowCellParticipantName___2pCMCKl').text # rowCellParticipantName___2pCMCKl
#                 if teamName == awayName :
#                     A_MPval = rows[i].find_elements_by_class_name('rowCell___1QFnPje.cell___2g1YNU6')[0].text # rowCell___1QFnPje cell___2g1YNU6 
#                     A_Gval = rows[i].find_element_by_class_name('rowCell___1QFnPje.cellScore___2hJ0b9o').text # rowCell___1QFnPje cellScore___2hJ0b9o 
#                     print('A_MPval :',A_MPval,'A_Gval :',A_Gval)
#                     AMP, AG1, AG2 = int(A_MPval), int(A_Gval.split(':')[0]), int(A_Gval.split(':')[1])
#                     break
#             ## --------- show result -------
#             print('---- result -------')
#             print(HMP/1, HG1/1, HG2/1, AMP/1, AG1/1, AG2/1)
#             homefor=HG1/HMP
#             homeagainst=HG2/HMP
#             awayfor=AG1/AMP
#             awayagainst=AG2/AMP
#             homescore=(homefor+awayagainst)/2
#             awayscore=(awayfor+homeagainst)/2
#             print(str(homescore))
#             print(str(awayscore))    
#             ## ---- write excel row ---------
#             sheet.write(rownum, 0, dateval) 
#             sheet.write(rownum, 1, homeName) 
#             sheet.write(rownum, 2, awayName)
#             sheet.write(rownum, 3, str(homescore))
#             sheet.write(rownum, 4, str(awayscore))
#             workbook.save("football.xls")
#             driver.close()
#             driver.switch_to.window(srcwin)
#             rownum +=1
#         else:
#             driver.close()
#             driver.switch_to.window(srcwin)
#     # driver.close()






from selenium import webdriver
import  bs4, time

driver = webdriver.Chrome()
url = 'https://mobile.bet365.com/#type=Splash;key=1;ip=0;lng=1'


driver.get(url)
driver.maximize_window()
# sleep is given so that JS populate data in this time
time.sleep(10)
pSource= driver.page_source

soup = bs4.BeautifulSoup(pSource, "html.parser")


# for data in soup.findAll('div',{'class':'eventWrapper'}):
#     for res in data.find_all('span') :
#         print res.text