FROM continuumio/miniconda3
ENV LANG C.UTF-8

ADD ./ /src/

SHELL ["/bin/bash", "-c"]

# Create a wheel of my project
RUN conda create -n myenv python=3.7 wheel
RUN source activate myenv && cd /src && python setup.py bdist_wheel

FROM continuumio/miniconda3
ENV LANG C.UTF-8


SHELL ["/bin/bash", "-c"]

COPY --from=0 /src/dist/*.whl /opt/docker_flask/


# Install wheel of my project into container
RUN conda create -n myenv python=3.7
RUN source activate myenv && conda install flask
RUN source activate myenv && pip install --no-cache-dir /opt/docker_flask/docker_flask-0.0.1-py3-none-any.whl

# open docker port
EXPOSE 8180/tcp

# define entry point
COPY docker/main.py src/main.py
ENTRYPOINT ["/opt/conda/envs/myenv/bin/python", "src/main.py"]
