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
$ES_HOME/bin/elasticsearch "$@"
