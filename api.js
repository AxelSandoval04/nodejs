const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(bodyParser.json());
app.use(cors());

const db = mysql.createPool({
    host: '189.197.187.187',
    user: 'alumnos',
    password: 'Alumnos1010$',
    database: 'controlescolar',
});

// Endpoint para verificar que la API está funcionando
app.get('/', (req, res) => {
    res.send("Hola mundo 2");
});

// Obtener todos los profesores
app.get('/profesores', (req, res) => {
    const sql = 'SELECT * FROM profesores';
    db.query(sql, (err, result) => {
        if (!err) {
            res.status(200).send(result);
        } else {
            res.status(500).send(err);  // Cambiado el código de estado a 500 para errores del servidor
        }
    });
});

// Obtener un profesor por ID
app.get('/profesor/:id', (req, res) => {
    const identificador = req.params.id;
    const sql = 'SELECT * FROM profesores WHERE id = ?';
    db.query(sql, [identificador], (err, result) => {
        if (!err) {
            res.status(200).send(result);
        } else {
            res.status(500).send(err);  // Cambiado el código de estado a 500 para errores del servidor
        }
    });
});

// Registrar un nuevo profesor
app.post('/profesores/registrar', (req, res) => {
    const { id, nombre, correo, direccion } = req.body;
    const sql = 'INSERT INTO profesores (id, nombre, correo, direccion) VALUES (?, ?, ?, ?)';
    db.query(sql, [id, nombre, correo, direccion], (err, resultado) => {
        if (!err) {
            res.status(201).send({
                resultado,
                mensaje: 'Profesor registrado',
            });
        } else {
            res.status(500).send({
                err,
                mensaje: 'No se registró el profesor',
            });
        }
    });
});

// Modificar un profesor existente
app.put('/profesores/modificar/:id', (req, res) => {
    const { id } = req.params;
    const { nombre, correo, direccion } = req.body;
    const sql = 'UPDATE profesores SET nombre = ?, correo = ?, direccion = ? WHERE id = ?';
    db.query(sql, [nombre, correo, direccion, id], (err, result) => {
        if (!err) {
            res.status(200).send({
                result,
                mensaje: 'Profesor modificado',
            });
        } else {
            res.status(500).send({
                err,
                mensaje: 'No se modificó el profesor',
            });
        }
    });
});

// Eliminar un profesor por ID
app.delete('/profesores/eliminar/:id', (req, res) => {
    const identificador = req.params.id;
    const sql = 'DELETE FROM profesores WHERE id = ?';
    db.query(sql, [identificador], (err, result) => {
        if (!err) {
            res.status(200).send({
                result,
                mensaje: 'Profesor eliminado',
            });
        } else {
            res.status(500).send(err);  // Cambiado el código de estado a 500 para errores del servidor
        }
    });
});

// Manejo de rutas no definidas
app.all('*', (req, res) => {
    res.status(404).send("Esta dirección no existe, contacta a tu administrador o proveedor");  // Cambiado el código de estado a 404 para recursos no encontrados
});

app.listen(port, () => {
    console.log(`Escuchando en el puerto ${port}`);
});
