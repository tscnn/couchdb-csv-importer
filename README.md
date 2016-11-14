# couch-csv-import.py
A simple Python script for importing CSV data into a CouchDB database. It
supports Unix pipelining and can be used to import records from relational
databases. __The first line of the CSV data must correspond to the key
names of the CouchDB documents to be created.__

## Requirements
In addition to Python, the following Python packages are required for the
script to run. Install it with your preferred python package manager.
* csv
* couchdb
* argparse

## Usage
```
$ python couch-csv-import.py --help

usage: couch-csv-import.py [-h] [-d DELIMITER] [-q QUOTECHAR]
                           SERVER DBNAME INPUTFILE

positional arguments:
  SERVER                The URL for the CouchDB server.
  DBNAME                The name of the target database.
  INPUTFILE             The CSV file to import. (use - for pipelining)

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        The CSV delimiter char. Default=';' (use '\t' for
                        tabs)
  -q QUOTECHAR, --quotechar QUOTECHAR
                        The CSV quotechar char. Default='"'
```

## Examples
Import CSV data stored in the ``contacs.csv`` file to the database ``contacts``
on the server ``127.0.0.1:5984``.
```
$ python couch-csv-import.py http://127.0.0.1:5984/ contacts contacts.csv
```

The CSV stream now comes from the Unix pipe.
```
$ cat contacts.csv | python couch-csv-import.py http://127.0.0.1:5984/ contacts -
```

Import MySQL tables into CouchDB.
```
$ echo "SELECT * FROM contacts" | mysql -uuser -ppass db | python couch-csv-import.py -d "\t" http://127.0.0.1:5984 contacts -
```
