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
  - [Security & Privacy](#security--privacy)
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

***Step 1:*** Configure the `run_weakly.sh`:

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
sh run_weakly.sh
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

- The argument of **authors** and **titles** are the authors and titles you are interested, they should be separated by commas.
- The argument of **option** makes search results in the past `weak` or past `day`. 
- The argument of **path** is the path to save the result with csv file. You can discard this argument and the result will be saved in the project.

### Getting daily push

An example of steps to get daily push:

***Step 1:*** Configure the `run_daily.sh`:

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

Set daily push at 14:30 every afternoon with crontab:
```bash
crontab -e
# Write command below and save it 
# 30 14 * * * /bin/sh /home/<user_name>/customize-arXiv-push-master/run_daily.sh
crontab -l  # Check your command
```
If you would like to set another time, see https://crontab.guru/examples.html to change the command.

***Step 3:***
Find the daily reports at 14:30 every afternoon.

### Getting weakly push

***Step 1:*** Configure the `run_weakly.sh`:

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
Set weakly push at 10:50 every Friday morning with crontab:

```bash
crontab -e
# Write command below and save it 
# 50 10 * * 5 /bin/sh /home/<user_name>/customize-arXiv-push-master/run_weakly.sh
crontab -l  # Check your command
```

***Step 3:***
Find the weakly reports at 10:50 every Friday morning.

## Security & Privacy
We only provide a tool to help you find the papers you interested. 

It is your own responsibility to ensure the safety and privacy.

## Contributing & Contact

Feel free to contribute to our repository.

- If you woulk like to **correct mistakes**, please do it directly;
- If you have any **questions or advice**, please contact us by email (yuanjk@zju.edu.cn) or GitHub issues.

Thanks for your cooperation and contributions!