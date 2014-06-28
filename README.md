voter_poll_join
=================

Join a voter record with the appropriate precinct poll location.


### Documentation

1. Clone this voter_poll_join repo.
   ```
   $ git clone git@github.com:mroswell/voter_poll_join.git
   ```

2. Ensure that your comma-separated voter and poll files match the format of the sample csv files ([_voter_file.csv_](https://raw.githubusercontent.com/mroswell/voter_poll_join/master/voter_file.csv "voter_file.csv")  and [_precinct_polling_list.csv_](https://raw.githubusercontent.com/mroswell/voter_poll_join/master/precinct_polling_list.csv "precinct_polling_list.csv"). Note: nearly any prefix before the "-" in the 'Precinct ID' and 'Precinct' fields could work, as long as there is a 'state' field in the voter file, and a 'State/ZIP' field in the poll file. The number of digits in the zip code (in either file) does not matter.

3. Ensure that you have Python 2.7 installed.

4. Install csvkit
   ```
   $ pip install csvkit
   ```
If pip is not already installed, follow the installation documentation here:
https://pip.pypa.io/en/latest/installing.html



5. Run the voter_poll_join.py program with three arguments, as follows:

   ```
   $ python voter_poll_join.py VOTERFILE.csv POLLFILE.csv OUTPUTFILE.csv
   ```
   if you run:

   ```
   $ python voter_poll_join.py
   ```
   without any arguments, it will join the sample files. This is the equivalent to the following:
   ```
   $ python voter_poll_join.py voterfile.csv precinct_polling_list.csv voter_poll_joined.csv
   ```

The result will be three new files, located in the same directory as your cloned repo:
 - parsed_voter_file.csv
 - parsed_precinct_polling_list.csv
 - __voter_poll_joined.csv__ (or whatever you specified as your OUTPUTFILE.csv name) This is your final result.

(You may choose to remove the two parsed files, since they are joined in the final result file.)


### Note
To facilitate placement on GitHub, the voter_file.csv and precinct_polling_list.csv had line ends changed to unix style via the dos2unix utility.
http://sourceforge.net/projects/dos2unix/

