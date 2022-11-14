import requests


class HttpManager:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result = requests.get(url,
                              headers=HttpManager.headers,
                              cookies=HttpManager.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url,
                               json=body,
                               headers=HttpManager.headers,
                               cookies=HttpManager.cookie)
        return result

    @staticmethod
    def delete(url):
        result = requests.delete(url,
                                 headers=HttpManager.headers,
                                 cookies=HttpManager.cookie)
        return result
