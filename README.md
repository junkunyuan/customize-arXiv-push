# customize-arXiv-push
- It is an easy-to-use tool to customize your arXiv paper push.

- It can extract recent arXiv papers with your interested authors and titles.

- And push the information to your computer every day/weak.   

- If you would like to contribute to our repository or have any questions/advice, see [Contributing & Contact](#contributing--contact).

## Contents
- [customize-arXiv-push](#customize-arxiv-push)
  - [Contents](#contents)
  - [Environment](#environment)
  - [Getting started](#getting-started)
    - [Getting a push](#getting-a-push)
    - [Getting daily push](#getting-daily-push)
    - [Getting weakly push](#getting-weakly-push)
  - [Contributing & Contact](#contributing--contact)

## Environment
We use Python to write the code, and conda is recommended to configure the environment. 
```bash
conda install beautifulsoup4  # Install using conda
pip install beautifulsoup4  # Or using pip
```

## Getting started

### Getting a push

An example of steps to get a push of the papers in the past weak:
***Step 1:*** Configure the `run.sh`:
```bash
#!/bin/sh
# Please use absolute path
/home/<user_name>/anaconda3/envs/<env>/bin/python /home/<user_name>/customize-arXiv-push-master/main.py \
--subject "cs.LG, stat.ML, stat.TH" \
--authors "Donald B Rubin, Michael I. Jordan, Bernhard Schölkopf" \
--titles "Variational inference, Optimization, Kernel" \
--option weak \
--path /home/<user_name>/
```
***Step 2:*** Run 
```bash
sh run.sh
```

***Step 3:***

Find the reports at the path.

Note:
- The argument of **subject** is the *code* of the subject at https://arxiv.org/. For example, if you want to choose *Computer Vision and Pattern Recognition* (under Computer Science), you can click it and find the code of `cs.CV` in the opened url https://arxiv.org/list/cs.CV/recent. We list some popular code of AI below.

| Subject | Code |
| ---- | ---- |
| Computer Vision and Pattern Recognition | cs.CV |
| Machine Learning | cs.LG or stat.ML |
| Artificial Intelligence | cs.AI |
| Computation and Language | cs.CL |

- The argument of **authors** is the authors you are interested, they should be separated by commas.
- The argument of  **titles** is the keywords you are interested, they should be separated by commas.
- The argument of **option** chooses to search results in the past `weak` or past `day`. 
- The argument of **path** is the path to save the result with csv file. You can discard this argument and the result will be saved in the project.

### Getting daily push

An example of steps to get daily push:

***Step 1:*** Configure the `run.sh`:
```bash
#!/bin/sh
# Please use absolute path
/home/<user_name>/anaconda3/envs/<env>/bin/python /home/<user_name>/customize-arXiv-push-master/main.py \
--subject "cs.CV, cs.AI, cs.LG, stat.ML" \
--authors "Geoffrey Hinton, Kaiming He, Ross Girshick" \
--titles "Self-supervised, Detection, Segmentation " \
--option day \
--path /home/<user_name>/
```

***Step 2:***
An example of steps to get weakly push:

Set daily push at 14:30 every afternoon with crontab:
```bash
crontab -e
# Write command below and save it 
# 30 14 * * * /bin/sh /home/<user_name>/customize-arXiv-push-master/run.sh
crontab -l  # Check your command
```
If you would like to set another time, see https://crontab.guru/examples.html to change the command.

***Step 3:***
Find the daily reports at 14:30 every afternoon.

### Getting weakly push

***Step 1:*** Configure the `run.sh`:
```bash
#!/bin/sh
# Please use absolute path
/home/<user_name>/anaconda3/envs/<env>/bin/python /home/<user_name>/customize-arXiv-push-master/main.py \
--subject "cs.CL, cs.AI, cs.LG, stat.ML" \
--authors "Christopher D Manning, Ilya Sutskever" \
--titles "Translation, Pretrain, Summarization" \
--option weak \
--path /home/<user_name>/
```

***Step 2:***
Set weakly push at 9:10 every Friday afternoon with crontab:
```bash
crontab -e
# Write command below and save it 
# 50 10 * * 5 /bin/sh /home/<user_name>/customize-arXiv-push-master/run.sh
crontab -l  # Check your command
```

***Step 3:***
Find the weakly reports at 9:10 every Friday afternoon.

## Contributing & Contact

Feel free to contribute to our repository.

- If you woulk like to **correct mistakes**, please do it directly;
- If you have any **questions or advice**, please contact us by email (yuanjk@zju.edu.cn) or GitHub issues.

Thank you for your cooperation and contributions!