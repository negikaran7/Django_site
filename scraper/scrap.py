from mathematicians import simple_get
raw_html = simple_get('https://realpython.com/blog/')
len(raw_html)


no_html = simple_get('https://realpython.com/blog/nope-not-gonna-find-it')
no_html is None


from bs4 import BeautifulSoup
raw_html = open('contrived.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
for p in html.select('p'):
    if p['id'] == 'walrus':
        print(p.text)