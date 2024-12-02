from config import FIELD_DEFINITIONS, MESSAGES_CONFIG, JSON_TEMPLATE, EXAMPLES

def create_messages(texto_entrada):
    """
    Crea la lista de mensajes para la API de OpenAI
    """
    # Formateamos las definiciones de campos como texto
    field_definitions_text = '. '.join([
        f"'{key}': '{value}'" 
        for key, value in FIELD_DEFINITIONS.items()
    ])

    # Creamos el mensaje del usuario con el template
    user_message = MESSAGES_CONFIG["template"]["content"].format(
        json_template=JSON_TEMPLATE,
        field_definitions=field_definitions_text,
        input_example=EXAMPLES,
        input_text=texto_entrada
    )

    # Retornamos la lista completa de mensajes
    return [
        MESSAGES_CONFIG["system"],
        {"role": "user", "content": user_message}
    ]
