FROM oraclelinux:10

RUN dnf update -y && \
  dnf groupinstall "Development Tools" -y && \
  dnf install -y cmake python3 python3-pip && \
  dnf clean all

RUN pip3 install conan

# Create a non-root user for security (good practice for Jenkins)
RUN useradd -m jenkins
USER jenkins
WORKDIR /home/jenkins

# Initialize Conan profile for the 'jenkins' user
RUN conan profile detect --force

# Set the entrypoint to bash by default
CMD ["/bin/bash"]
