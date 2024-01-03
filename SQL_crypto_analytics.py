select *
from raw.transactions;
/*
How many buy and sell transactions are there for Bitcoin? - your result should return
two columns :  txn_type, transaction_count
 */
Select txn_type, count(txn_type) as transaction_count
From raw.transactions
group by txn_type;

/* For each year, calculate the following buy and sell metrics for bitcoin:
- Total transaction count
- Total quantity
- Average quantity
Kindly note that you are generating a single query to calculate these metrics and
you should return exactly 5 columns - txn_year, txn_type, txn_count,
total_quantity, average_quantity
*/

Select txn_type, 
EXTRACT(YEAR FROM txn_date::date) as txn_year, 
count(txn_type) as txn_count, 
sum(quantity) as total_quantity, 
avg(quantity) as average_quantity
from raw.transactions
where txn_type in ('BUY', 'SELL') and ticker = 'BTC'
group by txn_type, txn_year
order by total_quantity desc;


/*
 What was the monthly total quantity purchased and sold for Ethereum in 2020? Your
query should return exactly three columns - calendar_month, buy_qunatity,
sell_quantity */

select EXTRACT(MONTH FROM txn_date::date) as Calender_month, 
sum(case when txn_type = 'BUY' then quantity else 0 end) as buy_quantity,
sum(case when txn_type = 'SELL' then quantity else 0 end) as sell_quantity
from raw.transactions
where EXTRACT(YEAR FROM txn_date::date) = 2020 and ticker ='ETH'
group by calender_month;

/*
Who are the top 3 members with the most bitcoin quantity? Your result should return
exactly two columns - first_name, total_quantity
 */

select first_name, sum(quantity) as total_quantity
from members as m
join transactions as t
on m.member_id = t.member_id
where ticker = 'BTC'
group by first_name
order by total_quantity desc 
limit 3;