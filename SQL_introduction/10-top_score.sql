-- list by best score
-- Execute: cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name FROM first_table ORDER BY score DESC;
