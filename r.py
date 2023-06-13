import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'httpMethod': 'POST',
    'path': '/api/resource/v2/camera/search',
    'headers': {},
    'query': {},
    'parameter': {},
    'body': {
        'name': '神坛村',
        'regionIndexCodes': [
            '99069dab-e923-46df-b154-a5f4ce6a2ad1',
        ],
        'isSubRegion': True,
        'pageNo': 1,
        'pageSize': 20,
        'authCodes': [
            'view',
        ],
        'orderBy': 'name',
        'orderType': 'desc',
    },
    'contentType': 'application/json;charset=UTF-8',
    'mock': False,
    'appKey': '24664304',
    'appSecret': 'j0G8fSnucFCj43AQrvz7',
}

response = requests.post('https://122.226.221.122:8443/artemis-web/debug', headers=headers, json=json_data, verify=False)
print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"httpMethod":"POST","path":"/api/resource/v2/camera/search","headers":{},"query":{},"parameter":{},"body":{"name":"神坛村","regionIndexCodes":["99069dab-e923-46df-b154-a5f4ce6a2ad1"],"isSubRegion":true,"pageNo":1,"pageSize":20,"authCodes":["view"],"orderBy":"name","orderType":"desc"},"contentType":"application/json;charset=UTF-8","mock":false,"appKey":"24664304","appSecret":"j0G8fSnucFCj43AQrvz7"}'.encode()
#response = requests.post('https://122.226.221.122:8443/artemis-web/debug', headers=headers, data=data, verify=False)