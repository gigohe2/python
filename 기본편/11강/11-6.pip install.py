from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
# 구글에서 pypi 검색 후 다양한 pip 다운받기