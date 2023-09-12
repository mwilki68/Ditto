
ALTER SEQUENCE "liaisons_recno_seq" RESTART WITH 1;
ALTER SEQUENCE "reviews_recno_seq" RESTART WITH 1;
ALTER SEQUENCE "wl_recno_seq" RESTART WITH 1;
ALTER SEQUENCE "tasks_recno_seq" RESTART WITH 1;
ALTER SEQUENCE "epp_recno_seq" RESTART WITH 1;

delete  from liaisons
delete from reviews
delete from wl
delete from tasks
delete from epp


select count (*) from liaisons
select count (*) from reviews
select count (*) from wl
select count (*) from tasks
select count (*) from epp


select * from liaisons order by edit_timestamp desc
select * from reviews order by edit_timestamp desc
select * from wl order by edit_timestamp desc
select * from tasks order by edit_timestamp desc
select * from epp order by edit_timestamp desc