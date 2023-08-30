import requests

APP = {
    'client_id': 'Jp28Q~1jlXrpCS-4mazzhQ12LHVj0OVG_sp.Qbq8', # 自動生成されたもの
    'redirect_uri': 'http://localhost/', # 自分で決める。例として http://localhost:10101/authorized を使う。
    'client_secret': 'f87b34f9-a1bf-44b9-8316-28fb6201b798' # 自動生成されたもの
}

def get_refresh_token(code, app):
    data = {
        'grant_type': 'authorization_code',
        'client_id' : app['client_id'],
        'code': code,
        'redirect_uri' : app['redirect_uri'],
        'scope': 'https://graph.microsoft.com/calendars.read offline_access',
        'client_secret': app['client_secret'],
    }
    print('data: %s' % data)
    global response
    response = requests.post(
        'https://login.microsoftonline.com/common/oauth2/v2.0/token',
        data=data,
    )
    if response.status_code == 200:
        token = response.json()['refresh_token']
        return response, token
    return response, None

refresh_token = get_refresh_token(APP, 'HOGEHOGE')


def get_access_token(app, token):
    params = {
        'grant_type': 'refresh_token',
        'client_id' : app['client_id'],
        'refresh_token': token,
        'redirect_uri' : app['redirect_uri'],
        'client_secret' : app['client_secret'],
        'scope': 'https://graph.microsoft.com/calendars.read offline_access',
    }

    response = requests.post(
        'https://login.microsoftonline.com/common/oauth2/v2.0/token',
        data=params,
    )
    return response.json()['access_token']

access_token = get_access_token(APP, refresh_token)
access_token