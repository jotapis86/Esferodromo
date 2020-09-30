create table Esferodromos
(
	Nit text primary key not null,
	Nombre text not null,
	Dir text not null,
	Tel text not null,
	claveAdmin text not null,
	montoMinimoApuestasXmaquina integer not null
);

create table ValoresXmonedas
(
	Id integer not null primary key autoincrement,
	ValorM1 integer not null,
	ValorM2 integer not null,
	ValorM3 integer not null,
	ValorM4 integer not null,
	ValorM5 integer not null,
	fechaIngreso text not null,
	Nit_Esferodromo text not null
);

create table Rondas
(
	Id integer not null primary key autoincrement,
	Fecha text not null,
	HoraInicio text not null,
	HoraCierreApuestas text,
	HoraFin text,
	ganadora text,
	nit_Esferodromo text not null,
	id_Coordinador integer not null
);

create table Apuestas
(
	Id integer not null primary key autoincrement,
	Fecha text not null,
	Hora text not null,
	Id_Ronda integer not null,
	Id_Maquina integer not null
);

create table Maquinas
(
	Id integer not null primary key autoincrement,
	Ip text not null,
	Puerto integer not null,
	Dinero integer not null,
	codMegaManager text not null default ''
);

create table Opciones 
(
	id integer not null primary key autoincrement,
	desc text not null,
	id_TipoOpcion integer not null
);

create table ApuestasXopciones
(
	id_Apuesta integer not null,
	id_Opcion integer not null,
	valorApostado integer not null,
	valorGanado integer,
	primary key (id_Apuesta, id_Opcion)
);

create table Billetes
(
	Id integer not null primary key autoincrement,
	Valor integer not null unique
);

create table BilletesXmaquinas
(
	Id integer not null primary key autoincrement,
	Fecha text not null,
	Hora text not null,
	Id_Billete integer not null,
	id_Maquina integer not null
);

create table TipoOpciones
(
	id integer not null primary key autoincrement,
	desc text not null,
	pagaPor real not null,
	min integer not null,
	max integer not null
);

create table Coordinadores
(
	id integer not null primary key autoincrement,
	nombre text not null,
	clave text not null,
	codMegaManager text not null default ''
);

create table Pagos
(
	id integer not null primary key autoincrement,
	valor integer not null,
	fecha text not null,
	hora text not null,
	id_Coordinador integer not null,
	id_Maquina integer not null,
	idCliente text not null default '',
	enviadoMegaManager text not null default 'N'
);

create table CreditosManualesXmaquinas
(
	id integer not null primary key autoincrement,
	fecha text not null,
	hora text not null,
	id_Coordinador integer not null,
	id_Maquina integer not null,
	valor integer not null,
	enviadoMegaManager text not null default 'N'
);

create table Pozos
(
	id integer not null primary key autoincrement,
	montoInicial integer not null,
	montoActual integer not null,
	montoReserva integer not null,
	montoMinimoParaConcursar integer not null,
	frecuenciaSorteo integer not null,
	factorReserva real not null,
	factorIncremento real not null,
	id_ultimaRondaJugada integer not null,
	nit_Esferodromo text not null
);

create table jugadasPozo
(
	id integer not null primary key autoincrement,
	fecha text not null,
	hora text not null,
	monto integer null,
	id_pozo integer not null,
	id_ronda integer not null,
	id_opcion integer not null
);

create table ganadoresPozo
(
	id_jugadaPozo integer not null,
	id_maquina integer not null,
	id_apuesta integer not null,
	id_opcion integer not null,
	montoGanado integer not null
);


