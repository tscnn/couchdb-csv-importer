#!/usr/bin/env python

import sys
import csv
import couchdb
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("SERVER",             help="The URL for the CouchDB server.")
parser.add_argument("DBNAME",             help="The name of the target database.")
parser.add_argument("INPUTFILE",          help="The CSV file to import. (use - for pipelining)")
parser.add_argument("-d", "--delimiter",  help="The CSV delimiter char. Default=';' (use '\\t' for tabs)", default=";")
parser.add_argument("-q", "--quotechar",  help="The CSV quotechar char. Default='\"'", default='"')
args = parser.parse_args()

# establish couchdb connection
couchServer = couchdb.Server(args.SERVER)
couchDb = couchServer[args.DBNAME]

# convert each line in csv to json and store it
with sys.stdin if args.INPUTFILE == '-' else open(args.INPUTFILE, 'rb') as csvStream:
    reader = csv.reader(csvStream, delimiter=args.delimiter.replace("\\t", "\t"), quotechar=args.quotechar)
    keys = next(reader)
    for values in reader:
        couchDb.save(dict(zip(keys, values)))
