#创建触发器
delimiter //
CREATE TRIGGER tri_after_insert_cmd AFTER INSERT ON cmd FOR EACH ROW
BEGIN
    IF NEW.success = 'no' THEN #等值判断只有一个等号
            INSERT INTO errlog(err_cmd, err_time) VALUES(NEW.cmd, NEW.sub_time) ; #必须加分号
      END IF ; #必须加分号
END//
delimiter ;


create table while_num(
    id int not null auto_increment,
    num int not null,
    primary key(id)
);

#while循环
delimiter //
CREATE PROCEDURE proc_while ()
BEGIN

    declare numa int ;
    SET numa = 1 ;
    WHILE numa < 1000000000 do
        insert into while_num(num) values (numa);
        SET numa = numa + 1 ;
    END WHILE ;

END //
delimiter ;

