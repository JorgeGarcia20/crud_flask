# from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
# from flask_mysqldb import MySQL
# from flask_wtf.csrf import CSRFProtect
# from flask_login import LoginManager, login_user, logout_user, login_required, current_user
# from werkzeug.security import generate_password_hash
# from src.models.ModeloSeleccion import ModeloSeleccion
# # from flask_mail import Mail

# from src.models.entities.usuario import Usuario
# from src.models.entities.compra import Compra
# from src.models.ModeloVenta import ModeloVenta
# from src.models.ModeloUsuario import ModeloUsuario
# from src.models.ModeloCategoria import ModeloCategoria
# from src.models.ModeloProveedor import ModeloProveedor
# from src.models.ModeloProducto import ModeloProducto
# from src.models.ModeloCompra import ModeloCompra
# from src.consts import *
# from .emails import bienvenida_nuevo_usuario

# app = Flask(__name__)
# csrf = CSRFProtect()
# db = MySQL(app)
# login_manager_app = LoginManager(app)
# # mail = Mail()


# @login_manager_app.user_loader
# def load_user(id):
#     return ModeloUsuario.obtener_id(db, id)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # CSRF (Cross-site Request Forgery): Solicitud de falsificación entre sitios.
#     if request.method == 'POST':
#         usuario = Usuario(
#             None, None, None, request.form['nick'], request.form['password'], None)
#         usuario_logeado = ModeloUsuario.login(db, usuario)
#         if usuario_logeado != None:
#             login_user(usuario_logeado)
#             flash(BIENVENIDA, 'success')
#             return redirect(url_for('index'))
#         else:
#             flash(LOGIN_NO_VALIDO, 'warning')
#             return render_template('auth/login.html')
#     else:
#         return render_template('auth/login.html')


# @app.route('/logout')
# def logout():
#     logout_user()
#     flash(LOGOUT, 'success')
#     return redirect(url_for('login'))


# @app.route("/")
# @login_required
# def index():
#     if current_user.is_authenticated:
#         ventas = ModeloVenta.productos(db)
#         return render_template('index.html', data=ventas)
#     else:
#         return redirect(url_for('login'))


# @app.route("/nuevo_cliente")
# def nuevo_cliente():
#     return render_template('registrar_cliente.html')


# @app.route("/registrar_cliente", methods=['POST'])
# def registrar_cliente():
#     if request.method == 'POST':
#         nombre = request.form['nombre']
#         apellidos = request.form['apellidos']
#         nick = request.form['nick']
#         password = generate_password_hash(request.form['password'])
#         correo = request.form['correo']
#         ModeloUsuario.registrar(db, nombre, apellidos, nick,
#                                 password, correo)
#         flash(NUEVO_CLIENTE, 'success')
#         bienvenida_nuevo_usuario(correo)
#         return redirect(url_for('login'))
#     else:
#         flash(ALERT, 'warning')
#         return render_template('registrar_cliente.html')


# @app.route("/productos")
# @login_required
# def productos():
#     categorias = ModeloCategoria.obtener_categorias(db)
#     provedores = ModeloProveedor.obtener_proveedores(db)
#     productos = ModeloProducto.consultar_productos(db)
#     data = {
#         'categorias': categorias,
#         'proveedores': provedores,
#         'productos': productos
#     }
#     return render_template('productos.html', data=data)


# @app.route("/agregar_producto", methods=['GET', 'POST'])
# @login_required
# def agregar_producto():
#     if request.method == 'POST':
#         nombre = request.form['nombre']
#         marca = request.form['marca']
#         proveedor = request.form.get('proveedor')
#         categoria = request.form.get('categoria')
#         precio = request.form['precio']
#         ModeloProducto.agregar_producto(
#             db, nombre, marca, proveedor, categoria, precio)
#         flash(NUEVO_PRODUCTO, 'success')
#         return redirect(url_for('productos'))
#     else:
#         flash(ALERT, 'warning')
#         return render_template('productos.html')


# @app.route("/actualizar_producto/<id_producto>")
# @login_required
# def actualizar_producto(id_producto):
#     producto = ModeloProducto.consultar_por_id(db, id_producto)
#     categorias = ModeloCategoria.obtener_categorias(db)
#     provedores = ModeloProveedor.obtener_proveedores(db)

#     data = {
#         'producto': producto[0],
#         'categorias': categorias,
#         'proveedores': provedores
#     }

#     return render_template('editar_producto.html', data=data)


# @app.route("/editar_producto/<id_producto>", methods=['GET', 'POST'])
# @login_required
# def editar_producto(id_producto):
#     if request.method == 'POST':
#         nombre = request.form['nombre']
#         marca = request.form['marca']
#         proveedor = request.form.get('proveedor')
#         categoria = request.form.get('categoria')
#         precio = request.form['precio']
#         ModeloProducto.editar_producto(
#             db, nombre, marca, proveedor, categoria, precio, id_producto)
#         flash(MODIFICADO, 'success')
#         return redirect(url_for('productos'))
#     else:
#         flash(ALERT, 'warning')
#         return render_template('productos.html')


# @app.route("/eliminar_producto/<id_producto>", methods=['GET', 'POST'])
# @login_required
# def eliminar_producto(id_producto):
#     ModeloProducto.eliminar_producto(db, id_producto)
#     flash(ELIMINADO, 'success')
#     return redirect(url_for('productos'))


# @app.route("/nueva_venta", methods=['GET', 'POST'])
# @login_required
# def nueva_venta():
#     productos = ModeloProducto.consultar_productos(db)
#     detalle_productos = ModeloSeleccion.detalle_producto(db)

#     sumatoria = []
#     for d in detalle_productos:
#         sumatoria.append(float(d.precio))
#     total = ModeloProducto.sumar_precios(sumatoria)

#     data = {
#         'productos': productos,
#         'detalle_productos': detalle_productos,
#         'total': total
#     }

#     return render_template('ventas.html', data=data)


# @app.route("/seleccionar_producto/<id_producto>", methods=['GET', 'POST'])
# @login_required
# def seleccionar_producto(id_producto):
#     ModeloSeleccion.producto_seleccionado(db, id_producto)
#     return redirect(url_for('nueva_venta'))


# @app.route("/eliminar_seleccion/<id_producto>", methods=['GET', 'POST'])
# @login_required
# def eliminar_seleccion(id_seleccion):
#     ModeloSeleccion.eliminar_seleccion(db, id_seleccion)
#     return redirect(url_for('nueva_venta'))


# @app.route("/guardar_venta", methods=['GET', 'POST'])
# @login_required
# def guardar_venta():
#     if request.method == 'POST':
#         nombre = request.form['nombre']
#         apellidos = request.form['apellidos']
#         correo = request.form['correo']
#         rfc = request.form['rfc']
#         direccion = request.form['direccion']
#         total = request.form['total']
#         ModeloVenta.nueva_venta(
#             db, nombre, apellidos, correo, rfc, direccion, total)
#         ModeloSeleccion.vaciar_tabla(db)
#         flash(NUEVA_VENTA, 'success')
#         return redirect(url_for('nueva_venta'))
#     else:
#         flash(ALERT, 'warning')
#         return render_template('ventas.html')


# def pagina_no_encontrada(error):
#     return render_template('error/404.html'), 404


# def pagina_no_autorizada(error):
#     return redirect(url_for('login'))


# def start_app(configuration):
#     app.config.from_object(configuration)
#     csrf.init_app(app)
#     # mail.init_app(app)
#     app.register_error_handler(401, pagina_no_autorizada)
#     app.register_error_handler(404, pagina_no_encontrada)
#     return app
