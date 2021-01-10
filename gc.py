import requests,re,bs4
cnt = 1
inf = input('국민청원 댓글읽기 프로그램\n제작 : 이현록\n깃허브 아이디 : Eos0510\n국민청원 링크 입력 : ')
if 'page' in inf : inf = inf[0:50]
while(True):
    rp = requests.get(inf+'?page='+str(cnt)).text
    a = re.compile('href="(.*)";').search(rp)
    if a != None: rp = requests.get(a.group(1)).text
    soup = bs4.BeautifulSoup(rp, 'html.parser').findAll('div', {'class':'R_R_contents_txt'})
    cnt += 1
    for i in soup:
        t = i.text.strip()
        if t == '동의합니다' or t == '동의합니다.': continue
        else : print(t)