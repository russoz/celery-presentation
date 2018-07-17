#!/bin/bash

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install rabbitmq-server
sudo -u rabbitmq rabbitmqctl add_user admin admin
sudo -u rabbitmq rabbitmqctl set_user_tags admin administrator
sudo -u rabbitmq rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
sudo -u rabbitmq rabbitmqctl set_vm_memory_high_watermark 0.8

