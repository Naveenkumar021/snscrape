import pandas as pd
import json 
import csv
# Opening JSON file
with open('tweets.json') as json_file:
    data = json.load(json_file)
#rem=['url','content','date','renderedContent','media','hashtags']
res={key:data[key]for key in data.keys()&{'url','content','date','renderedContent','media','hashtags'}}
#res=dict([(key,val)for key,value in data.items() if key in rem()])

with open('output.csv','w+')as output:
    writer=csv.writer(output)
    for key,value in res.items():
        writer.writerow([key,value])
