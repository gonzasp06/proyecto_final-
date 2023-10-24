def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    if environ['PATH_INFO'] == '/formulario_smartphone':
        # Cargar las respuestas de formulario_smartphone.html y enviar como respuesta
        with open('formulario_smartphone.html', 'r') as file:
            response = file.read()
            
    if environ['PATH_INFO'] == '/formulario_tv':
        # Cargar las respuestas de formulario_smartphone.html y enviar como respuesta
        with open('formulario_tv.html', 'r') as file:
            response = file.read()
            
    elif environ['PATH_INFO'] == '/eleccion_equipo':
        # Cargar las respuestas de eleccion_equipo.html y enviar como respuesta
        with open('eleccion_equipo.html', 'r') as file:
            response = file.read()
            
    elif environ['PATH_INFO'] == '/index':
        # Cargar las respuestas de index.html y enviar como respuesta
        with open('index.html', 'r') as file:
            response = file.read()
            
    elif environ['PATH_INFO'] == '/ordenes':
        # Cargar las respuestas de ordenes.html y enviar como respuesta
        with open('ordenes.html', 'r') as file:
            response = file.read()
    else:
        response = 'ERROR'

    return [response.encode('utf-8')]

