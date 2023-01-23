from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

dob = date(2004, 12, 31)
age = calculate_age(dob)
print(age)
18

import json
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

class User:    

    def __init__(self, name, uid, password, dob, loc): # classof not included otherwise will not be defined
        self._name = name    # variables with self prefix become part of the object, 
        self._uid = uid
        self.set_password(password)
        self._dob = dob
        self._classOf = str (self._dob.year + 18) # classOf, dob + 18 years of school gives graduation class
        self._loc = loc # part of our project

    @property # getter
    def classOf(self):
        return self._classOf

    @property # getter for location
    def classOf(self):
        return self._loc

    # a setter function
    @classOf.setter 
    def classOf(self, classOf):
        self._classOf = classOf


    @property
    def name(self):
        return self._name
    
    # setter
    @name.setter
    def name(self, name):
        self._name = name
    
    # getter
    @property
    def uid(self):
        return self._uid
    
    # setter
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, uid):
        return self._uid == uid
    
    # dob returned as string to manage the output
    @property
    def dob(self):
        dob_string = self._dob.strftime('%m-%d-%Y')
        return dob_string
    
    # setter
    @dob.setter
    def dob(self, dob):
        self._dob = dob
        
    # returns current age
    @property
    def age(self):
        today = date.today()
        return today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
    
    # dictionary is customized, removing password for security purposes
    @property
    def dictionary(self):
        dict = {
            "name" : self.name,
            "uid" : self.uid,
            "dob" : self.dob,
            "age" : self.age,
            "classOf" : self.classOf, 
            "location" : self._loc 
        }
        return dict
    
    # updates the password
    def set_password(self, password):
        """Create a hashed password."""
        self._password = generate_password_hash(password, method='sha256')

    # check password parameter versus stored/encrypted password
    def is_password(self, password):
        """Check against hashed password."""
        result = check_password_hash(self._password, password)
        return result
    
    # json allows for backend and frontend interaction, str makes it readable
    def __str__(self):
        return json.dumps(self.dictionary)
    
    # output command to recreate the object, uses attribute directly
    def __repr__(self):
        return f'User(name={self._name}, uid={self._uid}, password={self._password},dob={self._dob}, classOf={self._classOf}, location={self._loc})'

if __name__ == "__main__":
    u1 = User(name='Thomas Edison', uid='toby', password='123toby', dob=date(1847, 2, 11), location='San Diego' )# used help from team and example here
    print("Raw Variables of object:\n", vars(u1), "\n") 
    print("Raw Attributes and Methods of object:\n", dir(u1), "\n")
    print("Representation to Re-Create the object:\n", repr(u1), "\n") 