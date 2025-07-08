CREATE DATABASE ventas;
CREATE TABLE ventas.clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    telefono VARCHAR(20)
);
CREATE TABLE ventas.productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);
CREATE TABLE ventas.pedidos (
    id_pedido INT PRIMARY KEY,
    id_cliente INT,
    fecha DATE,
    total DECIMAL(10,2)
);
CREATE TABLE ventas.detalle_pedido (
    id_detalle INT PRIMARY KEY,
    id_pedido INT,
    id_producto INT,
    cantidad INT,
    subtotal DECIMAL(10,2)
);
INSERT INTO ventas.clientes(id_cliente,nombre,correo,telefono) VALUES (1, 'Ana Torres', 'ana.torres@mail.com', '912345678');
INSERT INTO ventas.clientes(id_cliente,nombre,correo,telefono) VALUES (2, 'Luis Pérez', 'luis.perez@mail.com', '987654321');
INSERT INTO ventas.clientes(id_cliente,nombre,correo,telefono) VALUES (3, 'Maria Alvarado', 'maria.alvarado@mail.com', '85963214');

INSERT INTO ventas.productos (id_producto, nombre, precio, stock)VALUES(1, 'Teclado', 15990, 100);
INSERT INTO ventas.productos (id_producto, nombre, precio, stock)VALUES(2, 'Mouse', 8990, 200);
INSERT INTO ventas.productos (id_producto, nombre, precio, stock)VALUES(3, 'Monitor 24"', 119990, 50);

INSERT INTO ventas.pedidos (id_pedido, id_cliente, fecha, total)VALUES(101, 1, '2025-07-01', 149980);
INSERT INTO ventas.pedidos (id_pedido, id_cliente, fecha, total)VALUES(102, 2, '2025-07-02', 8990);

INSERT INTO ventas.detalle_pedido (id_detalle, id_pedido, id_producto,cantidad,subtotal)VALUES(1, 101, 1, 2, 31980);
INSERT INTO ventas.detalle_pedido (id_detalle, id_pedido, id_producto,cantidad,subtotal)VALUES(2, 101, 3, 1, 119990);
INSERT INTO ventas.detalle_pedido (id_detalle, id_pedido, id_producto,cantidad,subtotal)VALUES(3, 102, 2, 1, 8990);

-- PREGUNTAS

-- 1.   Agregue la columna region a la tabla clientes
ALTER TABLE ventas.clientes ADD region VARCHAR(30);
-- 2.   Agregue la columna id_cliente como clave foranea para la tabla pedidos
ALTER TABLE ventas.pedidos ADD CONSTRAINT fk_cliente FOREIGN KEY(id_cliente) REFERENCES ventas.pedidos(id_cliente);
-- 3.   Agregue la columna id_pedido como clave foranea para la tabla detalle_pedido
ALTER TABLE ventas.detalle_pedido ADD CONSTRAINT fk_pedido FOREIGN KEY(id_pedido) REFERENCES ventas.detalle_pedido(id_pedido);
-- 4.   Agregue la columna id_producto como clave foranea para la tabla detalle_pedido
ALTER TABLE ventas.detalle_pedido ADD CONSTRAINT fk_producto FOREIGN KEY(id_producto) REFERENCES ventas.detalle_pedido(id_producto);
-- 5.   Cambie el nombre de la columna subtotal por total
ALTER TABLE  ventas.detalle_pedido CHANGE subtotal DECIMAL(10,2);
-- 6.   Actualice el stock del producto mouse a 150 
UPDATE ventas.productos 
SET stock = 150
WHERE nombre = "Mouse";
-- 7.   Actualice la region de todos los clientes por Araucanía
UPDATE ventas.clientes SET region = "Araucanía";
-- 8.   Actualice la fecha del pedido 101 por la fecha de hoy
UPDATE ventas.pedidos SET fecha = '08-07-2025' WHERE id_pedido = 101; 
-- 9.   Elimine el pedido con total 8990
DELETE FROM ventas.pedidos WHERE total = 8990;
-- 10.  Elimine al usuario Maria Alvarado
DELETE FROM ventas.clientes WHERE nombre = 'Maria Alvarado';