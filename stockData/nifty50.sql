drop table if exists nifty50_analysis;

create table nifty50_analysis as 
select trading_date, open_price,high_price,low_price,close_price,adj_close,volume,dividends,
round(((close_price/previous_close)-1)*100::numeric,2) daily_volatility_percentage
from (
select date(trading_date) trading_date ,
	   round(open::numeric,2) open_price,
	   round(high::numeric,2) high_price,
	   round(low::numeric,2) low_price,
	   round(close::numeric,2) close_price,
	   round(adj_close::numeric,2) adj_close,
	   volume,dividends,
	   stock_splits,
	   round(lead(close,1) over(order by trading_date asc)::numeric,2) previous_close
	   from nifty50 a
	  ) x; 



--Calculating Daily Volatility for 5 days, 10 days, 30 days, 90 days, 180 days, 365 days for Nifty 50
with cte as(
				select max(trading_date)-5 trading_date5, 
				max(trading_date)-10 trading_date10, 
				max(trading_date)-30 trading_date30,
				max(trading_date)-90 trading_date90,
				max(trading_date)-180 trading_date180,
				max(trading_date)-365 trading_date365
				from nifty50_analysis
			 )
select 5 std_duration_in_days,stddev_samp(daily_volatility_percentage) 
from nifty50_analysis v,cte
where v.trading_date>cte.trading_date5
union
select 10 std_duration_in_days,stddev_samp(daily_volatility_percentage) 
from nifty50_analysis v,cte
where v.trading_date>cte.trading_date10
union
select 30 std_duration_in_days,stddev_samp(daily_volatility_percentage) 
from nifty50_analysis v,cte
where v.trading_date>cte.trading_date30
union
select 90 std_duration_in_days,stddev_samp(daily_volatility_percentage) 
from nifty50_analysis v,cte
where v.trading_date>cte.trading_date90
union
select 180 std_duration_in_days,stddev_samp(daily_volatility_percentage) 
from nifty50_analysis v,cte
where v.trading_date>cte.trading_date180
union
select 365 std_duration_in_days,stddev_samp(daily_volatility_percentage) 
from nifty50_analysis v,cte
where v.trading_date>cte.trading_date365
order by std_duration_in_days;

