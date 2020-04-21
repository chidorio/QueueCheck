import pyrebase
#firebase config
config = {
  'apiKey': "AIzaSyD351sZwVgyMRu-7SwqzEoOHo9VEIoHFtw",
  'authDomain': "queuecheck-f1526.firebaseapp.com",
  'databaseURL': "https://queuecheck-f1526.firebaseio.com",
  'projectId': "queuecheck-f1526",
  'storageBucket': "queuecheck-f1526.appspot.com",
  'messagingSenderId': "248340142836",
  'appId': "1:248340142836:web:14ad5b6510198d11429ca1"
}
firebase = pyrebase.initialize_app(config)
# firebase auth
auth_firebase = firebase.auth()
# firebase database
database = firebase.database()
