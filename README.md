# flask-sql

Aplicación web simple de balance de ingresos y gastos con Flask y SQL

## Cómo lanzar el programa para usarlo

1. Crear un entorno virtual

   ```shell
   # Windows
   python -m venv env

   # Mac / Linux
   python3 -m venv env
   ```

2. Activar el entorno virtual

   ```shell
    # Windows
    env\Scripts\activate

    # Mac / Linux
    source ./env/bin/activate

3. Instalar las dependencias

   ```shell
   pip install -r requirements.txt
   ```

4. Hacer una copia del archivo `.env_template` como `.env`

   ```shell
   # Windows
   copy .env_template .env

   # Mac / Linux
   cp .env_template .env
   ```

5. Editar el archivo `.env` y cambiar los valores de
   entorno necesarios. Por motivos de seguridad, dejar
   la variable `DEBUG` con el valor `False`.

6. Con el entorno virtual activo, lanzar la aplicación

   ```shell
   flask run
   ```

## Cómo lanzar el programa en desarrollo

1. Crear un entorno virtual

   ```shell
   # Windows
   python -m venv env

   # Mac / Linux
   python3 -m venv env
   ```

2. Activar el entorno virtual

   ```shell
    # Windows
    env\Scripts\activate

    # Mac / Linux
    source ./env/bin/activate

3. Instalar las dependencias

   ```shell
   pip install -r requirements.dev.txt
   ```

4. Hacer una copia del archivo `.env_template` como `.env`

   ```shell
   # Windows
   copy .env_template .env

   # Mac / Linux
   cp .env_template .env
   ```

5. Editar el archivo `.env` y cambiar (o no) el valor de `DEBUG` (`True`/`False`)
