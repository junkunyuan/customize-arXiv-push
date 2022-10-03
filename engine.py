# -----------------------------------------------------------------
# Customize arXiv push
# Engine for crawler and search
# Written by Junkun Yuan
# -----------------------------------------------------------------

import os
import csv
import time
from bs4 import BeautifulSoup
import urllib.request as request


class ArxivSearchEngine():
    """Simple crawler and search engine for arXiv."""
    def __init__(self, args):
        self.url = f'https://arxiv.org/list/{args.subject}/pastweek?show=10000'
        
        # Open the url
        try:
            self.page = request.urlopen(self.url)
        except:
            raise Exception(f'Fail to access {self.url}, please check it!')

        # Get all the html page
        self.soup = BeautifulSoup(self.page, 'html.parser')

        # Get the info part
        self.info = self.soup.find(id='dlpage')

        if (args.path is not None) and (os.path.exists(args.path)):
            self.file_dir = args.path
        else:
            self.file_dir = os.path.dirname(__file__)
            print('=> Path is None or does not exist! Save results in the project.')
        
        self.time = time.strftime("-%Y-%m-%d", time.localtime()) 
    
    def extract_info(self, args):
        """Extract info of field, number, date, url, title, author, subject."""
        print(f'\n=> To get arXiv info from <{self.url}>')
        # Get field
        self.field = self.info.find('h1').text

        # Get the number of papers per day 
        papers_per_day = self.info.find_all('dl')
        self.papers_per_day = [len(papers_per_day[i].find_all('dd')) for i in range(len(papers_per_day))]

        # Get date list
        dates_ = self.info.find_all('h3')
        self.dates_ = [dates_[i].text for i in range(len(dates_))]
        self.dates = []
        for i in range(len(self.dates_)):
            self.dates = self.dates + [self.dates_[i]] * self.papers_per_day[i]

        # Get paper urls
        urls = self.info.find_all('a', title='Abstract')
        self.urls = ['https://arxiv.org' + urls[i]['href'] for i in range(len(urls))]

        # Get titles
        titles = self.info.find_all(class_='list-title mathjax')
        self.titles = [titles[i].text[8:-1] for i in range(len(titles))]

        # Get authors
        authors = self.info.find_all(class_='list-authors')
        self.authors = [authors[i].text[10:-1].replace('\n', '') for i in range(len(authors))]

        # # Get abstracts
        # self.abstracts = []
        # for i in range(len(self.urls)):
        #     page = request.urlopen(self.urls[i])
        #     soup = BeautifulSoup(page, 'html.parser')
        #     abstract = soup.find(class_='abstract mathjax')
        #     self.abstracts.append(abstract.text)
        # print(self.abstracts)

        # Get primary subject
        subjects = self.info.find_all(class_='primary-subject')
        self.subjects = [subjects[i].text for i in range(len(subjects))]

        # Get number of paper in the past day/weak
        self.paper_num = {'day': self.papers_per_day[0], 'weak': len(self.urls)}

        def save_papers(subject, option='week'):
            csv_file = '-papers_past_' + option + self.time + '.csv'
            save_path = os.path.join(self.file_dir, subject + csv_file)
        
            with open(save_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([self.field])
                writer.writerow(['Number', 'Date', 'Title', 'Authors', 'Url', 'Primary subject'])
                for i in range(self.paper_num[option]):
                    writer.writerow([str(i + 1), self.dates[i], self.titles[i], self.authors[i], self.urls[i], self.subjects[i]])
            
            print(f'=> Save papers in the past {option} to <{save_path}>')

        # Save info in past week and past day
        save_papers(args.subject, option=f'{args.option}')

    def search_author(self, args, keywords):
        """Search interested authors."""

        print(f'\n=> Search interested authors of <{args.authors}> on {args.subject} in the past {args.option} ...')
        
        search_result = {keyword: [] for keyword in keywords}
        
        # Search authors
        author_str = ''
        for keyword in keywords:
            author_str = author_str + keyword + ', '
            for i, authors in enumerate(self.authors[:self.paper_num[args.option]]):
                if keyword.lower() in authors.lower():
                    search_result[keyword].append(i)

        # Save papers of interested authors
        save_path = os.path.join(self.file_dir, args.subject + f'-authors-past_{args.option}{self.time}.csv')

        with open(save_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([f'Intested authors of {author_str}'])
            writer.writerow(['Interested', 'Number', 'Dates', 'Titles', 'Authors', 'Url', 'Primary subjects'])
            for keyword in keywords:
                print(f'=> Found {len(search_result[keyword])} papers of {keyword}!')
                for i in search_result[keyword]:
                    writer.writerow([keyword, str(i + 1), self.dates[i], self.titles[i], self.authors[i], self.urls[i], self.subjects[i]])
        print(f'=> Save papers of interested authors to <{save_path}>')

    def search_title(self, args, keywords):
        """Search interested titles."""

        print(f'\n=> Search interested titles of <{args.titles}> on {args.subject} in the past {args.option} ...')
        
        search_result = {keyword: [] for keyword in keywords}

        # Search titles
        keyword_str = ''
        for keyword in keywords:
            keyword_str = keyword_str + keyword + ', '
            for i, title in enumerate(self.titles[:self.paper_num[args.option]:]):
                if keyword.lower() in title.lower():
                     search_result[keyword].append(i)

        # Save papers of interested titles
        save_path = os.path.join(self.file_dir, args.subject + f'-titles-past_{args.option}{self.time}.csv')

        with open(save_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([f'Intested titles of keywords {keyword_str}'])
            writer.writerow(['Interested', 'Number', 'Dates', 'Titles', 'Authors', 'Url', 'Primary subjects'])
            for keyword in keywords:
                print(f'=> Found {len(search_result[keyword])} papers of {keyword}!')
                for i in search_result[keyword]:
                    writer.writerow([keyword, str(i + 1), self.dates[i], self.titles[i], self.authors[i], self.urls[i], self.subjects[i]])
        
        print(f'=> Save papers of interested titles to <{save_path}>')
    
    # def search_abstract(args, keywords):
