import requests
from bs4 import BeautifulSoup

# musinsa = requests.get("https://store.musinsa.com/app/contents/bestranking")
# musinsa_soup = BeautifulSoup(musinsa.text,'html.parser')


# num = []
# m_page = musinsa_soup.find_all("a",{"class":"paging-btn btn"})
# for page in m_page:
#     num.append(m_page.string)

# print(num)
# products = musinsa_soup.find("ul",{"class":"snap-article-list boxed-article-list article-list center list goods_small_media8"})
# productsImg = products.find_all("div",{"class":"list_img"})



indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text,'html.parser')

print(indeed_soup)
pagination = indeed_soup.find("div",{"class":"pagination"})

pages = pagination.find_all('a')
spans = []

for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])
