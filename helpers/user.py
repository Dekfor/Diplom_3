import requests, random, string

BASE_URL = 'https://qa-stellarburgers.education-services.ru'


def generate_user_data():
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    return {
        'email': f'test_{rand}@yandex.ru',
        'password': 'password1447Test',
        'name': f'user_{rand}'
    }


def create_user():
    payload = generate_user_data()

    response = requests.post(
        f'{BASE_URL}/api/auth/register',
        json=payload
    )

    assert response.status_code == 200

    response_data = response.json()
    access_token = response_data.get('accessToken')

    return payload, access_token


def delete_user(token):

    if token:
        requests.delete(
            f'{BASE_URL}/api/auth/user',
            headers={'Authorization': token}
        )