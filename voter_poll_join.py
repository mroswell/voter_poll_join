#!/usr/bin/env python
from csv import DictReader, DictWriter
import sys
import os


def process_precincts(input_poll_file):
    polls = {}
    pollreader = DictReader(open(input_poll_file, 'rb'))
    pollwriter = DictWriter(open('parsed_precinct_polling_list.csv','wt'), ['poll_street', 'poll_city', 'poll_state', 'poll_zip', 'poll_precinct_state', 'poll_precinct_num', 'poll_precinct_id'])

    pollwriter.writeheader()

    for row in pollreader:
        polls['poll_street'] = row['Street']
        polls['poll_city'] = row['City']
        polls['poll_state'] = row['State/ZIP'][0:2]
        polls['poll_zip'] = row['State/ZIP'][row['State/ZIP'].index(' ')+1:]
        polls['poll_precinct_state'] = row['Precinct'][:row['Precinct'].index('-')]
        polls['poll_precinct_num'] = row['Precinct'][row['Precinct'].index('-')+1:]
        polls['poll_precinct_id'] = polls['poll_state'] +"-" + polls['poll_precinct_num']
        pollwriter.writerow(polls)

def process_voterfile(input_voter_file):
    voterfile = {}
    voterreader = DictReader(open(input_voter_file, 'rb'))
    voterwriter = DictWriter(open('parsed_voter_file.csv','wt'), ['street', 'apt', 'city', 'state', 'zip', 'state_fips', 'precinct_num', 'precinct_id'])

    voterwriter.writeheader()

    for row in voterreader:
        voterfile['street'] = row['Street']
        voterfile['apt'] = row['Apt']
        voterfile['city'] = row['City']
        voterfile['state'] = row['State']
        voterfile['zip'] = row['Zip']
        voterfile['state_fips'] = row['Precinct ID'][:row['Precinct ID'].index('-')]
        voterfile['precinct_num'] = row['Precinct ID'][row['Precinct ID'].index('-')+1:]
        voterfile['precinct_id'] = voterfile['state'] +"-" + voterfile['precinct_num']
        voterwriter.writerow(voterfile)


def main():
    if len(sys.argv) > 1:
        input_voter_file = sys.argv[1]
        input_poll_file = sys.argv[2]
        outputfile = sys.argv[3]
    else: # default to sample input files
        input_voter_file = 'voter_file.csv'
        input_poll_file = 'precinct_polling_list.csv'
        outputfile = 'voter_poll_joined.csv'

    process_precincts(input_poll_file)
    process_voterfile(input_voter_file)

    os.system("csvjoin -c 8,7 --left parsed_voter_file.csv parsed_precinct_polling_list.csv > "+ outputfile)

if __name__ == "__main__":
  main()
