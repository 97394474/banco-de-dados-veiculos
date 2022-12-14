CREATE DATABASE Veiculos;
USE Veiculos;

CREATE TABLE Veiculos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_modelo INT, 
    ano INT, 
    placa CHAR(7), 
    id_categoria INT, 
  FOREIGN KEY (id_modelo) REFERENCES    modelos(id), 
  FOREIGN KEY (id_categoria) REFERENCES categorias(id) 
);

CREATE TABLE modelos (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    nome VARCHAR(45)
);

CREATE TABLE categorias (
     id INT PRIMARY KEY AUTO_INCREMENT, 
     nome VARCHAR(45)
);

show databases;
drop database veiculos;

SELECT v.id, v.id_modelo,  m.nome AS nome_modelo, v.ano, v.placa FROM veiculos v JOIN modelos m ON v.id_modelo = v.id;