import csv
from selenium import webdriver
import time


def get_data(driver, csv_header):
    with open("list3-4.csv", 'a', encoding="utf-8-sig", newline='') as fw:
        writer = csv.writer(fw, lineterminator='\n')    
        agent_urls = driver.find_elements_by_xpath('//*[@id="agent_list_wrapper"]/div/div[1]/a')
        experiences = driver.find_elements_by_xpath('//*[@id="agent_list_wrapper"]/div/div[3]')
        for i in range(0,len(agent_urls)):
            experience = experiences[i].get_attribute("innerHTML")
            if "Experience:" in experience and "year" in experience:
                year = ((experience.split("Experience:")[1]).split(" year")[0]).split("<strong>")[1]
                print("Year: ", year)
                if int(year) > 15:
                    continue
            else:
                continue
            temp = []
            temp.append(agent_urls[i].get_attribute("href"))
            writer.writerow(temp)


if __name__ == "__main__":
    target_url_first = "https://www.realtor.com/realestateagents/"
    target_url_last= "/photo-1/pg-"
    driver = webdriver.Chrome('chromedriver.exe')
    csv_header = ['Name','Phone','Email','Email', 'Website']
    zip_code = []
    with open('2.csv', 'r') as fr:
        reader = csv.reader(fr)
        for row in reader:
            zip_code.append(row[0])
    
    for z in zip_code:
        target_url = target_url_first + str(z) + target_url_last
        for i in range(3, 100):
            url = target_url + str(i)
            driver.get(url)
            time.sleep(2)
            try:
                exist = driver.find_element_by_xpath('//*[@id="agent_list_wrapper"]/div[2]/div[1]/a')
                print("page exist")
            except:
                print("no such page")
                break
            get_data(driver, csv_header)
    driver.close()