#!/bin/sh
set -eu

envsubst < /etc/alertmanager/alertmanager.template.yml \
  > /tmp/alertmanager.yml

exec /bin/alertmanager \
  --config.file=/tmp/alertmanager.yml