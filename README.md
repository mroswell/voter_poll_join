voter_poll_join
=================

Join a voter with his or her precinct poll location.



1. clone this mroswell/voter_poll_join repo.
```
$ git clone git@github.com:mroswell/voter_poll_join.git
```

2. Ensure that your comma-separated voter and poll files match the format of the sample csv files (voter_file.csv and precinct_polling_list.csv) Note: any prefix before the "-" in the Precinct ID and Precinct fields could work, as long as there is a 'state' field in the voter file, and a 'State/ZIP' in the poll file. The number of digits in the zip code (in either file) does not matter.

3. Ensure that you have Python 2.7 installed.

4. Install csvkit
```
$ pip install csvkit
```
If pip is not installed already, follow the installation documentation here:
https://pip.pypa.io/en/latest/installing.html


5. python voting_polls_join VOTERFILE.csv POLLFILE.csv OUTPUTFILE.csv
example: append_poll voterfile.csv precinct_polling_list.csv

The result will be three new files, located in the same directory as your cloned repo:
 - parsed_voter_file.csv
 - parsed_precinct_polling_list.csv
 - voter_poll_joined.csv

(You may choose to remove the two parsed files, since they are joined in the final voter_poll_joined.csv file.)


Note: the voter_file.csv and precinct_polling_list.csv had line ends changed via the dos2unix utility, to facilitate placement on github.
http://sourceforge.net/projects/dos2unix/

