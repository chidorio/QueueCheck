import pyrebase
#firebase config
config = {
  'apiKey': "AIzaSyDevQplt3baNyCJctkUEua-kfBql7btMJY",
  'authDomain': "se-2s-70ca2.firebaseapp.com",
  'databaseURL': "https://se-2s-70ca2.firebaseio.com",
  'projectId': "se-2s-70ca2",
  'storageBucket': "se-2s-70ca2.appspot.com",
  'messagingSenderId': "239192608253",
  'appId': "1:239192608253:web:5449a7272efa3fdd6d5d94"
}
firebase = pyrebase.initialize_app(config)
# firebase auth
auth_firebase = firebase.auth()
# firebase database
database = firebase.database()
