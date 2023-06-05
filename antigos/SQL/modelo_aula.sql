USE aula_univesp;
CREATE TABLE funcionario(
	ident INT NOT NULL AUTO_INCREMENT,
    nome varchar(30) NOT NULL,
    sobrenome varchar(50) NOT NULL,
    endereco varchar(150) NOT NULL,
    data_nasc DATE NOT NULL,
    sexo char(1) not null,
    supident int,/*chave estrangeira */
    dnumero int,/*chave estrangeira dar alter table para torna-la not null */
    primary	key(ident)
);

create table dependente(
	func_ident INT not null,/*CHAVE ESTRANGEIRA*/
	nome_completo varchar(60) not null,
	dt_nasc date not null,
	sexo char(1) not null,
	relacionamento varchar(30) not null,
    foreign key (func_ident) references funcionario(ident)
    on delete cascade
    on update cascade,
    primary key(func_ident,nome_completo)
);

create table departamento(
	numero int not null auto_increment,
    nome varchar(50) not null,
    gerente_id int not null,
    data_inicio date not null,
    primary key (numero),
    foreign key (gerente_id) references funcionario(ident)
    on update cascade
    on delete cascade
);

create table LOCALIZACOES(
	dnumero int not null, 
	localizacao varchar(200) not null,
    foreign key (dnumero) references departamento(numero)
    on delete cascade
    on update cascade,
    primary key(dnumero,localizacao)
    );
create table PROJETO(
	numero int not null auto_increment,
	nome varchar(50),
    
    dnumero int,
	localizacao varchar(200), 
	
    primary key(numero),
    foreign key (dnumero,localizacao) references localizacoes(dnumero,localizacao)
);

create table TRABALHA_EM (
	pnumero int , 
    fident int , 
    horas time not null,
    foreign key (pnumero) references PROJETO(numero),
    foreign key (fident) references funcionario(ident)
    );