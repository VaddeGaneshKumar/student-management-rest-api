import requests

# 1. నువ్వు డేటా అడగాల్సిన API లింక్
url = 'http://127.0.0.1:8000/api/students/'

# 2. ఇక్కడే ఉంది మ్యాజిక్! నీ VIP పాస్ (Token) ని సెక్యూరిటీ గార్డ్ కి పంపిస్తున్నాం.
# (కింద <నీ_టోకెన్_ఇక్కడ_పెట్టు> అన్న చోట, అడ్మిన్ ప్యానెల్ లో వచ్చిన ఆ 40 అక్షరాల కోడ్ ని పేస్ట్ చెయ్)
headers = {
    'Authorization': 'Token 6d6a887c619866c8de1f1e6e9f2ad3f1b9d582ae' 
}

# 3. ఇప్పుడు డేటా అడుగుతున్నాం (GET Request)
response = requests.get(url, headers=headers)

# 4. వచ్చిన డేటాని ప్రింట్ చేస్తున్నాం
print("Status Code:", response.status_code)
print("Data:", response.json())