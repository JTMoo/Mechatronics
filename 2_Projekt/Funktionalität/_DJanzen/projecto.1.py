import requests




from sklearn import svm
import matplotlib.pyplot as plt
x = [[0,0],[1,1]]
y = [0,1]
clf = svm.SVC()
clf.fit(x,y)
y_pred = clf.predict([[2.,2.]])

plt.plot(x, y, y_pred)
plt.show()




url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process the data as needed
else:
    print('Error: Failed to retrieve data from API')






url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'London,UK',
    'appid': 'your_api_key_here'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Process the data as needed
else:
    print('Error: Failed to retrieve data from API')
