create database bd_estoque;

use bd_estoque;

create table mercadorias(id_mercadoria integer primary key auto_increment not null, 
	nome_produto varchar(60) not null, 
	valor_produto varchar(60) not null, 
	quantidade_produto int, 
	unidade_medida varchar(45), 
	data_entrada date);

create table login_usuario(id_usuario integer primary key auto_increment not null, 
							nome varchar(45) not null, senha varchar(45))


select * from login_usuario;
select * from mercadorias;


alter table mercadorias modify quantidade_produto integer not null;

alter table mercadorias modify data_entrada datetime;

delete from mercadorias where id_mercadoria = 6;
delete from login_usuario where id_usuario = 1;

SET SQL_SAFE_UPDATES=0;
update mercadorias set quantidade_produto = '5' where nome_produto = 'Banana Prata';



select quantidade_produto from mercadorias where nome_produto like 'leite';


create table relatorio (idRelatorio integer primary key not null auto_increment,  nome_f varchar(20), nome_prod varchar(30), qnt integer, dataRel datetime);

desc relatorio;

drop table relatorio;