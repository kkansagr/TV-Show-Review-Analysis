# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
from requests import get

tvshows=["the office","arrow","daredevil","the flash","the 100","outlander","parks and recreation","breaking bad","house of cards","this is us","sex and the city","game of thrones","the vampire diaries","teen wolf","hannibal","the walking dead","the haunting of hill house","riverdale","sherlock","how to get away with murder","dexter","the wire","suits","sense8","altered carbon","gotham","the big bang theory","orange is the new black","stranger things"]

f=open("season.csv","a")
for name in tvshows:
    ratings=[]
    url = 'https://www.rottentomatoes.com/tv/'+ name.replace(' ','_')
    
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    season_info = html_soup.find_all('div', class_='bottom_divider media seasonItem')
    for season in season_info:
        try:
            rating = season.find('span', class_='meter-value').text.strip()
            if rating!='0':
                ratings.append(rating)
                rating= rating.strip('%')
        except AttributeError:
            rating='0'

    print(ratings)
    
    
    imdburl= 'https://www.imdb.com/search/title?title='+name.replace(' ','+')
    imdbresponse=get(imdburl)
    iihtml_soup = BeautifulSoup(imdbresponse.text, 'html.parser')
    
    sp= iihtml_soup.find('h3','lister-item-header').a['href']
    name=iihtml_soup.find('h3','lister-item-header').a.text
    print(name)
    sp=sp.split('/')
    
    iurl = 'https://www.imdb.com/title/'+ sp[2] + '/episodes?'
    
    iresponse = get(iurl)
    ihtml_soup = BeautifulSoup(iresponse.text, 'html.parser')
    
    season_nav = ihtml_soup.find('select', {"id": "bySeason"}).find_all('option')
    
    s=[]
    
    for season in season_nav:
        s.append(season.text.strip())
    print(s)
    
    avgr=[]
    for j in s:
        f.write(name+ ", ")
        f.write(j+", ")
        try:
            f.write(str(ratings[int(j)-1])+", ")
        except IndexError:
            f.write(",")
        odds=[]
        evens=[]
        d='https://www.imdb.com/title/'+ sp[2] + '/episodes?'+'season='+j
        html=BeautifulSoup(get(d).text, 'html.parser')
        
        odd = html.find_all('div', class_='list_item odd')
        
        for j in odd:
            bb=j.find('div', class_='ipl-rating-star').find('span', class_='ipl-rating-star__rating').text
            if bb!='0':
                odds.append(bb)
            
        even = html.find_all('div', class_='list_item even')
        
        for jj in even:
            bb1=jj.find('div', class_='ipl-rating-star').find('span', class_='ipl-rating-star__rating').text
            if bb1 != '0':
                evens.append(bb1)
        
        odds=[float(i) for i in odds]
        evens=[float(i) for i in evens] 
        epr = [""]*(len(odds)+len(evens))
        epr[::2] = odds
        epr[1::2] = evens
        print(len(epr))
        try:
            avg=sum(epr)/len(epr)
        except ZeroDivisionError:
            avg=0
        avg=round(avg,2)
        avgr.append(avg)
        if avg != 0.0:
            f.write(str(avg)+", ")
        for i in epr:
            if i!=0.0:
                f.write(str(i)+ ", ")
        f.write("\n")
    print(avgr)
    f.write("\n")

f.close()

