Instructions for Windows Users
----------------

### Introduction

Installing csvkit is a challenge on Windows, probably not worth the trouble. We're using it (on Linux or OS X) only to join _parsed_voter_file.csv_ with _parsed_precinct_polling_list.csv_ on the precinct_id and _poll_precinct_id_ fields. Windows users can achieve the same goals using other means, including Excel.

### Summary
1. Follow the [documentation](https://github.com/mroswell/voter_poll_join/blob/master/README.md) instructions, excluding step 4.
3. Join _parsed_voter_file.csv_ with _parsed_precinct_polling_list.csv_ on the precinct ID

### Detailed steps to join the two parsed files in Excel
_These instructions were tested on MS Excel from Microsoft Office 2010 (Excel 14.0.7116.5000 (32-bit))_

1. Review the voter_poll_join  [documentation](https://github.com/mroswell/voter_poll_join/blob/master/README.md). Skip step 4 (installing csvkit), but complete step 5 (running the voter_poll_join.py program). This will create the two parsed voter and poll files that you will join in Excel.
2. Open Excel
3. Rename the left-most worksheet (Sheet1) to __voterfile__
4. Place your cursor in cell A:1
  5. On the Data tab, in the Get External Data group, click From Text.
  6. Navigate to the voter_poll_join repo
  7. Select _parsed_voter_file.csv_. Complete the wizard by selecting Delimiter. Next. Deselect tab, select Comma. Next. General.Finish. Existing Worksheet. Okay. This will fill columns A through H.
8. Select Sheet2, and rename it __polls__
  9. Place your cursor in cell A:1 of the polls worksheet
  10. On the Data tab, in the Get External Data group, click From Text.
  11. Navigate to the voter_poll_join repo, if you're not already there.
  12. Select _parsed_precinct_polling_list.csv_. Complete the wizard by selecting Delimiter. Next. Deselect tab, select Comma. Next. General. Finish. Existing Worksheet. Okay. This will fill columns A through H.
  13. Press Control-End to get to the bottom-right cell in the spreadsheet. Remember that row number.
  14. Press Control-Home to get back to the top-left cell
  15. Copy the first row (the headers)
16. Click on to the __voterfile__ worksheet.
  17. Place your cursor in cell I:1 and paste in the poll column headers.
  18. Place your cursor in cell I:2, and paste in the following.
      ```
      =INDEX(polls!A$1:A$34,MATCH($H2,polls!$H$1:$H$34,0))
      ```
  19. Replace the 34 (in both formula places) with the last row number that you memorized above. Press enter
  20. Click back on Cell I:2. Drag the formula dot to the right-most poll column. This should fill in the first row with the polling location of the first voter.
  21. Double-click on the formula dot to extend the formula to all of the voters. (If this doesn't work, make sure you don't have  any blank columns between the voters and the formulas.)
22. Spot check that your results seem in good order.
  23. Visually inspect the right-hand precinct_poll_id to ensure that it matches the one in the original file. If it does, feel free to delete the two duplicate columns (poll_precinct_num and poll_precinct_id).
  24. Format the zip code columns as zip codes. (Select the 'poll_zip' column. Right click. Choose Format Cells > Special > Zip Code. Click 'Okay')
  25. Format the state_fips and precinct_num with leading zeroes. (Select the two columns. Right-click. Choose Format Cells > Custom. Enter: 000. Click "Okay")
  25. Decide if you actually want to keep the other precinct_num, and the country. Delete if unnecessary.
  26. Select the new poll columns using the header.  Right click. Select Copy, then Paste Values (click the icon with the 123 symbol), to replace the formulas with values.
  27. To clear out the #N/A cells (these represent the voters with no corresponding precinct information): Press Ctrl-H. Find what: #N/A    Replace with: (leave this blank). Click Replace All.

28. Save the Excel file and/or Save As a CSV file.

Congratulations!

If you prefer to use a tool other than Excel to join the two parsed files, feel free. Options include Access, MySQL, Postgres, SQLite. If you prefer VLOOKUP to INDEX/MATCH in Excel, feel free to implement that (INDEX/MATCH is generally faster). In essence, the Python script creates parsed files that share a common precinct ID, enabling a straightforward join.
