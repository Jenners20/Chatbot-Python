from core import message_probability
import random

#Realizar un chatbot para responder preguntas básicas
def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Saludos, en qué puedo ayudarle?', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('Software, Multimedia, Redes, Mecatronica', ['cuales', 'principales', 'carreras', 'tecnologos'], single_response=True)
        response('Nuestro Rector se llama Omar Mendez', ['como', 'llama', 'rector', 'director'], single_response=True)
        response('Nuestro numero de telefono es: (809) 738-4852', ['cual', 'numero', 'telefono','contacto','llamarlos','llamarles'], single_response=True)
        response('Nuestro correo electronico es: info@itla.edu.do', ['cual', 'corre', 'electronico','contacto','email','mail','escribirles'], single_response=True)
        response('Nuestra direccion es: Autopista Las Américas, km. 27, PCSD, La Caleta, Boca Chica', ['cual', 'direccion', 'ubicacion','ubicados','estan'], single_response=True)
        response('ITLA Virtual', ['cual', 'plataforma', 'virtual','nombre','clases'], single_response=True)
        response('Orbi', ['cual', 'nombre', 'administrativa','nombre','plataforma','pagos'], single_response=True)
        response('Nuestras carreras tienen un promedio de duracion de 2 años y medio', ['cuanto', 'carreras', 'duran','tarda','tiempo'], single_response=True)
        response('Si vives en el interior puedes quedarte en nuestra residencia', ['Puedo', 'allá', 'estudiar','provincia','interior','vivo'], single_response=True)
        response('Hasta luego, esperamos poder verte en nuestro nuevo campus', ['gracias', 'muchas', 'adios','amable','bye','placer','ok'], single_response=True)
        best_match = max(highest_prob, key=highest_prob.get)
       

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['Puedes repetir la pregunta?', 'No estoy seguro de lo quieres', 'No cuento con esa informacion','Creo que no te entiendo'][random.randrange(3)]
    return response
