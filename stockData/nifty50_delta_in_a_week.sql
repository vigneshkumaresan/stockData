/* What are we trying to do here?
 * Trying to figure out the maximum high point and minimum low point that has occured withing a week of option trading
 * This query does not work during the year-changes
 */


select trading_date,open,high,low,close,volume,turnover,dow,option_order,yr,week_year,max_change_in_a_day,close-weekly_opening change_in_a_week
from (
		select * ,case when extract(dow from trading_date) =1 then 'monday'
			when extract(dow from trading_date) =2 then 'tuesday'
			when extract(dow from trading_date) =3 then 'wednesday'
			when extract(dow from trading_date) =4 then 'thursday'
			when extract(dow from trading_date) =5 then 'friday'
		end dow,
		case 
			when extract(dow from trading_date) =1 then 2
			when extract(dow from trading_date) =2 then 3
			when extract(dow from trading_date) =3 then 4
			when extract(dow from trading_date) =4 then 5
			when extract(dow from trading_date) =5 then 1
		end option_order,			
		to_char(trading_date,'IYYY')::integer yr, 
		case when extract(dow from trading_date) =5 then to_char(trading_date,'IW')::integer+1 
			 else to_char(trading_date,'IW')::integer
		end week_year,
		close-open max_change_in_a_day,
		lag(open,4)over(partition by to_char(trading_date,'IYYY')::integer ,
									 case when extract(dow from trading_date) =5 then to_char(trading_date,'IW')::integer+1 
										 else to_char(trading_date,'IW')::integer
									end 
						order by case 
									when extract(dow from trading_date) =1 then 2
									when extract(dow from trading_date) =2 then 3
									when extract(dow from trading_date) =3 then 4
									when extract(dow from trading_date) =4 then 5
									when extract(dow from trading_date) =5 then 1
								end
						) weekly_opening
	from nse_nifty50 nn 
	where to_char(trading_date,'IYYY')::integer>2000
	)a	
where weekly_opening is not null
order by 13 desc
limit 5;


			
select trading_date,open,high,low,close,volume,turnover,dow,option_order,yr,week_year,max_change_in_a_day,close-weekly_opening change_in_a_week
from (
		select * ,case when extract(dow from trading_date) =1 then 'monday'
		when extract(dow from trading_date) =2 then 'tuesday'
		when extract(dow from trading_date) =3 then 'wednesday'
		when extract(dow from trading_date) =4 then 'thursday'
		when extract(dow from trading_date) =5 then 'friday'
	end dow,
	case 
		when extract(dow from trading_date) =1 then 2
		when extract(dow from trading_date) =2 then 3
		when extract(dow from trading_date) =3 then 4
		when extract(dow from trading_date) =4 then 5
		when extract(dow from trading_date) =5 then 1
	end option_order,			
	to_char(trading_date,'IYYY')::integer yr, 
	case when extract(dow from trading_date) =5 then to_char(trading_date,'IW')::integer+1 
		 else to_char(trading_date,'IW')::integer
	end week_year,
	close-open max_change_in_a_day,
	lag(open,4)over(partition by to_char(trading_date,'IYYY')::integer ,
								 case when extract(dow from trading_date) =5 then to_char(trading_date,'IW')::integer+1 
									 else to_char(trading_date,'IW')::integer
								end 
					order by case 
								when extract(dow from trading_date) =1 then 2
								when extract(dow from trading_date) =2 then 3
								when extract(dow from trading_date) =3 then 4
								when extract(dow from trading_date) =4 then 5
								when extract(dow from trading_date) =5 then 1
							end
					) weekly_opening
from nse_nifty50 nn 
where to_char(trading_date,'IYYY')::integer>2000
	)a	
where weekly_opening is not null
order by 13 asc
limit 5;

				
