from sympy import arg
from main_engine import ArxivSearchEngine

import argparse

subject_list = {
    'cs.CV': 'https://arxiv.org/list/cs.CV/pastweek?show=10000', 
    'cs.LG': 'https://arxiv.org/list/cs.LG/pastweek?show=10000',
    'stat.ML': 'https://arxiv.org/list/stat.ML/pastweek?show=10000', 
    'cs.AI': 'https://arxiv.org/list/cs.AI/pastweek?show=10000',
    'cs.CL': 'https://arxiv.org/list/cs.CL/pastweek?show=10000', 
    }

def set_config():
    parser = argparse.ArgumentParser('Run', add_help=False)

    parser.add_argument('--subject', default='cv', type=str, help='Subject to search, choose from preset list or customized url')

    parser.add_argument('--all_papers_path', default=None, type=str, help='If you set the (csv) path, it means that you would like to save all the papers')

    parser.add_argument('--authors', default=None, type=str, help='Interested authors to search')
    parser.add_argument('--author_path', default='interested_authors.csv', type=str, help='Path to save papers of interested authors')

    parser.add_argument('--titles', default=None, type=str, help='Interested titles to search')
    parser.add_argument('--title_path', default='interested_title.csv', type=str, help='Path to save papers of interested titles')

    parser.add_argument

    return parser.parse_args()

if __name__ == '__main__':
    args = set_config()

    if args.subject in subject_list:
        url = subject_list[args.subject]
    elif 'http' in args.subject:
        url = args.subject
    else:
        raise 'Wrong subject!' 
    
    # Create a crawler and search engine
    engine = ArxivSearchEngine(url)

    # Extract info of field, number, date, url, title, author, subject, and save the info if all_papers_path is set
    engine.extract_info(args.all_papers_path)

    # Extract info of interested authors
    keywords = args.authors.split(',')
    keywords = [keyword.strip() for keyword in keywords]
    engine.search_author(keywords, args.author_path)

    # Extract info of interested titles
    keywords = args.titles.split(',')
    keywords = [keyword.strip() for keyword in keywords]
    engine.search_title(keywords, args.title_path)
