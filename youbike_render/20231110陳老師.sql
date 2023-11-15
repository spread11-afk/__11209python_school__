select * from 台北市youbike
order by 更新時間 desc

select * from 台北市youbike
where 更新時間 in(select max(更新時間)from 台北市youbike group by 站點名稱);


select 站點名稱,max(更新時間)from 台北市youbike group by 站點名稱

select a.* from 台北市youbike a join (select distinct 站點名稱,max(更新時間) 更新時間 from 台北市youbike group by 站點名稱) b
on  a.更新時間=b.更新時間 and a.站點名稱=b.站點名稱

select 


select 站點名稱,max(更新時間) 更新時間 from 台北市youbike group by 站點名稱
