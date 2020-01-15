# encoding: utf-8
import logging

class Bot(object):
    """docstring for ClassName"""
    def __init__(self, send_callback, users_dao, tree):
        self.send_callback = send_callback
        self.users_dao = users_dao
        self.tree = tree

    def handle(self, user_id, user_message):
        logging.info("Se logro")
        # Obtener historial de eventos / mensajesç
        history = [
            (u"¡Hola! Soy el Bot de MPG. Por favor, escoge una de las opciones para ayudarte.", "bot"),
            (u"CTS", "user"),
            (u"Por favor, elija la opcion que desee consultar.", "bot"),
            (user_message, "user")
        ]
        # En Func. al mensaje escrito por el usuario (y tree)
        response_text = self.tree['say']
        possible_answers = self.tree['answers'].keys()

        tree = self.tree

        for text, author in history:
            logging.info("text : %s", text)
            logging.info("author : %s", author)
            
            if author == 'bot':
                if text == tree['say']:
                    tree == tree['answers']

            elif author == 'user':
                key = get_key_if_valid(text, tree)
                if key is not None:
                    tree = tree[key]
                    if 'say' in tree:
                        response_text = tree['say']
                    if 'answers' in tree:
                        possible_answers = tree['answers'].keys()

                    else:
                        possible_answers = None
                        
        possible_answers.sort()               
        self.send_callback(user_id, response_text, possible_answers)

def get_key_if_valid(text, dictionary):
    for key in dictionary:
        if key.lower() == text.lower():
            return key

    return None
