import os
from flask import flash, redirect, render_template, request, url_for

from . import app
from .forms import MovimientoForm
from .models import DBManager


RUTA = os.path.join('data', 'balance.db')


@app.route('/')
def home():
    # Ruta principal que muestra todos los movimientos.
    """
    Muestra una tabla con todos los movimientos.
    """
    db = DBManager(RUTA)
    consulta = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos'
    movimientos = db.consultaSQL(consulta)
    return render_template('inicio.html', movs=movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    # Ruta para agregar un nuevo movimiento, GET muestra el formulario, POST agrega el movimiento a la base de datos.

    """
    GET: muestra el formulario vacío
    POST: recoge los datos del formulario,
          crea el movimiento en la base de datos,
          vuelve a la página de inicio
    TODO: modificar el template del formulario para que envíe los datos a /modificar o /nuevo
          (el action del formulario debe ser dinámico)
    """
    if request.method == 'GET':
        formulario = MovimientoForm()
        return render_template('form_movimiento.html', form=formulario)
    return 'TODO: tratar POST para agregar movimiento'


@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def actualizar(id):
    # Ruta para actualizar un movimiento existente.
    """
    Actualiza los datos de un movimiento.
    """
    if request.method == 'GET':
        db = DBManager(RUTA)
        movimiento = db.obtenerMovimiento(id)
        formulario = MovimientoForm(data=movimiento)
        return render_template('form_movimiento.html', form=formulario, id=id)
    elif request.method == 'POST':
        form = MovimientoForm(data=request.form)
        if form.validate():
            db = DBManager(RUTA)
            consulta = 'UPDATE movimientos SET fecha=?, concepto=?, tipo=?, cantidad=? WHERE id=?'
            params = (
                form.fecha.data,
                form.concepto.data,
                form.tipo.data,
                form.cantidad.data,
                form.id.data
            )
            resultado = db.consultaConParametros(consulta, params)
            if resultado:
                # genero un mensaje flash que se va a mostrar en la siguiente página
                flash('El movimiento se ha actualizado correctamente',
                      category='exito')
                return redirect(url_for('home'))
            return render_template(
                'form_movimiento.html',
                form=form,
                id=id,
                errores=['El movimiento no se ha podido guardar en la base de datos'])
        else:
            return render_template(
                'form_movimiento.html',
                form=form,
                id=id,
                errores=["Los datos no son válidos"])


@app.route('/borrar/<int:id>')
def eliminar(id):
    # Ruta para eliminar un movimiento por su ID.
    """
    Elimina un movimiento.
    TODO: En lugar de mostrar otro template, usar un mensaje flash
    TODO: Al pulsar el botón "papelera" en lugar de eliminar directamente,
          mostrar una página que pida confirmación.
          Debe tener:
            - Mensaje pidiendo confirmación
            - Botón "Eliminar" elimina el movimiento y vuelve a la página de inicio
            - Botón "Cancelar" vuelve a la página de inicio sin eliminar el movimiento
    """
    db = DBManager(RUTA)
    esta_borrado = db.borrar(id)
    return render_template('borrado.html', resultado=esta_borrado)
