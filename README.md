# site_served_union

Issue: Agencies have many vendors they work with, and will somes need to Excel flat files (site served data) to be added into our database. However there are many and they are hard to QA and cumbersome to upload.
Fix: Python script takes all the site served files in a folder, unions them and provides a quick QA on them. 

How it works: 

1. "Input" file is where all of the site served data will be stored. There is currently dummy data housed within.
2. Run the "Union & Save.py" script. The script will call upon 2 modules created in "QA_Script.py" and will start QAing the files in "Input".
3. The "Union & Save.py" script will export a unioned file into "Output/Export Ad Server File" and create a timestamped documention of the errors in "Output/QA Documentation"
4. The folder "Output/Archive/Ad Server Override Base File" is the empty file to set the standard for the format


WIP: 
1. Need to update some of the "QA_Script.py" outputs to feed into the .txt documentation function. Some of it is just printed in the python IDE.
2. Need to create and finalize an Excel document to send to the teams. As it stands now the teams are using mismatched Excel templates. This needs (1) standardization in the headers and (2) data validation to make sure certain values are not allowed within certain rows. Example: some vendors will fill in "-" for blank dates. I also suggest putting in a locked row under the column headers that serves as an example. 
