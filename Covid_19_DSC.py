from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(2000)
driver.get("https://www.mohfw.gov.in/")

python_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/button").click()

for i in range(1,23):
    istring = int(i)
    state_Name = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[%s]/td[2]"%(istring)).text
    confirmed_Case = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[%s]/td[3]"%(istring)).text
    f_Nationals = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[%s]/td[4]"%(istring)).text
    cured_patients = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[%s]/td[5]"%(istring)).text
    death_case = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[%s]/td[6]"%(istring)).text
    print("State Name : %s || Confirmed Case : %s || Foreign Nationals : %s || Cured Patients : %s || Deaths : %s" %(state_Name,confirmed_Case,f_Nationals,cured_patients,death_case))


total_CC = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[24]/td[2]/strong").text
total_FC = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[24]/td[3]/strong").text
total_cured = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[24]/td[4]/strong").text
total_deaths = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/strong/div[2]/div/table/tbody/tr[24]/td[5]/strong").text
print("Total Cases : %s || Total Foreign Cases : %s || Total Cured : %s || Total Deaths : %s" %(total_CC,total_FC,total_cured,total_deaths))

driver.quit()
