# CSC-510

[![DOI](https://zenodo.org/badge/529681582.svg)](https://zenodo.org/badge/latestdoi/529681582)
[![Build Status](https://github.com/rahulgautam21/CSC-510/actions/workflows/github-actions-build.yml/badge.svg)](https://github.com/rahulgautam21/CSC-510/actions)
[![GitHub Release](https://img.shields.io/github/release/rahulgautam21/CSC-510.svg)](https://github.com/rahulgautam21/CSC-510/releases)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/rahulgautam21/CSC-510.svg)](https://img.shields.io/github/repo-size/rahulgautam21/CSC-510.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/rahulgautam21/CSC-510)](https://github.com/rahulgautam21/CSC-510/graphs/contributors)
[![Open Issues](https://img.shields.io/github/issues/rahulgautam21/CSC-510)](https://github.com/rahulgautam21/CSC-510/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/rahulgautam21/CSC-510)](https://github.com/rahulgautam21/CSC-510/pulls)
![Supports Python](https://img.shields.io/pypi/pyversions/pytest)
[![codecov](https://codecov.io/gh/rahulgautam21/CSC-510/branch/main/graph/badge.svg?token=6QCOL7VZ2T)](https://codecov.io/gh/rahulgautam21/CSC-510)

# Fall 2022 CSC 510 (Group 40)
This is the code repo for Software Engineering group 40, a group of 6 people - Srilekha, Chetana, Shreya, Sarika, Rahul, Shubham.This repository was developed to demonstrate the various ideas we acquired while taking CSC 510 in the Fall of 22 at NC State University.

## Introduction
A Python program to read CSV files and provide column summaries (medians and standard deviation for numerics; mode and entropy for symbolic columns). The goal of this project is to translate the lua-to-python conversion of the source code found at [link](https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf).

## Homeworks
|Homework| Status| Task|
|:------:|:------|:------|
|HW2     |&check;|Get this going for the `Num` and `Sym` class (below) and the tests cases `the`, `sym`, `num`, `bignum`.|
|HW3     |&check;|Get this going for the `Cols`, `Row`, `Data` class and the test cases `eg.csv, eg.data, eg.stats`.|
|HW4     |&check;|Add all the bling from HW1. Also, add post-commit hooks to auto run all the test cases, the code coverage checks (if your language supports then), and the documentation generators.  For more on what kinds of documentation is acceptable, see [the web site from lecture1](https://user-images.githubusercontent.com/29195/130997647-d933884e-8e5c-4f0c-a367-6a5d69bb1df1.png).|
|HW5     |&check;|For five other groups from cs510 (picked at random), apply the Project1 [rubric](https://github.com/txt/se22/blob/main/docs/proj1.md#rubric).  Important note: whatever scores you offer, these will **not** change the other group's scores.|

## Installation
To run the following source code, make sure you have the `auto93.csv` in the data folder.

For installing the additional requirements, execute the following command

``` pip install -r requirements.txt ```

Execute the following command:

``` python csv.py -e ALL```

### Command Line Arguments:

-e  --eg        start-up example                      = nothing  
-d  --dump      on test failure, exit with stack dump = false  
-f  --file      file with csv data                    = ../data/auto93.csv  
-h  --help      show help                             = false  
-n  --nums      number of nums to keep                = 512  
-s  --seed      random number seed                    = 10019  
-S  --seperator feild seperator                       = ,  

### Sample Output

``` 
python csv.py -e ALL

−−−−−−−−−−−−−−−−−----------------−−−−−−−−−−−−−−−−−−
!!!!!! PASS test_bignum True

−−−−−−−−−−−−−−−−−----------------−−−−−−−−−−−−−−−−−−
['Clndrs', 'Volume', 'Hp:', 'Lbs-', 'Acc+', 'Model', 'origin', 'Mpg+']
[8.0, 304.0, 193.0, 4732.0, 18.5, 70.0, 1.0, 10.0]
[8.0, 360.0, 215.0, 4615.0, 14.0, 70.0, 1.0, 10.0]
[8.0, 307.0, 200.0, 4376.0, 15.0, 70.0, 1.0, 10.0]
[8.0, 318.0, 210.0, 4382.0, 13.5, 70.0, 1.0, 10.0]
[8.0, 429.0, 208.0, 4633.0, 11.0, 72.0, 1.0, 10.0]
[8.0, 400.0, 150.0, 4997.0, 14.0, 73.0, 1.0, 10.0]
[8.0, 350.0, 180.0, 3664.0, 11.0, 73.0, 1.0, 10.0]
[8.0, 383.0, 180.0, 4955.0, 11.5, 71.0, 1.0, 10.0]
[8.0, 350.0, 160.0, 4456.0, 13.5, 72.0, 1.0, 10.0]
!!!!!! PASS test_csv True

−−−−−−−−−−−−−−−−−----------------−−−−−−−−−−−−−−−−−−
!!!!!! PASS test_data True

−−−−−−−−−−−−−−−−−----------------−−−−−−−−−−−−−−−−−−
51 31.007751937984494
!!!!!! PASS test_num True

−−−−−−−−−−−−−−−−−----------------−−−−−−−−−−−−−−−−−−
xmid= {'Clndrs': 4, 'Volume': 120, 'Model': 72, 'origin': 1.0}
xdiv= {'Clndrs': -1.55, 'Volume': -98.062, 'Model': 3.876, 'origin': 1.327}
ymid= {'Lbs-': 2506, 'Acc+': 14, 'Mpg+': 20}
ymid= {'Lbs-': -817.442, 'Acc+': 1.163, 'Mpg+': 7.752}
!!!!!! PASS test_stats True

−−−−−−−−−−−−−−−−−----------------−−−−−−−−−−−−−−−−−−
!!!!!! PASS test_sym True

−−−−−−−−−−−−−−−−−----------------−−−−−−−−−−−−−−−−−−
!!!!!! PASS test_the True
!!!!!! PASS ALL True
```

### Group Review (HW 5)
[Reviews](https://github.com/rahulgautam21/CSC-510/tree/main/docs/HW5_Reviews)

### Documentation 
[Docs](https://github.com/rahulgautam21/CSC-510/tree/main/docs/HW5_Reviews)

### License:
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/rahulgautam21/CSC-510/blob/main/LICENSE) for more details.


