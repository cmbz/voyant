# Given a CSV file, convert it into a number of text documents suitable for use with Voyant Tools

# Column headings

# Dictionary of column headings for the libanswers file (includes column for tags)
headers = {'IID':0,
           'QID':1,
           'Timestamp':2,
           'Query':3
            }

# Convert timestamp to a YYYY-MM-DD date for file naming purposes
def timestamp2date(timestamp):
    components = timestamp.split(' ')
    date = components[0].split('/')
    day = int(date[0])
    month = int(date[1])
    year = int(date[2]) + 2000
    date_string = str(year) + '-' + str(month) + '-' + str(day)
    return date_string

# Given the CSV file containing all Lib Answers, create a document for each row of data
def create_corpus(headers, csv_filename, docs_directory):
    iid_index = headers['IID']
    qid_index = headers['QID']
    timestamp_index = headers['Timestamp']
    query_index = headers['Query']
    # import the csv module
    import csv
    # open the csv file for reading (make sure it's utf-8, otherwise, csv parsing fails)
    fh = open(csv_filename, 'r', encoding='utf-8')
    # create a csv reader
    reader = csv.reader(fh)
    # skip the header row from the file
    next(reader)
    # dictionary of tags
    tags = {}
    # import datetime
    import datetime
    # loop through file, extract information, create document file for corpus
    for row in reader:
        if len(row) > 0:
            # get data
            iid = row[iid_index]
            qid = row[qid_index]
            timestamp = row[timestamp_index]
            query = row[query_index]
            date = timestamp2date(timestamp)
            document_name = docs_directory + '/' + date + '_' + qid + '_' + iid + '.txt'
            document = open(document_name, 'w+')
            document.write(query)
            document.close()
    fh.close()
    
# Import argparse
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument('csv', help='Unix path to CSV input file')
parser.add_argument('docs', help='Unix path to directory to save text documents')

args = parser.parse_args()

# Get filename from command line
csv = args.csv.split('=')[1]

# Get data directory from command line
docs = args.docs.split('=')[1]

# Read CSV file and write text files
create_corpus(headers, csv, docs)



