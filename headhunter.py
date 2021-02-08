import requests
from bs4 import BeautifulSoup

URL="https://hh.ru/search/vacancy?text=%D0%B1%D0%B8%D0%B7%D0%BD%D0%B5%D1%81-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA"
headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Mozilla/5.0',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive',
  }


  
def extract_max_page():
  
  hh_request = requests.get(f'{URL}&page=0',headers=headers)
  hh_soup = BeautifulSoup(hh_request.text, 'html.parser')
  pages=[]
  paginator=hh_soup.find_all("span",{'class':'pager-item-not-in-short-range'})
  for page in paginator:
    pages.append(int(page.find('a').text))
  return pages[-1]

def extract_job(html):
  title=html.find('a').text
  link = html.find('a')['href']
  company= html.find('div',{'class':'vacancy-serp-item__meta-info-company'}).text
  company = company.strip()
  location = html.find('span',{'data-qa':'vacancy-serp__vacancy-address'}).text
  return {'title':title,'company':company, 'location':location, 'link':link}

def extract_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    print(f'HeadHunter: Парсинг страницы: {page}')
    result=requests.get(f'{URL}&page={page}', headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    results=soup.find_all("div", {'class':'vacancy-serp-item'})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
    

  return jobs

def get_jobs():
  max_page= extract_max_page()
  jobs = extract_jobs(max_page)
  return jobs

  