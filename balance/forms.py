from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, HiddenField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired


class MovimientoForm(FlaskForm):
    id = HiddenField()  # Campo oculto para almacenar el ID del movimiento.
    fecha = DateField('Fecha', validators=[DataRequired(
        message="Debes introducir una fecha")])  # Campo para la fecha del movimiento.
    concepto = StringField('Concepto', validators=[
                           DataRequired(message="Debes especificar un concepto")])  # Campo para el concepto del movimiento.
    tipo = RadioField(
        choices=[('I', 'Ingreso'), ('G', 'Gasto')], validators=[DataRequired()])  # Campo para el tipo de movimiento (Ingreso/Gasto).
    cantidad = FloatField('Cantidad', validators=[DataRequired(
        message="La cantidad debe tener un valor")])  # Campo para la cantidad del movimiento.
    submit = SubmitField('Guardar')  # Botón para enviar el formulario.
