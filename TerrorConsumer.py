#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
 

endfile = open('TerrorDBoutput.txt','w') 
# To write received messages into this file

consumer = KafkaConsumer('topicname',
                         bootstrap_servers=['quickstart.cloudera:9092'])
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
        # prints out topic, partition, offset, key and value of message
        # partition is always zero
        # there is no key set
    endfile.write(message.value)
    
endfile.close()

