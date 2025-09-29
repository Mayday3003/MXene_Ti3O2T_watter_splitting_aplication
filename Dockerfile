FROM mambaorg/micromamba:latest

COPY environment.yml /tmp/environment.yml
RUN micromamba create -n matbook -f /tmp/environment.yml && \
    micromamba clean -a -y

ENV PATH /opt/conda/envs/matbook/bin:$PATH
WORKDIR /home/jovyan

CMD ["jupyter", "lab"]
