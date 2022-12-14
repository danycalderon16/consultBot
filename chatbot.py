import re
import random

def get_response(user_input):
    user_input = user_input.replace(' ','')
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('Para registrar un chofer haz clic en el boton de + y completa el fomulario',['registro'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        response('Ha sido un placer ayudarte', ['adios', 'Vuelve pronto', 'bye'], single_response=True)
        response('Para modificar un chófer, haz clic primero sobre el conductor que quieres cambiar algo, luego en la siguiente página haz clic en el botón del lápiz',['Modificar chofer','Modificarchofer','modificarchofer', 'ModificarChofer', 'ModificarChófer', 'Modificarchófer', 'modificarchófer'],single_response=True)
        response('Para eliminar un chófer, desplace hacia la izquierda el item del conductor que desea dar de baja',['Eliminar chofer','Eliminarchofer', 'eliminarchofer', 'EliminarChofer', 'Eliminarchófer', 'eliminarchófer', 'EliminarChófer'],single_response=True)
        response('Para consultar un chófer haga clic sobre el item del conductor que desea conocer su información',['Consultar chofer','Consultarchofer', 'consultarchofer', 'ConsultarChofer', 'Consultarchófer', 'consultarchófer', 'ConsultarChófer'],single_response=True)
        response('Para registrar un camión haz clic en el boton de + y completa el fomulario',['Registrar camión','Registrarcamión', 'registrarcamión', 'RegistrarCamión'], required_words=['Registrar','registrar'])
        response('Para modificar un camión, pide al administrador activar el módulo de "Modificar Camión"',['Modificar camión','Modificarcamión','modificarcamión', 'ModificarCamión'],single_response=True)
        response('Para eliminar un camión, desplace hacia la izquierda el item del camión que desea dar de baja',['Eliminar camión','Eliminarcamión', 'eliminarcamión', 'EliminarCamión'],single_response=True)
        response('Para consultar un camión, pide al administrador activar el módulo de "Modificar Camión"',['Consultar camión', 'Consultarcamión','consultarcamión', 'ConsultarCamión','ConsultarCamion','consultarcamion'],single_response=True)
        response('Para consultar esa infomación pida a su administrador activar el módulo de consulta de pasajeros con filtro de estudiantes',['Estudiantes','estudiantes','¿Cuántos estudiantes tomaron camión hoy?'],single_response=True)
        response('Para consultar esa infomación pida a su administrador activar el módulo de consulta de pasajeros',['Pasajero normal','normal','pasajero','¿Cuántos pasajeros normales tomaron camión hoy?'],single_response=True)
        response('Hay mucho por agregar a este proyecto aún, no desesperes, que lo mejor está por venir',['Novedades','novedades','¿Qué hay de nuevo?'],single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal','se más explicito porfavor'][random.randrange(4)]
    return response
# while True:
#     print("Bot: " + get_response(input('You: ')))