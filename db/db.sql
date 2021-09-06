DROP DATABASE IF EXISTS tienda_test;
CREATE DATABASE tienda_test CHARACTER SET utf8 COLLATE utf8_general_ci;
USE tienda_test;

CREATE TABLE cliente(
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(30) NOT NULL,
  apellidos VARCHAR(50) NOT NULL,
  nick VARCHAR(20) NOT NULL,
  password CHAR(120) NOT NULL,
  correo VARCHAR(60) NOT NULL,
  rfc VARCHAR(10) NOT NULL,
  direccion VARCHAR(250) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE proveedor(
  id_proveedor INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50),
  PRIMARY KEY(id_proveedor)
);

CREATE TABLE categoria(
  id_categoria INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50),
  PRIMARY KEY(id_categoria)
);

CREATE TABLE producto(
  id_producto INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(30) NOT NULL, 
  marca VARCHAR(30) NOT NULL,
  precio DECIMAL(5,2) NOT NULL,
  id_proveedor INT NOT NULL,
  id_categoria INT NOT NULL,
  FOREIGN KEY(id_proveedor) REFERENCES proveedor(id_proveedor),
  FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria),
  PRIMARY KEY(id_producto)
);

CREATE TABLE venta(
  id_venta INT NOT NULL AUTO_INCREMENT,
  fecha DATETIME NOT NULL,
  factura TINYINT(1) NOT NULL,
  total DECIMAL(5,2),
  PRIMARY KEY(id_venta)
);

CREATE TABLE detalle_venta(
  id_detalle_venta INT NOT NULL AUTO_INCREMENT,
  id_venta INT NOT NULL,
  id_cliente INT NOT NULL,
  id_producto INT NOT NULL,
  FOREIGN KEY(id_venta) REFERENCES venta(id_venta),
  FOREIGN KEY(id_cliente) REFERENCES cliente(id),
  FOREIGN KEY(id_producto) REFERENCES producto(id_producto),
  PRIMARY KEY(id_detalle_venta)
);

INSERT INTO cliente(nombre, apellidos, nick, password, correo, rfc, direccion)
VALUE ('Jorge', 'Garcia Estrada', 'jorgegarcia', 'pbkdf2:sha256:260000$JJVqzW0AXKMuUQXr$ec2795ab8a7ae82df79eee2e477fc405524d66fbcb867fe16c81d227a7aac0b6', 'jorge@outlook.com', 'GAEJ991020', 'Francisco Villa s/n Tepetzongo');

INSERT INTO proveedor(nombre) VALUES
('Bimbo SA de CV'), 
('CocaCola Company'), 
('Sabritas SA de CV'), 
('Frutas y verduras el wero'),
('Grupo Modelo SA de CV'),
('Pedigree SA de CV'), 
('Holanda SA de CV'),
('Abarrotes el Zorro'), 
('Herdez SA de CV');

INSERT INTO categoria(nombre) VALUES
('Belleza e Higiene'),
('Cervezas y Snacks'),
('Helados'),
('Abarrotes'),
('Verduras/Frutas procesadas'),
('Mascotas'),
('Refrescos y Bebidas energeticas');