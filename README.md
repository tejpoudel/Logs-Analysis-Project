# LOGS ANALYSIS 
# Author: Tej P Poudel
# Date: August 11, 2017

# Description
This project is part of Full Stack Nanodegree

# Aim
Aim of this project is to print report based on data in database by using python(2.7.10) and postgresql

#Installation
1. Install Vagrant and VirtualBox
2. Download or clone from github fullstack-nandegree-vm repository
3. Now we got newsdata.sql in our vagrant directory and lets start.

#How to run
- change directory to vagrant directory
- vagrant up command to run the vagrant on vm
- vagrant ssh to login into vm
- change directory to /vagrant/logs_analysis_project
- use command psql -d news -f newsdata.sql or psql -d news to connect to the database
- Create two database views for the reporting tool to work properly:
	CREATE view creator as
	  SELECT date_trunc('day', time) "day", count(status) as totals
	  FROM log
	  WHERE status = '404 NOT FOUND'
	  GROUP by day;

	CREATE view request_totals as
	  SELECT date_trunc('day', time) "day", count(status) as totals
	  FROM log
	  GROUP by day;

- use command python Query.py to run the programm

#File Description:
- `Query.py`: this is the main entrypoint for the application
- `Database.py`: this encapsulates the database connection logic
- 'README.md': It is the current read me file. 
- 'newsdata.sql': It is the main database table for the query. 

## Output

