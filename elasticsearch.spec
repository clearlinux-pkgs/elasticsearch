Name     : elasticsearch
Version  : 5.4.0
Release  : 5
URL      : https://github.com/elastic/elasticsearch/
Source0  : https://github.com/elastic/elasticsearch/archive/v5.4.0.tar.gz
Source1  : init.gradle
Source2  : elasticsearch-script.sh
Source3  : elasticsearch.tmpfiles
Patch0   : 0001-Change-repo-config-to-LOCAL.patch
Patch1   : 0002-Change-config-path-default.patch
Patch2   : 0003-Make-elasticsearch.service-use-the-elasticsearch-scr.patch
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires: gradle
BuildRequires: elasticsearch-dep
BuildRequires: openjdk-dev
BuildRequires: ca-certs
BuildRequires: procps-ng
BuildRequires: rpm-common

%description
You can add .gradle init scripts to this directory. Each one is executed at the start of the build.

%prep
%setup -q -n elasticsearch-5.4.0
%patch0 -p1
%patch1 -p1
%patch2 -p1

mkdir -p /builddir/.m2
cp -R /usr/share/elasticsearch/.m2/* /builddir/.m2

%build
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/
gradle --offline assemble --init-script %{SOURCE1}

%install
cp distribution/rpm/build/distributions/elasticsearch-5.4.0-SNAPSHOT.rpm %{buildroot}
pushd %{buildroot}
mkdir -p %{buildroot}/usr/share/defaults/elasticsearch
mkdir -p %{buildroot}/usr/share/elasticsearch/plugins
rpm2cpio elasticsearch-5.4.0-SNAPSHOT.rpm | cpio -imdv
cat %{SOURCE3} >> %{buildroot}/usr/lib/tmpfiles.d/elasticsearch.conf
#Copy config files to default directory
cp -R %{buildroot}/etc/elasticsearch/* %{buildroot}/usr/share/defaults/elasticsearch
chmod 755 -R %{buildroot}/usr/share/defaults/elasticsearch
#Replace elasticsearch binary with a script that will provide the stateless funcitonality
cp %{SOURCE2} %{buildroot}/usr/share/elasticsearch/bin/elasticsearch-script
chmod 755 %{buildroot}/usr/share/elasticsearch/bin/elasticsearch-script
rm elasticsearch-5.4.0-SNAPSHOT.rpm
popd

%files
%defattr(-,root,root,-)
/usr/lib/sysctl.d/elasticsearch.conf
/usr/lib/systemd/system/elasticsearch.service
/usr/lib/tmpfiles.d/elasticsearch.conf
/usr/share/defaults/elasticsearch/elasticsearch.yml
/usr/share/defaults/elasticsearch/jvm.options
/usr/share/defaults/elasticsearch/log4j2.properties
/usr/share/defaults/elasticsearch/scripts/
/usr/share/elasticsearch/LICENSE.txt
/usr/share/elasticsearch/NOTICE.txt
/usr/share/elasticsearch/README.textile
/usr/share/elasticsearch/bin/elasticsearch
/usr/share/elasticsearch/bin/elasticsearch-keystore
/usr/share/elasticsearch/bin/elasticsearch-plugin
/usr/share/elasticsearch/bin/elasticsearch-script
/usr/share/elasticsearch/bin/elasticsearch-systemd-pre-exec
/usr/share/elasticsearch/bin/elasticsearch-translog
/usr/share/elasticsearch/bin/elasticsearch.in.sh
/usr/share/elasticsearch/lib/HdrHistogram-2.1.9.jar
/usr/share/elasticsearch/lib/elasticsearch-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/lib/hppc-0.7.1.jar
/usr/share/elasticsearch/lib/jackson-core-2.8.6.jar
/usr/share/elasticsearch/lib/jackson-dataformat-cbor-2.8.6.jar
/usr/share/elasticsearch/lib/jackson-dataformat-smile-2.8.6.jar
/usr/share/elasticsearch/lib/jackson-dataformat-yaml-2.8.6.jar
/usr/share/elasticsearch/lib/java-version-checker-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/lib/jna-4.4.0.jar
/usr/share/elasticsearch/lib/joda-time-2.9.5.jar
/usr/share/elasticsearch/lib/jopt-simple-5.0.2.jar
/usr/share/elasticsearch/lib/jts-1.13.jar
/usr/share/elasticsearch/lib/log4j-1.2-api-2.8.2.jar
/usr/share/elasticsearch/lib/log4j-api-2.8.2.jar
/usr/share/elasticsearch/lib/log4j-core-2.8.2.jar
/usr/share/elasticsearch/lib/lucene-analyzers-common-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-backward-codecs-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-core-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-grouping-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-highlighter-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-join-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-memory-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-misc-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-queries-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-queryparser-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-sandbox-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-spatial-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-spatial-extras-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-spatial3d-6.5.0.jar
/usr/share/elasticsearch/lib/lucene-suggest-6.5.0.jar
/usr/share/elasticsearch/lib/securesm-1.1.jar
/usr/share/elasticsearch/lib/snakeyaml-1.15.jar
/usr/share/elasticsearch/lib/spatial4j-0.6.jar
/usr/share/elasticsearch/lib/t-digest-3.0.jar
/usr/share/elasticsearch/modules/aggs-matrix-stats/aggs-matrix-stats-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/aggs-matrix-stats/plugin-descriptor.properties
/usr/share/elasticsearch/modules/ingest-common/ingest-common-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/ingest-common/jcodings-1.0.12.jar
/usr/share/elasticsearch/modules/ingest-common/joni-2.1.6.jar
/usr/share/elasticsearch/modules/ingest-common/plugin-descriptor.properties
/usr/share/elasticsearch/modules/lang-expression/antlr4-runtime-4.5.1-1.jar
/usr/share/elasticsearch/modules/lang-expression/asm-5.0.4.jar
/usr/share/elasticsearch/modules/lang-expression/asm-commons-5.0.4.jar
/usr/share/elasticsearch/modules/lang-expression/asm-tree-5.0.4.jar
/usr/share/elasticsearch/modules/lang-expression/lang-expression-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/lang-expression/lucene-expressions-6.5.0.jar
/usr/share/elasticsearch/modules/lang-expression/plugin-descriptor.properties
/usr/share/elasticsearch/modules/lang-expression/plugin-security.policy
/usr/share/elasticsearch/modules/lang-groovy/groovy-2.4.6-indy.jar
/usr/share/elasticsearch/modules/lang-groovy/lang-groovy-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/lang-groovy/plugin-descriptor.properties
/usr/share/elasticsearch/modules/lang-groovy/plugin-security.policy
/usr/share/elasticsearch/modules/lang-mustache/compiler-0.9.3.jar
/usr/share/elasticsearch/modules/lang-mustache/lang-mustache-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/lang-mustache/plugin-descriptor.properties
/usr/share/elasticsearch/modules/lang-mustache/plugin-security.policy
/usr/share/elasticsearch/modules/lang-painless/antlr4-runtime-4.5.1-1.jar
/usr/share/elasticsearch/modules/lang-painless/asm-debug-all-5.1.jar
/usr/share/elasticsearch/modules/lang-painless/lang-painless-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/lang-painless/plugin-descriptor.properties
/usr/share/elasticsearch/modules/lang-painless/plugin-security.policy
/usr/share/elasticsearch/modules/percolator/percolator-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/percolator/plugin-descriptor.properties
/usr/share/elasticsearch/modules/reindex/commons-codec-1.10.jar
/usr/share/elasticsearch/modules/reindex/commons-logging-1.1.3.jar
/usr/share/elasticsearch/modules/reindex/httpasyncclient-4.1.2.jar
/usr/share/elasticsearch/modules/reindex/httpclient-4.5.2.jar
/usr/share/elasticsearch/modules/reindex/httpcore-4.4.5.jar
/usr/share/elasticsearch/modules/reindex/httpcore-nio-4.4.5.jar
/usr/share/elasticsearch/modules/reindex/plugin-descriptor.properties
/usr/share/elasticsearch/modules/reindex/reindex-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/reindex/rest-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/transport-netty3/netty-3.10.6.Final.jar
/usr/share/elasticsearch/modules/transport-netty3/plugin-descriptor.properties
/usr/share/elasticsearch/modules/transport-netty3/plugin-security.policy
/usr/share/elasticsearch/modules/transport-netty3/transport-netty3-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/modules/transport-netty4/netty-buffer-4.1.9.Final.jar
/usr/share/elasticsearch/modules/transport-netty4/netty-codec-4.1.9.Final.jar
/usr/share/elasticsearch/modules/transport-netty4/netty-codec-http-4.1.9.Final.jar
/usr/share/elasticsearch/modules/transport-netty4/netty-common-4.1.9.Final.jar
/usr/share/elasticsearch/modules/transport-netty4/netty-handler-4.1.9.Final.jar
/usr/share/elasticsearch/modules/transport-netty4/netty-resolver-4.1.9.Final.jar
/usr/share/elasticsearch/modules/transport-netty4/netty-transport-4.1.9.Final.jar
/usr/share/elasticsearch/modules/transport-netty4/plugin-descriptor.properties
/usr/share/elasticsearch/modules/transport-netty4/plugin-security.policy
/usr/share/elasticsearch/modules/transport-netty4/transport-netty4-5.4.0-SNAPSHOT.jar
/usr/share/elasticsearch/plugins
