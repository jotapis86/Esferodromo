-- contiene solo los cambios necesarios que se deben aplicar para pasar de la version del Esferodromo 1.0 a la 2.0
-- Script de tablas e inserciones basicas tambien contienen estos cambios si la instalacion es desde cero.

-- 1. crear tabla para ingreso de creditos manuales "CreditosManualesXmaquinas"
create table CreditosManualesXmaquinas
(
	id integer not null primary key autoincrement,
	fecha text not null,
	hora text not null,
	id_Coordinador integer not null,
	id_Maquina integer not null,
	valor integer not null
);

-- 2. agregar columna "montoMinimoApuestasXmaquina integer not null" a tabla "Esferodromos"
alter table esferodromos add column montoMinimoApuestasXmaquina integer not null default 0;

-- 3. actualizar monto por defecto a campo "montoMinimoApuestasXmaquina integer not null" en tabla "Esferodromos"
update esferodromos set montoMinimoApuestasXmaquina = 1000;

-- 4. crear tabla de pozos
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

-- 4.1. insertar pozo por defecto
insert into pozos (montoInicial, montoActual, montoReserva, montoMinimoParaConcursar, frecuenciaSorteo, factorReserva, factorIncremento, id_ultimaRondaJugada, nit_Esferodromo) values (0, 0, 0, 0, 10, 0.01, 0.03, 0, '000-1');

-- 5. crear tabla de jugadas del pozo
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

-- 6. crear tabla de ganadores del pozo
create table ganadoresPozo
(
	id_jugadaPozo integer not null,
	id_maquina integer not null,
	id_apuesta integer not null,
	id_opcion integer not null,
	montoGanado integer not null
);

