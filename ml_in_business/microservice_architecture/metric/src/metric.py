import pika
import json
 
try:
    # Создаём подключение к серверу на локальном хосте
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
   
    # Объявляем очередь y_true
    channel.queue_declare(queue='y_true')
    # Объявляем очередь y_pred
    channel.queue_declare(queue='y_pred')
 
    # Создаём функцию callback для обработки данных из очереди
    def callback(ch, method, properties, body):
        answer_string = f'Из очереди {method.routing_key} получено значение {json.loads(body)}'
        with open('./logs/labels_log.txt', 'a') as log:
            log.write(answer_string +'\n')
 
    # Извлекаем сообщение из очереди y_true
    channel.basic_consume(
        queue='y_true',
        on_message_callback=callback,
        auto_ack=True
    )
    # Извлекаем сообщение из очереди y_pred
    channel.basic_consume(
        queue='y_pred',
        on_message_callback=callback,
        auto_ack=True
    )
 
    # Запускаем режим ожидания прихода сообщений
    print('...Ожидание сообщений, для выхода нажмите CTRL+C')
    channel.start_consuming()
except:
    print('Не удалось подключиться к очереди')