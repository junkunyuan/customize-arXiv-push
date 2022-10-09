# -----------------------------------------------------------------
# Customize arXiv push
# Main file to run
# Written by Junkun Yuan
# -----------------------------------------------------------------

import argparse

from engine import ArxivSearchEngine

def set_config():
    parser = argparse.ArgumentParser('Customize your arXiv push', add_help=False)

    # Search parameters
    parser.add_argument('--subject', default='cs.CV', type=str, help='Subjects to search, choose by clicking the subjects in https://arxiv.org/')
    parser.add_argument('--authors', default=None, type=str, help='Interested authors to search, separated by commas')
    parser.add_argument('--titles', default=None, type=str, help='Interested titles to search, separated by commas')
    # parser.add_argument('--abstracts', default=None, type=str, help='Interested abstracts to search, separated by commas')
    parser.add_argument('--option', choices=['day', 'week'], type=str, help='Search results in the past day or week')
    
    parser.add_argument('--path', default=None, type=str, help='Path to save the result with csv file')

    return parser.parse_args()


def split_arg(_args):
    """Split args separated by commas."""
    return [arg.strip() for arg in _args.strip().split(',')]


if __name__ == '__main__':

    args = set_config()

    subjects = split_arg(args.subject)

    for subject in subjects:
        args.subject = subject
        
        # Create a crawler and search engine
        engine = ArxivSearchEngine(args)

        # Extract info and save it
        engine.extract_info(args)

        # Extract info of interested authors
        if args.authors is not None:
            keywords = split_arg(args.authors)
            engine.search_author(args, keywords)

        # Extract info of interested titles
        if args.titles is not None:
            keywords = split_arg(args.titles)
            engine.search_title(args, keywords)
        
        # # Extract info of interested abstracts
        # if args.abstracts is not None:
        #     abstracts = split_arg(args.abstracts)
        #     engine.search_abstract(args, abstracts)
