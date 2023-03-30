import requests


def test_get_request():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    assert response.json()['userId'] == 1
    assert response.json()['id'] == 1


def test_list_get_request():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    data = response.json()
    i = 1
    j = 1
    for element in data:
        assert element['userId'] == i
        assert element['id'] == j
        if j % 10 == 0:
            i += 1
        j += 1


def test_post_request():
    test_object = {'postTestKey': 'postTestValue'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=test_object)
    assert response.status_code == 201
    assert response.json()['id'] == 101
    assert response.json()['postTestKey'] == 'postTestValue'


def test_put_request():
    test_object = {'putTestKey': 'putTestValue'}
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=test_object)
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['putTestKey'] == 'putTestValue'


def test_delete_request():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    assert str(response.json()) == "{}"


def test_head_request():
    response = requests.head('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200


def test_patch_request():
    test_object = {'patchTestKey': 'patchTestValue'}
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=test_object)
    assert response.status_code == 200
    assert response.json()['userId'] == 1
    assert response.json()['id'] == 1
    assert response.json()['patchTestKey'] == 'patchTestValue'


def test_options_request():
    response = requests.options('https://www.example.com')
    assert response.status_code == 200
    assert response.headers['Allow'] == 'OPTIONS, GET, HEAD, POST'


def test_redirection_handling():
    url = "http://httpbin.org/redirect-to?url=https://www.example.com"
    response = requests.get(url)
    print(response.url)
    assert response.url == "https://www.example.com"


def test_cookies_handling():
    session = requests.Session()
    session.cookies.set('testCookie', 'testCookieValue')
    response = session.get('http://httpbin.org/cookies')
    assert response.json()['cookies']['testCookie'] == 'testCookieValue'


def test_authentication_with_correct_credentials():
    username = 'testUsername'
    password = 'testPassword'
    response = requests.get(f'http://httpbin.org/basic-auth/{username}/{password}', auth=(username, password))
    assert response.status_code == 200
    assert response.json()['authenticated']
    assert response.json()['user'] == f'{username}'


def test_authentication_with_wrong_credentials():
    username = 'correctUsername'
    password = 'correctPassword'
    response = requests.get(f'http://httpbin.org/basic-auth/{username}/{password}', auth=('wrongUsername', 'wrongPassword'))
    assert response.status_code == 401


def main():
    test_get_request()
    test_list_get_request()
    test_post_request()
    test_put_request()
    test_delete_request()
    test_head_request()
    test_patch_request()
    test_options_request()
    test_redirection_handling()
    test_cookies_handling()
    test_authentication_with_correct_credentials()
    test_authentication_with_wrong_credentials()


if __name__ == "__main__":
    main()
