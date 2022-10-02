# customize-arXiv-push
- It is an easy-to-use tool to customize your arXiv paper push.

- It can push arXiv papers of your interested authors and titles to your email every day/weak.   

- If you would like to contribute to our repository or have any questions/advice, see [Contributing & Contact](#contributing--contact).

## Contents
- [customize-arXiv-push](#customize-arxiv-push)
  - [Contents](#contents)
  - [Environment](#environment)
  - [Getting started](#getting-started)
  - [Contributing & Contact](#contributing--contact)

## Environment
We use Python to write the code.

We recommend you to use conda to configure the environment. 
```bash
conda install beautifulsoup4  # Install using conda
pip install beautifulsoup4  # Or using pip
```

## Getting started
Run the command below:
```bash
python main.py \
--subject ${SUBJECT} \
--all_papers_path ${PAPER_PATH} \
--authors ${AUTHORS} \
--author_path ${AUTHOR_PATH} \
--titles ${TITLES} \
--title_path ${TITLE_PATH}
```
Note:
- The *Code* of **SUBJECT** can be chosen from the following table. Or you can enter your own url. For example, you can set `SUBJECT="cs.CV"` or `SUBJECT="https://arxiv.org/list/math.PR/pastweek?show=10000"`.

| Subject | Code | Url |
| ---- | ---- | ---- |
| Computer Vision and Pattern Recognition | cs.CV | https://arxiv.org/list/cs.CV/pastweek?show=10000 |
| Machine Learning | cs.LG or stat.ML | https://arxiv.org/list/cs.LG/pastweek?show=10000 or https://arxiv.org/list/stat.ML/recent |
| Artificial Intelligence | cs.AI | https://arxiv.org/list/cs.AI/pastweek?show=10000 |
| Computation and Language | cs.CL | https://arxiv.org/list/cs.CL/pastweek?show=10000 |

- Set **PAPER_PATH** with a csv path, like `PAPER_PATH="./all_papers.csv"`, to save all the papers in the past week.
- Set **AUTHORS** with the authors you are interested, like `AUTHORS="Kaiming He, Yann LeCun, Ilya Sutskever, Geoffrey Hinton"`, separated by commas.
- Set **AUTHOR_PATH** with a csv path, like `AUTHOR_PATH="./interested_authors.csv"`, to save the papers of your interested authors.
- Set **TITLES** with the keywords you are interested, like `TITLES="Object Detection, Machine Translation, Multi-Agent, Pretrain"`
- Set **TITLE_PATH** with a csv path, like `TITLE_PATH="D:/interested_titles.csv"`, to save the papers of your interested titles.

## Contributing & Contact

Feel free to contribute to our repository.

- If you woulk like to **correct mistakes**, please do it directly;
- If you have any **questions or advice**, please contact us by email (yuanjk@zju.edu.cn) or GitHub issues.

Thank you for your cooperation and contributions!