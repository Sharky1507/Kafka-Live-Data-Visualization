from kafka import KafkaProducer
import time
import psutil
topic_name = '<write your topic name here>'
kafka_server = '<write your server here>'
#setup server
producer = KafkaProducer(bootstrap_servers=kafka_server)
for i in range(1000):
     time.sleep(0.5)
     cpu_percentage = int(psutil.cpu_percent())
     print(cpu_percentage)
     # producer.send expects input in bytes
     cpu_percentage_bytes = cpu_percentage.to_bytes(2, 'big')
     producer.send(topic_name, cpu_percentage_bytes)
