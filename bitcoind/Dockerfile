# Dockerfile
FROM blockstream/bitcoind:latest

# Copy custom bitcoin.conf into the container
COPY bitcoin.conf /etc/bitcoin/bitcoin.conf

# Optionally, you can expose ports or define volumes if needed
EXPOSE 8332 8333
VOLUME ["/root/.bitcoin"]

# Command to run `bitcoind` when the container starts
CMD ["bitcoind", "-conf=/root/.bitcoin/bitcoin.conf"]


# bitcoind/Dockerfile
# FROM ubuntu:20.04

# RUN apt-get update && \
#     apt-get install -y software-properties-common && \
#     add-apt-repository ppa:bitcoin/bitcoin && \
#     apt-get update && \
#     apt-get install -y bitcoind && \
#     rm -rf /var/lib/apt/lists/*

# RUN mkdir /root/.bitcoin
# COPY bitcoin.conf /root/.bitcoin/bitcoin.conf

# EXPOSE 8332 8333
