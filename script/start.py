from docker_flask.docker.docker_connection import DockerConnection

nb_cpu = 1

dpc = DockerConnection()  # docker platform connection
dpc.start(cpu_nb=nb_cpu)  # start container
#dpc.stop_all()  # stop all container
#dpc.remove_all()  # stop all container
