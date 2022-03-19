from docker_flask.client.base import BaseClient


def check_all_docker_up(nb_docker, display=True):
    not_up = []
    all_up = True
    base_client = BaseClient()
    for index in range(1, nb_docker + 1):
        response = base_client.get(url_last_digit=index)
        is_up = True if response.text == "IM UP!" else False
        if display:
            if is_up:
                print(f'docker {index} is up!')
            else:
                print(f'docker {index} is NOT up!')
        if not is_up:
            not_up.append(index)
            all_up = False
    return all_up, not_up
