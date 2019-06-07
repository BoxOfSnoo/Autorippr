FROM ubuntu:18.04

RUN apt-get update && apt-get install -y curl python-virtualenv build-essential pkg-config libc6-dev libssl-dev libexpat1-dev libavcodec-dev libgl1-mesa-dev libqt4-dev zlib1g-dev 

ADD latestVersion.sh /src/
RUN chmod +x /src/latestVersion.sh
RUN /src/latestVersion.sh

RUN tar xf /src/makemkv-bin.tar.gz -C /src
RUN mkdir /src/makemkv-bin/
RUN mv /src/makemkv-bin-*/* /src/makemkv-bin/

RUN mkdir /src/makemkv-bin/tmp/
RUN echo 'accepted' > /src/makemkv-bin/tmp/eula_accepted
RUN ls /src/makemkv-bin/

RUN  sed -ie 's#DESTDIR=#DESTDIR=/build#g' /src/makemkv-bin/Makefile

RUN cd /src/makemkv-bin && make install

RUN tar xf /src/makemkv-oss.tar.gz -C /src
RUN mkdir /src/makemkv-oss/
RUN mv /src/makemkv-oss-*/* /src/makemkv-oss/

RUN cd /src/makemkv-oss && ./configure --prefix /build/usr --disable-gui && make install

CMD ["tar", "cz", "/build"]
