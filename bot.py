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
        self.users_dao.add_user_event(user_id, 'user', user_message)
        history = self.users_dao.get_user_events(user_id)

        # history = [
        #     (u"¡Hola! Soy el Bot de MPG. Por favor, escoge una de las opciones para ayudarte.", "bot"),
        #     (u"CTS", "user"),
        #     (u"Por favor, elija la opcion que desee consultar.", "bot"),
        #     (user_message, "user")
        # ]
        # En Func. al mensaje escrito por el usuario (y tree)
        response_text = self.tree['say']
        possible_answers = self.tree['answers'].keys()
        possible_answers.sort()


        tree = self.tree

        for text, author in history:
            logging.info("text : %s", text)
            logging.info("author : %s", author)
            
            if author == "bot":
                if 'say' in tree && text == tree['say']:
                    tree == tree['answers']

            elif author == "user":
                key = get_key_if_valid(text, tree)
                if key is not None:
                    tree = tree[key]
                    if 'say' in tree:
                        response_text = tree['say']
                    if 'answers' in tree:
                        possible_answers = tree['answers'].keys()
                        possible_answers.sort()
                    else:
                        possible_answers = None

        self.send_callback(user_id, response_text, possible_answers)
        self.users_dao.add_user_event(user_id, 'bot', response_text)

def get_key_if_valid(text, dictionary):
    for key in dictionary:
        if key.lower() == text.lower():
            return key

    return None
