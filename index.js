const mysql = require('mysql2');
const express= require('express');
const app = express();
const port = 5000;

const db =mysql.createConnection({host : '189.197, 187.187'})

app.get('/',(req,res)=>{
    res.send("Hola Mundo");
});
app.get('/profesor',(req,res)=>{
    const sql='SELECT * FROM profesor';
    db.query(sql, (err, result=>{
        if(!err){
            res.status(200).send(result);
        }
        else{
            
        }
    }))
    const respuesta ={
        "id":5,
        "Nombre":"Dagoberto fiscal",
        "correo": "Dago@gmail.com",
        "direccion": "5 de febrero 100",
        "telefono": "6182839123",
    }
    res.status(200).send(respuesta);
});



app.all('*',(req, res)=>{
    res.send("esta direccion no existe, contacta a tu administrador o proveedor")
});
app.listen(port, ()=>{
    console.log(`Escuchando en el puerto $`)
})
app.listen(5000,()=>{
    console.log("Estamos escuchando el puerto 5000")
});