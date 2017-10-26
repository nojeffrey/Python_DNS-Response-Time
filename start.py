#!/usr/bin/env python

import pandas, subprocess, time, re, pprint

#Get top 50 domains:
print('-----Getting top 50 domains------')
domains_dataframe = pandas.read_html('https://en.wikipedia.org/wiki/List_of_most_popular_websites')[1][1].tolist()[:51]
domains_dataframe.remove('Domain')


#Iterate through domains, test response time.
def test_resp_time(domain_list):
    totaltime = 0
    for i in domain_list:
        x = subprocess.getoutput('dig ' + i)
        resp_time = re.search("Query time: ([0-9]*)", x).group(1)

        #pad short/long domain names for formatting
        if len(i) < 7:
            i = i + '   '
        elif len(i) > 15:
            i = i[:14]
        
        print(i.strip('\n'), '\t\t', resp_time)
        totaltime += int(resp_time)
        time.sleep(.5)
    print('\nAvg resp time: {0} msec'.format(totaltime/50))

    
test_resp_time(domains_dataframe)
