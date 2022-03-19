import docker

from docker_flask.docker.conf import BASE_CONTAINER_ADDRESS, EXPOSE_PORT, DOCKER_IMAGE


class DockerConnection:
    def __init__(self):
        self.client = docker.from_env()
        self.container_list = []
        self.base_address = BASE_CONTAINER_ADDRESS
        self.expose_port = EXPOSE_PORT
        self.docker_image_name = DOCKER_IMAGE

    def start(self, cpu_nb=1):
        for index in range(1, cpu_nb + 1):
            container = self.client.containers.run(self.docker_image_name,
                                                   ports={
                                                       '8180/tcp': (f'{self.base_address}.{index}', self.expose_port)},
                                                   detach=True)
            self.container_list.append(container)

    def stop_all_container(self):
        for container in self.container_list:
            container.stop()

    def remove_all_container(self):
        for container in self.container_list:
            container.remove()

    def stop_and_remove_all_flask_docker_container(self):
        for container in self.client.containers.list():
            if self.client.containers.list()[0].image.tags[0] == 'docker_flask:0.0.1':
                container.stop()
                container.remove()
