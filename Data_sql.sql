-- under the Mysql , creating a table named Tphil under the Phil DB
use Phil
CREATE TABLE Tphil ( Product VARCHAR(30) NOT NULL, Period TIMESTAMP, Actual INT , Target INT);

-- to fill up the Table Tphill without header
-- $ mysql -u root -p --local-infile Phil -e "LOAD DATA LOCAL INFILE 'Data.csv'  INTO TABLE Tphil  FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES"

-- sum of actuals
select * from Tphil;
select SUM(Actual) from Tphil ; 

--  the previous month vs current month difference of actuals.
select t1.* , abs(t2.Actual - ifnull(t1.Actual,0)) as diff_ac from tmp1 t1 LEFT OUTER JOIN tmp1 t2 ON(t1.row_number = t2.row_number + 1) order by t1.row_number;

--  each row and the total sum of actuals in each row
set @csum := 0; select Product, Period, Actual,Target, (@csum := @csum + Actual) as cumulative_sum_ac from tmp1 order by row_number;

