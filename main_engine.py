import csv
import urllib.request as request
from bs4 import BeautifulSoup
import chardet


class ArxivSearchEngine():
    """Simple crawler and search engine for arXiv."""
    def __init__(self, arxiv_url):
        self.arxiv_url = arxiv_url
        # Open the url
        try:
            self.page = request.urlopen(self.arxiv_url)
            print('Successfully access arXiv url')
        except:
            print('Fail to access arxiv url, it does not exist!!!')

        # Get all the html page
        self.soup = BeautifulSoup(self.page, 'html.parser')

        # Get the info part
        self.info = self.soup.find(id='dlpage')

    def extract_info(self, save_path=None):
        """Extract info of field, number, date, url, title, author, subject."""
        print('---------- To get arXiv info ----------')
        # Get field
        self.field = self.info.find('h1').text

        # Get number of papers per day 
        papers_per_day = self.info.find_all('dl')
        papers_per_day = [len(papers_per_day[i].find_all('dd')) for i in range(len(papers_per_day))]

        # Get dates
        dates_ = self.info.find_all('h3')
        dates_ = [dates_[i].text for i in range(len(dates_))]
        self.dates = []
        for i in range(len(dates_)):
            self.dates = self.dates + [dates_[i]] * papers_per_day[i]

        # Get paper urls
        urls = self.info.find_all('a', title='Abstract')
        self.urls = ['https://arxiv.org' + urls[i]['href'] for i in range(len(urls))]

        # Get titles
        titles = self.info.find_all(class_='list-title mathjax')
        self.titles = [titles[i].text[8:-1] for i in range(len(titles))]

        # Get authors
        authors = self.info.find_all(class_='list-authors')
        self.authors = [authors[i].text[10:-1].replace('\n', '') for i in range(len(authors))]

        # Get primary subject
        subjects = self.info.find_all(class_='primary-subject')
        self.subjects = [subjects[i].text for i in range(len(subjects))]
        
        # Save info
        if save_path:
            with open(save_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([self.field])
                writer.writerow(['Number', 'Date', 'Title', 'Authors', 'Url', 'Primary subject'])
                for i in range(len(self.urls)):
                    writer.writerow([str(i + 1), self.dates[i], self.titles[i], self.authors[i], self.urls[i], self.subjects[i]])
    
    def search_author(self, keywords, save_path=None):
        """Search interested authors."""
        print('---------- To search interested authors ----------')
        search_result = {keyword: [] for keyword in keywords}
        
        # Search authors
        author_str = ''
        for keyword in keywords:
            author_str = author_str + keyword + ', '
            for i, authors in enumerate(self.authors):        
                if keyword.lower() in authors.lower():
                    search_result[keyword].append(i)

        if save_path:
            with open(save_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([f'Intested authors of {author_str}'])
                writer.writerow(['Interested', 'Number', 'Dates', 'Titles', 'Authors', 'Url', 'Primary subjects'])
                for keyword in keywords:
                    print(f'Found {len(search_result[keyword])} papers of {keyword}!')
                    for i in search_result[keyword]:
                        writer.writerow([keyword, str(i + 1), self.dates[i], self.titles[i], self.authors[i], self.urls[i], self.subjects[i]])

    def search_title(self, keywords, save_path=None):
        """Search interested titles."""
        print('---------- To search interested titles ----------')
        search_result = {keyword: [] for keyword in keywords}

        # Search titles
        keyword_str = ''
        for keyword in keywords:
            keyword_str = keyword_str + keyword + ', '
            for i, title in enumerate(self.titles):
                if keyword.lower() in title.lower():
                     search_result[keyword].append(i)

        if save_path:
            with open(save_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([f'Intested titles of keywords {keyword_str}'])
                writer.writerow(['Interested', 'Number', 'Dates', 'Titles', 'Authors', 'Url', 'Primary subjects'])
                for keyword in keywords:
                    print(f'Found {len(search_result[keyword])} papers of {keyword}!')
                    for i in search_result[keyword]:
                        writer.writerow([keyword, str(i + 1), self.dates[i], self.titles[i], self.authors[i], self.urls[i], self.subjects[i]])