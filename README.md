i would like to add feature export output to a excel file


below command converts output tweets into excel



snscrape --max-results 100 twitter-hashtag SBIN >a.json
python3 json2excel.py
ls
you can observe output.csv  file which our required file
