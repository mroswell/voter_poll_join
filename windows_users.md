Instructions for Windows Users
----------------

### Introduction

Installing csvkit is a challenge on Windows, probably not worth the trouble. We're using it (on Linux or OS X) only to join _parsed_voter_file.csv_ with _parsed_precinct_polling_list.csv_ on the precinct_id / _poll_precinct_id_ fields. Windows users can achieve the same goals using other means, including Excel.

### Detailed steps to join the two parsed files in Excel
_These instructions were tested on MS Excel from Microsoft Office 2010 (Excel 14.0.7116.5000 (32-bit))_
 1. Review the voter_poll_join  [documentation](https://github.com/mroswell/voter_poll_join/blob/master/README.md). Skip step 4 (installing csvkit), but complete step 5 (running the voter_poll_join.py program). This will create the two parsed voter and poll files that you will join in Excel.
 2. Open Excel
 3. Rename the left-most worksheet (Sheet1) to _voterfile_
  4. Place your cursor in cell A:1
  5. Select the Data > From Text
  6. Navigate to the voter_poll_join repo
  7. Select _parsed_voter_file.csv_. Complete the wizard by selecting Delimiter. Next. Deselect tab, select Comma. Next. General. Finish. Existing Worksheet. Okay. This will fill columns A through H.
 8. Select Sheet2, and rename it _polls_
  9. Place your cursor in cell A:1 of the polls worksheet
  10. Select Data > From Text.
  11. Navigate to the voter_poll_join repo, if you're not already there.
  12. Select _parsed_precinct_polling_list.csv_. Complete the wizard by selecting Delimiter. Next. Deselect tab, select Comma. Next. General. Finish. Existing Worksheet. Okay. This will fill columns A through H.
  13. Press Control-End to get to the bottom-right cell in the spreadsheet. Remember that row number.
  14. Press Control-Home to get back to the top-left cell
  15. Copy the first row (the headers)

 16. Go back to the __voterfile__ worksheet. Place your cursor in cell I:1 and paste in the poll column headers.
   17. Place your cursor in cell I:2, and paste in the following.
```
=INDEX(polls!A$1:A$34,MATCH($H2,polls!$H$1:$H$34,0))
```
   18. Replace the 34 (in both places) with the last row number that you memorized above.
   19. Drag the formula dot to the right-most column. This should fill in the first row with the polling location of the first voter.
   20. Double click on the formula dot to extend the formula to all of the voters. (If this doesn't work, make sure you don't have  any blank columns between the voters and the formulas.)
   21. Visually inspect the right-hand precinct_poll_id to ensure that it matches the one in the original file. If it does, feel free to delete the two duplicate columns (precinct_poll_num and precinct_poll_id).
   22. Format the zip code columns as zip codes. (Select the column, Right click. Choose Format Cells > Special > Zip Code. Click 'Okay')
   23. Format the state_fips and precinct_num with leading zeroes. (Select the two columns. Right-click. Choose Format Cells > Custom. Enter: 000. Click "Okay")
   24. Decide if you actually want to keep the other precinct_number, and the country. Delete if unnecessary.
   25. Spot check that your results seem in good order.
   26. Select the new poll columns. Copy, and paste values, to replace the formulas with values.
   27. If the #N/A cells bother you (the voters with no corresponding precinct) you may do a search and replace. Press Ctrl-H. Find What: #N/A    Replace with: (leave this blank). Click Replace All.
28. Save the Excel file and/or Save As a CSV.

Congratulations!

If you prefer to use a different tool than Excel to join the two parsed files, feel free. Options include Access, MySQL, Postgres, SQLite. If you prefer VLOOKUP to INDEX/MATCH in Excel, feel free to implement that. In essence, the python script creates parsed files that share a common precinct number, making it a straightforward join.
