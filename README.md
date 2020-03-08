### Server-bottleneck  
Script for formatting data from iostat command output to csv format.  
May be useful with linux-based performance analysis.  

Author: Aleksei Kazancev  
email: aleksei.kazancev@mail.ru     

### How to use  
Firstly you should get raw data from server via cmd: iostat -x 1 > raw_data.log    
Put the raw_data.log in same folder with script  
Execute and check the result at raw_data_formatted.csv  
Open raw_data_formatted.csv in Excel or Google Tab, build diagrams and analysis its.

### More about iostat
[iostat](http://sebastien.godard.pagesperso-orange.fr/man_iostat.html) is part of [sysstat package](https://github.com/sysstat/sysstat)  
It is intended for collecting reports CPU statistics and input/output statistics for block devices and partitions.
