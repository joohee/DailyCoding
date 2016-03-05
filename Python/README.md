# Python 

This directory is for pythong programming. 

### Directories
- packages
   - utils : some utils to help your programming.
   - aws : functions related with AWS.
   - book : functions related with BOOK db (search, ...)

```
├── check_disk.py : check disk storage and send a push notification if usage is larger than usage_limit.
├── packages
│   ├── __init__.py
│   ├── aws
│   │   ├── __init__.py
│   │   └── sns.py : send push notification using AWS SNS.
│   ├── book
│   │   ├── __init__.py
│   │   └── search_by_isbn13.py : search a BOOK by isbn no. (API server is from Daum.)
│   └── utils
│   │   ├── __init__.py
│   │   ├── crawl_from_url_and_save_to_file.py : find file from url and save to the directory.
│   │   ├── crawl_with_options.py : used python option parameters.
│   │   ├── df.py : *nix command df parser. 
│   │   └── word_count_in_file.py : word count of a specific file. 
├── pdf
│   ├── numpy
│   │   ├── assets/
│   │   ├── scipy_tutorial.py : scipy examples
│   │   └── tutorial.py : numpy examples
│   ├── python_for_finance (book)
│   │   └── chapter1.py 
│   └── python_for_secret_agents (book)
│       ├── bit_byte_calculator.py
│       ├── chapter2.py
│       ├── chapter3.py
│       ├── chapter4.py
│       └── chapter5.py
├── tips : python tips
│   ├── decorator.py : decorator annotation examples.
│   └── kind_of_methods.py : static method, class method example.
└── works : used to workplace.
    └── push
        ├── config.json.sample : push config file.
        ├── push_filename.sample : push token file.
        ├── section_push.py : sample file to push notification using send_push.py.
        ├── send_push.py : send push function.
        ├── sns.py : AWS SNS function.
        └── sns_config.ini : sns.py config file.


```

- test : test files with unittest lib.
```
├── unittest_basic.py
├── unittest_expected_failure.py
├── unittest_inner_functions.py
├── unittest_sample.py
├── unittest_skip.py
└── unittest_subtest.py

```

- environment : use anaconda
   - http://conda.pydata.org/docs/using/envs.html
