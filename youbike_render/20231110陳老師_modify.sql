select * from 台北市youbike
order by 更新時間 desc

select * from 台北市youbike
where '2023-11-15 11:14:14' in(select max(更新時間)from 台北市youbike group by 站點名稱);

select * from 台北市youbike
where 更新時間 in(select max(更新時間)from 台北市youbike group by 站點名稱);

select 站點名稱,max(更新時間)from 台北市youbike group by 站點名稱

select a.* from 台北市youbike a join (select 站點名稱,max(更新時間) 更新時間 from 台北市youbike group by 站點名稱) b
on  a.更新時間=b.更新時間 and a.站點名稱=b.站點名稱

SELECT *FROM 台北市youbike WHERE (更新時間,站點名稱) IN (
	SELECT MAX(更新時間),站點名稱
	FROM 台北市youbike
	GROUP BY 站點名稱
) 

select * from 台北市youbike where 站點名稱='YouBike2.0_捷運臺電大樓站(5號出口)'
select 站點名稱,max(更新時間),count(*) 更新時間 from 台北市youbike group by 站點名稱