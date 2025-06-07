# 🚀 Instrucciones para levantar la aplicación

Este proyecto está desarrollado con **Python 3** y **Django**. Sigue los pasos a continuación para ponerlo en marcha en tu entorno local.  

---

## ✅ Requisitos previos

- Tener **Python 3** instalado en tu sistema.
- Tener **Git** instalado (opcional, pero recomendado para clonar el repositorio).

---

## 🛠️ Pasos para ejecutar la aplicación

1. **Clonar el repositorio**:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. **Crear y activar un entorno virtual**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. **Instalar las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones**:

   ```bash
   python manage.py migrate
   ```

5. **Iniciar el servidor**:

   ```bash
   python manage.py runserver
   ```

---

## 🌐 Enlace principal de la aplicación

Accede a la interfaz principal desde:  
[http://localhost:8000/ventas/](http://localhost:8000/ventas/)

---

## 📌 Notas

- Asegúrate de estar en el directorio raíz del proyecto antes de ejecutar los comandos.
- Puedes crear un superusuario con `python manage.py createsuperuser` para acceder al panel de administración si es necesario.

---

¡Listo! Tu aplicación está corriendo localmente 🚀
