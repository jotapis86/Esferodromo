-- contiene solo los cambios necesarios que se deben aplicar para pasar de la version del Esferodromo 2.0 a la 2.1
-- Script de tablas e inserciones basicas tambien contienen estos cambios si la instalacion es desde cero.

-- 1. Agregar columna en tabla de coordinadores con codigo que tienen en MegaManager
alter table coordinadores add column codMegaManager text not null default '';

-- 2. Agregar columna en tabla de maquinas con codigo que tienen en MegaManager
alter table maquinas add column codMegaManager text not null default '';

-- 3. Agregar columnas en tabla de pagos para almacenar el id del cliente al que se realizo el pago y si ha sido enviado a MegaManager exitosamente
alter table pagos add column idCliente text not null default '';
alter table pagos add column enviadoMegaManager text not null default 'S';

-- 4. Agregar columna en tabla de creditosManualesXmaquinas para guardar si ha sido enviada a MegaManager exitosamente
alter table creditosManualesXmaquinas add column enviadoMegaManager text not null default 'S';
