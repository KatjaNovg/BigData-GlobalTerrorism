#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time
from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient('quickstart.cloudera:9092')
producer = SimpleProducer(kafka, async = True,
                          batch_send_every_n = 1000, batch_send_every_t = 10)
# Simple producer that sends messages when 1000 messages are collected 
# or every 10 seconds

file = open('TerrorDBinput.txt', 'r') 

def simplemessage():
    
    timewait = 0
    for i in file:
        if timewait > 5000: # every 5000 lines
            print("Now wait...")
            time.sleep(30) # wait for 30 seconds to simulate tream
            timewait = 0
        print(i)
        producer.send_messages('topicname', i)
        
        timewait = timewait + 1

producer.send_messages("topicname",'Finished!') # Printed out when stream is done
    
simplemessage()

