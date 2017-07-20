#!/bin/sh

# Source system prefs
if [ -f /etc/java/elasticsearch.conf ] ; then
  . /etc/java/elasticsearch.conf
fi

# Source user prefs
if [ -f $HOME/.elasticsearchrc ] ; then
  . $HOME/.elasticsearchrc
fi

export ES_HOME="${ES_HOME:-/usr/share/elasticsearch}"
if [ -d /etc/elasticsearch -a "$(ls -A /etc/elasticsearch)" ] ; then
    echo "Config directory: /etc/elasticsearch"
    $ES_HOME/bin/elasticsearch -Epath.conf=/etc/elasticsearch "$@"
else
    echo "Config directory: /usr/share/defaults/elasticsearch"
    $ES_HOME/bin/elasticsearch "$@"
fi
