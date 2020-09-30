--- datos del esferodromo
insert into esferodromos values ('000-1', 'Holistica LTDA', 'calle con carrera', '5555555', '81dc9bdb52d04dc20036dbd8313ed055', 1000);

--- valores iniciales x moneda
insert into valoresXmonedas (valorM1, valorM2, valorM3, valorM4, valorM5, fechaIngreso, Nit_Esferodromo) values (200, 500, 1000, 2000, 5000, DATE('now','localtime'), '000-1');

--- maquinas de los jugadores
insert into Maquinas (Ip, puerto, dinero) values ('localhost', 2671, 0);
insert into Maquinas (Ip, puerto, dinero) values ('localhost', 2672, 0);
insert into Maquinas (Ip, puerto, dinero) values ('localhost', 2673, 0);
insert into Maquinas (Ip, puerto, dinero) values ('localhost', 2674, 0);
insert into Maquinas (Ip, puerto, dinero) values ('localhost', 2675, 0);
insert into Maquinas (Ip, puerto, dinero) values ('localhost', 2676, 0);
insert into Maquinas (Ip, puerto, dinero) values ('localhost', 2677, 0);
insert into Maquinas (Ip, puerto, dinero) values ('localhost', 2678, 0);

--- opciones de apuesta
insert into opciones (desc, id_TipoOpcion) values ("blanca", 1);
insert into opciones (desc, id_TipoOpcion) values ("1", 1);
insert into opciones (desc, id_TipoOpcion) values ("2", 1);
insert into opciones (desc, id_TipoOpcion) values ("3", 1);
insert into opciones (desc, id_TipoOpcion) values ("4", 1);
insert into opciones (desc, id_TipoOpcion) values ("5", 1);
insert into opciones (desc, id_TipoOpcion) values ("6", 1);
insert into opciones (desc, id_TipoOpcion) values ("7", 1);
insert into opciones (desc, id_TipoOpcion) values ("8", 1);
insert into opciones (desc, id_TipoOpcion) values ("9", 1);
insert into opciones (desc, id_TipoOpcion) values ("10", 1);
insert into opciones (desc, id_TipoOpcion) values ("menores", 4);
insert into opciones (desc, id_TipoOpcion) values ("mayores", 4);
insert into opciones (desc, id_TipoOpcion) values ("pares", 4);
insert into opciones (desc, id_TipoOpcion) values ("impares", 4);
insert into opciones (desc, id_TipoOpcion) values ("fila 1", 4);
insert into opciones (desc, id_TipoOpcion) values ("fila 2", 4);
insert into opciones (desc, id_TipoOpcion) values ("1 y 4", 2);
insert into opciones (desc, id_TipoOpcion) values ("2 y 3", 2);
insert into opciones (desc, id_TipoOpcion) values ("4 y 5", 2);
insert into opciones (desc, id_TipoOpcion) values ("3 y 6", 2);
insert into opciones (desc, id_TipoOpcion) values ("5 y 8", 2);
insert into opciones (desc, id_TipoOpcion) values ("6 y 7", 2);
insert into opciones (desc, id_TipoOpcion) values ("8 y 9", 2);
insert into opciones (desc, id_TipoOpcion) values ("7 y 10", 2);
insert into opciones (desc, id_TipoOpcion) values ("1 y 2", 2);
insert into opciones (desc, id_TipoOpcion) values ("3 y 4", 2);
insert into opciones (desc, id_TipoOpcion) values ("5 y 6", 2);
insert into opciones (desc, id_TipoOpcion) values ("7 y 8", 2);
insert into opciones (desc, id_TipoOpcion) values ("9 y 10", 2);
insert into opciones (desc, id_TipoOpcion) values ("1, 2, 3 y 4", 3);
insert into opciones (desc, id_TipoOpcion) values ("3, 4, 5 y 6", 3);
insert into opciones (desc, id_TipoOpcion) values ("5, 6, 7 y 8", 3);
insert into opciones (desc, id_TipoOpcion) values ("7, 8, 9 y 10", 3);

--- billetes
insert into billetes (valor) values (1000);
insert into billetes (valor) values (2000);
insert into billetes (valor) values (5000);
insert into billetes (valor) values (10000);
insert into billetes (valor) values (20000);
insert into billetes (valor) values (50000);

--- tipo de opciones
insert into TipoOpciones (desc, pagaPor, min, max) values ("pleno", 9, 200, 10000);
insert into TipoOpciones (desc, pagaPor, min, max) values ("medio", 4, 200, 10000);
insert into TipoOpciones (desc, pagaPor, min, max) values ("cuadro", 1.5, 200, 10000);
insert into TipoOpciones (desc, pagaPor, min, max) values ("chanza", 1, 2000, 10000);

-- insertar pozo por defecto
insert into pozos (montoInicial, montoActual, montoReserva, montoMinimoParaConcursar, frecuenciaSorteo, factorReserva, factorIncremento, id_ultimaRondaJugada, nit_Esferodromo) values (0, 0, 0, 0, 10, 0.01, 0.03, 0, '000-1');

