import csv
from selenium import webdriver
import time


if __name__ == "__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    with open('1.csv', 'r', encoding="utf-8-sig") as fr:
        reader = csv.reader(fr)
        index = 0
        for row in reader:
            index += 1
            print("\n", index,": ", row[0])
            driver.get(row[0])
            with open("FLRealtorList1.csv", 'a', encoding="utf-8-sig", newline='') as fw:
                writer = csv.writer(fw, lineterminator='\n')
                try:
                    info = (driver.find_elements_by_class_name("fa-ul")[0]).get_attribute("innerHTML")
                except:
                    continue
                if "Mobile" in info:
                    mobile = ((info.split("Mobile:")[1]).split('telephone">')[1]).split("</span>")[0]
                    print("mobile: ", mobile)
                else:
                    print("no mobile phone")
                    continue

                name = driver.find_element_by_class_name('modal-agent-name').get_attribute("innerHTML")
                print("name: ", name)
                location = driver.find_element_by_class_name('modal-agent-location').get_attribute("innerHTML").strip()
                print("location: ", location)
                try:
                    address = driver.find_element_by_xpath('//*[@itemprop="streetAddress"]').get_attribute("innerHTML")
                    print("address: ", address)
                except:
                    address = ""                
                try:
                    website = driver.find_element_by_xpath('//a[@itemprop="url"]').get_attribute("href")
                    print("website: ",website)
                except:
                    website = ""

                temp = []
                temp.append(name)
                temp.append(location)
                temp.append(mobile)
                temp.append(address)
                temp.append(website)
                writer.writerow(temp)