FROM archlinux



RUN pacman -Sy

RUN pacman -S --noconfirm openssh jre11-openjdk-headless maven git

RUN useradd -m jenkins

RUN mkdir -p /home/jenkins/workspace/Better_Freezer
RUN chown jenkins /home/jenkins/workspace/
RUN chown jenkins /home/jenkins/workspace/Better_Freezer

RUN mkdir /home/jenkins.ssh

COPY ftp_cgi.sh /home/jenkins/workspace/Better_Freezer
COPY jenkins_rsa.pub /home/jenkins/.ssh/authorized_keys

RUN chown jenkins: -R /home/jenkins
RUN ssh-keygen -A


#RUN /bin/bash ftp_cgi.sh


CMD /usr/sbin/sshd -D
