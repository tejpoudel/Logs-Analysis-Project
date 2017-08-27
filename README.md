
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
- 'README.md': It is the current read me file. 
- 'newsdata.sql': It is the main database table for the query. 

## Output

 ***** Three most popular articles of all time ***** 
 
     Candidate is jerk, alleges rival: 338647 views
     Bears love berries, alleges bear: 253801 views
     Bad things gone, say good people: 170098 views

 ***** Most popular authors of all time ***** 
 
     Ursula La Multa: 507594 views
     Rudolf von Treppenwitz: 423457 views
     Anonymous Contributor: 170098 views
     Markoff Chaney: 84557 views

 ***** More than 1% of requests lead to errors ***** 
 
     07/17/2016: 2.26%

