def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    if environ['PATH_INFO'] == '/form_handler':
        if environ['REQUEST_METHOD'] == 'POST':
            # Leer los datos del formulario POST desde `environ['wsgi.input']`
            post_data = environ['wsgi.input'].read().decode('utf-8')

            # Aquí puedes procesar los datos del formulario como sea necesario
            # Por ejemplo, puedes dividir los datos en pares clave-valor
            form_data = {item.split('=')[0]: item.split('=')[1] for item in post_data.split('&')}

            nombre = form_data.get('nombre')
            telefono = form_data.get('telefono')
            equipo = form_data.get('equipo')
            falla = form_data.get('falla')

            # Enviar el contenido de formulario.html como respuesta
            with open('templates/formulario.html', 'r') as file:
                response = file.read()

            return [response.encode('utf-8')]
    
    # Resto de la lógica de la aplicación

    
    # Resto de la lógica de la aplicación
