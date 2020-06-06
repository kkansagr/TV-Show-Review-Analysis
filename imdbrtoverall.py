from bs4 import BeautifulSoup
from requests import get

tvshows=["the office","arrow","daredevil","the flash","the 100","outlander","parks and recreation","breaking bad","house of cards","this is us","sex and the city","game of thrones","the vampire diaries","teen wolf","hannibal","the walking dead","the haunting of hill house","riverdale","sherlock","how to get away with murder","dexter","the wire","suits","sense8","altered carbon","gotham","the big bang theory","orange is the new black","stranger things"]
tvshowsr=[]
tvshowsi=[]
for i in tvshows:
    tvshowsr.append(i.replace(' ','_'))

print(tvshowsr)
f= open("rtv.csv","w+")
f.write("TV Show name,")
f.write("IMDB rating,")
f.write("Critic score,")
f.write("Audience score\n")
for j in tvshowsr:
    print(j)
    names = []
    ratings = []
    url = 'https://www.rottentomatoes.com/tv/'+ j
    imdburl= 'https://www.imdb.com/search/title?title='+ j.replace('_','+')
    response = get(url)
    imdbresponse=get(imdburl)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    ihtml_soup = BeautifulSoup(imdbresponse.text, 'html.parser')

    movie_containers = ihtml_soup.find_all('div', class_='lister-item mode-advanced')
    first_movie = movie_containers[0]
    first_name = first_movie.h3.a.text
    first_imdb = float(first_movie.strong.text)

    title = html_soup.find('div', class_ = 'seriesHeader')
    cr = html_soup.find('span', class_ = 'meter-value superPageFontColor')
    a=html_soup.find('div', class_ = 'meter-value')
    ar = html_soup.find('span', class_ = 'superPageFontColor')
    t=title.h1.text.strip()
    rate=cr.span.text
    arate=a.span.text

    f.write("%s,%2.f,%s,%s\n" % (first_name,first_imdb,rate,arate))
f.close()



