from google.cloud import storage
from firebase import firebase
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="google-services.json"
firebase = firebase.FirebaseApplication('https://iot1-379aa.firebaseio.com/')
client = storage.Client()
bucket = client.get_bucket('gs://iot1-379aa.appspot.com')
# posting to firebase storage
imageBlob = bucket.blob("/")
# imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
imagePath = "image1.jpg"
imageBlob = bucket.blob("image1.jpg")
imageBlob.upload_from_filename(imagePath)
