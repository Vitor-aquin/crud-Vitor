from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuração de conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Usuário do MySQL (padrão é root)
        password="",       # Senha (padrão do XAMPP é em branco)
        database="flask_db"  # Nome do banco de dados criado no phpMyAdmin
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")  # Consulta na tabela de usuários
    usuarios = cursor.fetchall()  # Retorna todos os usuários
    cursor.close()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/adicionar', methods=['POST'])
def adicionar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
