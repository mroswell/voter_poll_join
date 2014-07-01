
windows_users.md
----------------

### Introduction

Installing csvkit is a challenge on Windows, probably not worth the trouble. We're using it (in Linux or OS X) only to join _parsed_voter_file.csv_ with _parsed_precinct_polling_list.csv_ on the _poll_precinct_id_ field. Windows users can achieve the same goals using other means, including Excel.

### Detailed Steps
 1. Skip Step 4, but complete Step 5. This will create the two necessary parsed voter and poll location files.
 2. Open Excel
 3. Rename the left-most worksheet (Sheet1) to "voterfile"
  4. Place your cursor in cell A:1
  5. Select the Data > From Text
  6. Navigate to the voter_poll_join repo
  7. Select _parsed_voter_file.csv_. This will fill columns A through H.
 8. Select Sheet2, and rename it "polls"
  9. Place your cursor in cell A:1 of the polls worksheet
  10. Select Data > From Text.
  11. Navigate to the voter_poll_join repo
  12. select _parsed_precinct_polling_list.csv_. This will fill columns A through H.
  13. copy the first row (the headers, not including the last field)

Now comes the fun!

 12. Go back to the voterfile worksheet. Place your cursor in cell I:1 and paste the column headers.
13.
