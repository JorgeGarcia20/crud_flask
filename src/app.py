from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash

from src.models.entities.cliente import Cliente
from src.models.entities.compra import Compra

from src.models.ModeloCliente import ModeloCliente
from src.models.ModeloCategoria import ModeloCategoria
from src.models.ModeloProveedor import ModeloProveedor
from src.models.ModeloProducto import ModeloProducto
from src.models.ModeloCompra import ModeloCompra
from src.consts import *

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModeloCliente.obtener_id(db, id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # CSRF (Cross-site Request Forgery): Solicitud de falsificación entre sitios.
    if request.method == 'POST':
        usuario = Cliente(
            None, None, None, request.form['nick'], request.form['password'], None, None, None)
        usuario_logeado = ModeloCliente.login(db, usuario)
        if usuario_logeado != None:
            login_user(usuario_logeado)
            flash(BIENVENIDA, 'success')
            return redirect(url_for('index'))
        else:
            flash(LOGIN_NO_VALIDO, 'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))


@app.route("/")
def index():
    if current_user.is_authenticated:
        ventas = ModeloCompra.consultar_productos_cliente(db, current_user.id)
        return render_template('index.html', data=ventas)
    else:
        return redirect(url_for('login'))


@app.route("/nuevo_cliente")
def nuevo_cliente():
    return render_template('registrar_cliente.html')


@app.route("/registrar_cliente", methods=['POST'])
def registrar_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        nick = request.form['nick']
        password = generate_password_hash(request.form['password'])
        correo = request.form['correo']
        rfc = request.form['rfc']
        direccion = request.form['direccion']

        ModeloCliente.registrar(db, nombre, apellidos, nick,
                                password, correo, rfc, direccion)
        flash(NUEVO_CLIENTE, 'success')
        return redirect(url_for('login'))
    else:
        flash(ALERT, 'warning')
        return render_template('registrar_cliente.html')


@app.route("/productos")
@login_required
def productos():
    categorias = ModeloCategoria.obtener_categorias(db)
    provedores = ModeloProveedor.obtener_proveedores(db)
    productos = ModeloProducto.consultar_productos(db)
    data = {
        'categorias': categorias,
        'proveedores': provedores,
        'productos': productos
    }
    return render_template('productos.html', data=data)


@app.route("/agregar_producto", methods=['GET', 'POST'])
@login_required
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        proveedor = request.form.get('proveedor')
        categoria = request.form.get('categoria')
        precio = request.form['precio']
        ModeloProducto.agregar_producto(
            db, nombre, marca, proveedor, categoria, precio)
        return redirect(url_for('productos'))
    else:
        return render_template('productos.html')


@app.route("/actualizar_producto/<id_producto>")
@login_required
def actualizar_producto(id_producto):
    producto = ModeloProducto.consultar_por_id(db, id_producto)
    categorias = ModeloCategoria.obtener_categorias(db)
    provedores = ModeloProveedor.obtener_proveedores(db)

    data = {
        'producto': producto[0],
        'categorias': categorias,
        'proveedores': provedores
    }

    return render_template('editar_producto.html', data=data)


@app.route("/editar_producto/<id_producto>", methods=['GET', 'POST'])
@login_required
def editar_producto(id_producto):
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        proveedor = request.form.get('proveedor')
        categoria = request.form.get('categoria')
        precio = request.form['precio']
        ModeloProducto.editar_producto(
            db, nombre, marca, proveedor, categoria, precio, id_producto)
        return redirect(url_for('productos'))
    else:
        return render_template('productos.html')


@app.route("/eliminar_producto/<id_producto>", methods=['GET', 'POST'])
@login_required
def eliminar_producto(id_producto):
    ModeloProducto.eliminar_producto(db, id_producto)
    return redirect(url_for('productos'))


@app.route("/nueva_venta", methods=['GET', 'POST'])
@login_required
def nueva_venta():
    productos = ModeloProducto.consultar_productos(db)
    return render_template('ventas.html', data=productos)


@app.route("/vender_producto/<id_producto>", methods=['GET', 'POST'])
def vender_producto(id_producto):
    id_cliente = current_user.id
    venta = ModeloCompra.vender(db, id_producto, id_cliente)
    if venta == None:
        flash(NUEVA_VENTA, 'success')
        return redirect(url_for('nueva_venta'))
    else:
        flash(ERROR_VENTA, 'warning')
        return render_template('ventas.html')


def start_app(configuration):
    app.config.from_object(configuration)
    csrf.init_app(app)
    return app
