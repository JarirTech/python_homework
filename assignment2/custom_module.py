

secret = "shazam!"

def set_secret(new_secret):
   global secret
   secret = new_secret
   #print(new_secret)
   return new_secret
#set_secret("p@ssword@")