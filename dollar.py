import requests
import bs4

html = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')
soup = bs4.BeautifulSoup(html.text, 'html.parser')
dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.dw > strong

print(dollar.text)