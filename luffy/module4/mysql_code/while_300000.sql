#while循环 
 delimiter // 
 CREATE PROCEDURE proc_while () 
 BEGIN 
   declare numa int ; 
 SET numa = 1 ; 
 WHILE numa < 3000000 do 
 insert into while_num(num) values (numa); 
 SET numa = numa + 1 ; 
 END WHILE ; 
   END // 
 delimiter ; 
