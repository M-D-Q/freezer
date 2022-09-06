FROM python

RUN mkdir /betterfreezer
RUN apt update
RUN apt install python3-pip --yes
RUN pip install --upgrade pip
RUN curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash
RUN apt update
RUN apt install libmariadb3 --yes
RUN apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 --yes
RUN pip install pyaudio
RUN pip install mariadb
RUN pip install pytube

#RUN python /betterfreezer/server.py
