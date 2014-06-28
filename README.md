voter_poll_join
=================

Join a voter record with the appropriate precinct poll location.


### Documentation

1. Clone this voter_poll_join repo.
   ```
   $ git clone git@github.com:mroswell/voter_poll_join.git
   ```

2. Ensure that your comma-separated voter and poll files match the format of the sample CSV files ([voter_file.csv](https://raw.githubusercontent.com/mroswell/voter_poll_join/master/voter_file.csv "voter_file.csv")  and [precinct_polling_list.csv](https://raw.githubusercontent.com/mroswell/voter_poll_join/master/precinct_polling_list.csv "precinct_polling_list.csv")). Note: nearly any prefix before the "-" in the 'Precinct ID' and 'Precinct' fields could work, as long as there is a 'state' field in the voter file, and a 'State/ZIP' field in the poll file. The number of digits in the zip code (in either file) does not matter.

3. Ensure that you have Python 2.7.x installed.
    ```
    $ python --version
    ```
    If it is not already installed, find the download here:
    https://www.python.org/download/

4. Install csvkit
    ```
    $ pip install csvkit
    ```
If pip is not already installed, follow the installation documentation here:
https://pip.pypa.io/en/latest/installing.html



5. Run the voter_poll_join.py program with three filename arguments, as follows:

    ```
    $ python voter_poll_join.py INPUT_VOTERFILE.csv INPUT_POLLFILE.csv OUTPUT_FILE.csv
    ```
    Note that the two INPUT CSV files must already exist (per step 2 above). If you run:

    ```
    $ python voter_poll_join.py
    ```
    without any arguments, it will join the sample files. This is equivalent to the following:
    ```
   $ python voter_poll_join.py voter_file.csv precinct_polling_list.csv voter_poll_joined.csv
    ```

The result will be three new files, located in the same directory as your cloned repo:
 - parsed_voter_file.csv
 - parsed_precinct_polling_list.csv
 - __voter_poll_joined.csv__ (or the name you specified as your OUTPUT_FILE.csv); This file is your final result.

(You may choose to rename the two parsed files, or remove them, since they are joined in the final result file.)


### Note
To facilitate placement on GitHub, the [voter_file.csv](https://raw.githubusercontent.com/mroswell/voter_poll_join/master/voter_file.csv "voter_file.csv")  and [precinct_polling_list.csv](https://raw.githubusercontent.com/mroswell/voter_poll_join/master/precinct_polling_list.csv "precinct_polling_list.csv") line ends were changed to unix style via the dos2unix utility.
http://sourceforge.net/projects/dos2unix/

