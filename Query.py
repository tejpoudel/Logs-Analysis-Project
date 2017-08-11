#! /usr/bin/env python

from contextlib import contextmanager
import psycopg2

@contextmanager
def db_session_context(db_name):
    try:
        db = psycopg2.connect(database=db_name)
        yield db
    finally:
        db.close()

DB_NAME = 'news'


def find_popular_articles():
    """What are the most popular three articles of all time?"""

    print "\n\n ***** Three most popular articles of all time ***** "

    with db_session_context(DB_NAME) as db:
        cursor = db.cursor()
        cursor.execute("""
            SELECT articles.title, count(log.status) as count
            FROM articles, log
            WHERE log.status = '200 OK'
              and log.path like '%' || articles.slug || '%'
            GROUP BY articles.title
            ORDER BY count desc
            LIMIT 3;
        """)
        results = cursor.fetchall()

    # for each article/view count tuple, print article -- view count
    for article in results:
        print "     %s: %s views" % (article[0], article[1])


def find_popular_authors():
    """Who are the most popular article authors of all time?"""

    print "\n\n ***** Most popular authors of all time ***** "

    with db_session_context(DB_NAME) as db:
        cursor = db.cursor()
        cursor.execute("""
            SELECT authors.name, count(log.status) as count
            FROM authors, articles, log
            WHERE articles.author = authors.id
              and log.status = '200 OK'
              and log.path like '%' || articles.slug || '%'
            GROUP BY authors.name
            ORDER BY count desc;
        """)
        results = cursor.fetchall()

    # For each author/view count tuple, print author -- view count
    for author in results:
        print "     %s: %s views" % (author[0], author[1])


def find_most_errors():
    """On which days did more than 1% of requests lead to errors?"""

    print "\n\n ***** More than 1% of requests lead to errors ***** "

    with db_session_context(DB_NAME) as db:
        cursor = db.cursor()
        cursor.execute("""
            SELECT to_char(creator.day, 'MM/DD/YYYY'),
              round(
                (creator.totals*1.0 / request_totals.totals*1.0)*100, 2)
              as percentage
            FROM creator, request_totals
            WHERE creator.day = request_totals.day
              and (creator.totals*1.0 / request_totals.totals*1.0)*100 > 1
            ORDER BY percentage desc;
        """)
        result = cursor.fetchone()

    print "     %s: %s%%" % (result[0], result[1])

# Call all the functions if file is executed with the interpreter
if __name__ == "__main__":
    find_popular_articles()
    find_popular_authors()
    find_most_errors()
