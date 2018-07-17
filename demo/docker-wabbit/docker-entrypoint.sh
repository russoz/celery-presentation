#!/bin/bash

gosu rabbitmq rabbitmqctl add_user admin admin
gosu rabbitmq rabbitmqctl set_user_tags admin administrator
gosu rabbitmq rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

