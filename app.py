from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = '189.197.187.187'
app.config['MYSQL_USER'] = 'alumnos'
app.config['MYSQL_PASSWORD'] = 'Alumnos1010$'
app.config['MYSQL_DB'] = 'controlescolar'

mysql = MySQL(app)

def add_profesor(id, nombre, correo, direccion):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO profesores (id, nombre, correo, direccion) VALUES (%s, %s, %s, %s)", (id, nombre, correo, direccion))
    mysql.connection.commit()
    cur.close()
    print("Profesor registrado")

def update_profesor(id, nombre, correo, direccion):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE profesores SET nombre = %s, correo = %s, direccion = %s WHERE id = %s", (nombre, correo, direccion, id))
    mysql.connection.commit()
    cur.close()
    print("Profesor modificado")

def delete_profesor(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM profesores WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    print("Profesor eliminado")

def get_profesores():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM profesores")
    profesores = cur.fetchall()
    cur.close()
    for profesor in profesores:
        print(profesor)

def get_profesor(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM profesores WHERE id = %s", (id,))
    profesor = cur.fetchone()
    cur.close()
    print(profesor)

def report():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM profesores")
    profesores = cur.fetchall()
    cur.close()
    for profesor in profesores:
        print(profesor)

def exit_app():
    print("Gracias por usar la aplicación!")
    os._exit(0)

def show_menu():
    print("1. Agregar profesor")
    print("2. Modificar profesor")
    print("3. Eliminar profesor")
    print("4. Consultar profesor")
    print("5. Reportar profesores")
    print("6. Salir")

@app.route('/run_console', methods=['GET'])
def run_console():
    while True:
        show_menu()
        choice = input("Seleccione una opción: ")
        if choice == '1':
            id = input("ID: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")
            add_profesor(id, nombre, correo, direccion)
        elif choice == '2':
            id = input("ID: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")
            update_profesor(id, nombre, correo, direccion)
        elif choice == '3':
            id = input("ID: ")
            delete_profesor(id)
        elif choice == '4':
            id = input("ID: ")
            get_profesor(id)
        elif choice == '5':
            report()
        elif choice == '6':
            exit_app()
        else:
            print("Opción no válida")

if __name__ == '__main__':
    app.run() 
