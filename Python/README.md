# Python 

This directory is for pythong programming. 

### Directories
- utils : some utils to help your programming.
- aws : functions related with AWS.
- book : functions related with BOOK db (search, ...)

```
├── __pycache__
├── check_disk.py
├── packages
│   ├── __init__.py
│   ├── aws
│   │   ├── __init__.py
│   │   └── sns.py : send push notification using AWS SNS.
│   ├── book
│   │   ├── __init__.py
│   │   └── search_by_isbn13.py : search a BOOK by isbn no. (API server is from Daum.)
│   └── utils
│       ├── __init__.py
├── crawl_from_url_and_save_to_file.py : find file from url and save to the directory.
    ├── crawl_with_options.py : used python option parameters.
    ├── df.py : *nix command df parser. 
    └── word_count_in_file.py : word count of a specific file. 
```
