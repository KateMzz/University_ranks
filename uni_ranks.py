from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from lxml import etree
import pandas as pd



class InforgramDowloader:
    option = webdriver.ChromeOptions()
    # pls change the directory of your webdriver and switch '\' to '/'
    browser = webdriver.Chrome(executable_path=r"C:/Users/Downloads/chromedriver_win32 (2)/chromedriver.exe") 
    print('driver was opened')
    time.sleep(1)
    browser.get("https://infogram.com/quant-guide-table-2021-main-list-1hnp27mmx5d9n2g")
    print('got the link')
    time.sleep(1)
    file = browser.find_element_by_link_text("Download data")
    file.click()
    print('data.csv was downloaded')
    time.sleep(2)
    browser.close()


def tfetimes():
    url='https://tfetimes.com/best-financial-engineering-program-rankings/'
    page=requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    dom = etree.HTML(str(soup))
    rankss = []
    university_names=[]
    university_links=[]
    for rank in dom.xpath("//td[@class='column-1']/text()"):
        rankss.append(rank)
    for u in dom.xpath("//td[@class='column-2']/a"):
        university_name = u.xpath("text()")
        university_link = u.xpath("@href")
        str1 = ''.join(university_name)
        str2 = ''.join(university_link)
        university_names.append(str1)
        university_links.append(str2) 
    ranks={
        'ranks':rankss,
        'university_name': university_names,
        'university_link': university_links
    }
    return ranks

(pd.DataFrame.from_dict(data=tfetimes(), orient='columns')
# pls change the directory and switch '\' to '/'
   .to_csv('C:/Users/Downloads/data_tfetimes.csv', header=True, index=False))
print('tfetimes.csv was created')


def quantnet():
    url = 'https://quantnet.com/mfe-programs-rankings/'
    page=requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    data = etree.HTML(str(soup))
    ranking_total = data.xpath("//tbody/tr")
    for row in ranking_total:  
        rankk = row.xpath("//td/span/text()")
        rank =' '.join(rankk).split()
        uni_name = row.xpath("//td/b/text()")
        program = row.xpath("//td/a/text()")
        program_url = row.xpath("//td/a/@href")
        program_location = row.xpath("//td/i/text()")
        total_score = row.xpath("//td[3]/text()")
        peer_assessment = row.xpath("//td[4]/text()")
        emplm_rate_grad = row.xpath("//td[5]/text()")
        emplm_rate_three_month_aft = row.xpath("//td[6]/text()")
        avr_start_salary_bonus = row.xpath("//td[7]/text()")
        avr_gre_quant = row.xpath("//td[8]/text()")
        tuition = row.xpath("//td[9]/text()")
        cohort_size = row.xpath("//td[10]/text()")
        ranks={
            'rank': rank,
            'uni_name': uni_name,
            'program': program,
            'program_url': program_url,
            'program_location': program_location,
            'total_score': total_score,
            'peer_assessment': peer_assessment,
            'emplm_rate_grad': emplm_rate_grad,
            'emplm_rate_3_month_aft': emplm_rate_three_month_aft,
            'avr_start_salary_bonus': avr_start_salary_bonus,
            'avr_gre_quant': avr_gre_quant,
            'tuition': tuition,
            'cohort_size': cohort_size 
        }   
        return ranks

ranks = quantnet()
def pad_dict_list(ranks, padel):
    lmax = 0
    for lname in ranks.keys():
        lmax = max(lmax, len(ranks[lname]))
    for lname in ranks.keys():
        ll = len(ranks[lname])
        if  ll < lmax:
            ranks[lname] += [padel] * (lmax - ll)
    return ranks
        
(pd.DataFrame.from_dict(data=pad_dict_list(ranks, padel='-'), orient='columns')
# pls change the directory and switch '\' to '/'
    .to_csv('C:/Users/Downloads/data_quantnet.csv', header=True, index=False))
print('quantnet.csv was created')


# Merge multiple files with 

# Linux:
# sed 1d data_*.csv > merged_ranks.csv


# Windows:
# type data*.csv > merged_ranks.csv

