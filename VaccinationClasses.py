"""Name: Angeline Dorvil
Date: 02/07/2024
Assignment Title: Vaccinations Tracking OOP Pywidgets Assignment 5- VaccinationClasses
"""

class Person():
  def __init__(self, firstname='firstname', lastname='lastname', idnumber='0000', address='US', telephone='0000000000', vac_a=0, vac_b=0, vac_c=0, symp_a1=0, symp_a2=0, symp_a3=0, symp_b1=0, symp_b2=0, symp_b3=0, symp_c1=0, symp_c2=0, symp_c3=0):
      self._name = firstname
      self._lastname = lastname
      self._idnum = idnumber
      self._address = address
      self._phonenum = telephone
    
      self._vac_a = int(vac_a)
      self._vac_b = int(vac_b)
      self._vac_c = int(vac_c)
      # Initialize symptoms for each vaccine
    
      # vac_a
      self._symp_a1 = int(symp_a1)
      self._symp_a2 = int(symp_a2)
      self._symp_a3 = int(symp_a3)
      # vac_b
      self._symp_b1 = int(symp_b1)
      self._symp_b2 = int(symp_b2)
      self._symp_b3 = int(symp_b3)
      # vac_c
      self._symp_c1 = int(symp_c1)
      self._symp_c2 = int(symp_c2)
      self._symp_c3 = int(symp_c3)

  # Getter for _name
  def get_name(self):
      return self._name

  # Setter for _name
  def set_name(self, name):
      if 0 < len(name) < 20 and not name.isdigit():
          name = name.lower().strip()
          self._name = name
      else:
          raise ValueError("Name must be a string")
  
  # Getter for _lastname
  def get_lastname(self):
      return self._lastname

  # Setter for _lastname
  def set_lastname(self, name):
      if 0 < len(name) < 20 and not name.isdigit():
          name = name.lower().strip()
          self._lastname = name
      else:
          raise ValueError("Name must be a string")

  # Getter for _id
  def get_id(self):
      return self._idnum

  # Setter for _id
  def set_id(self, id):
      if 0 < len(id) < 5 and id.isdigit():
          id = id.strip()
          self._idnum = id
      else:
          raise ValueError("ID must be 4 digits")

  # Getter for _phone
  def get_phone(self):
      return self._phonenum

  # Setter for _phone
  def set_phone(self, phone):
      if len(phone) == 10 and phone.isdigit():
          phone = phone.strip()
          self._phonenum = phone
      else:
          raise ValueError("Phone number must be 10 digits without space or hyphen")

  # Getter for _address
  def get_address(self):
      return self._address

  # Setter for _address
  def set_address(self, address):
      if len(address) > 0:
          address = address.lower().strip()
          self._address = address
      else:
          raise ValueError("Invalid address")

  def get_vac_record(self, vac='vacName'):
    if vac == 'vac_a':
      return self._vac_a
    elif vac == 'vac_b':
      return self._vac_b
    elif vac == 'vac_c':
      return self._vac_c
    else:
      return f"No such vaccine '{vac}' record exist"

  def set_vac_record(self, value, vac='vacName'):
    if vac == 'vac_a':
      if value == 0 or 1:
        self._vac_a = int(value)
    elif vac == 'vac_b': 
      if value == 0 or 1:
        self._vac_b = int(value)
    elif vac == 'vac_c': 
      if value == 0 or 1:
        self._vac_c = int(value)
    else:
      return "invalid vaccine name or invalid value"

  def get_symp_record(self, vac='vacName'):
    if vac == 'vac_a':
      return self._symp_a1, self._symp_a2, self._symp_a3
    elif vac == 'vac_b':
      return self._symp_b1, self._symp_b2, self._symp_b3
    elif vac == 'vac_c':
      return self._symp_c1, self._symp_c2, self._symp_c3
    else:
      return f"No such vaccine '{vac}' symptom record exist"

  def set_symp_record(self, vac='vacName', sympA=None, sympB=None, sympC=None):
    if vac == 'vac_a':
      if sympA == 0 or 1:
        self._symp_a1 = int(sympA)
      if sympB == 0 or 1:
        self._symp_a2 = int(sympB)
      if sympC == 0 or 1:
        self._symp_a3 = int(sympC)
    elif vac == 'vac_b':
      if sympA == 0 or 1:
        self._symp_b1 = int(sympA)
      if sympB == 0 or 1:
        self._symp_b2 = int(sympB)
      if sympC == 0 or 1:
        self._symp_b3 = int(sympC)
    elif vac == 'vac_c':
      if sympA == 0 or 1:
        self._symp_c1 = int(sympA)
      if sympB == 0 or 1:
        self._symp_c2 = int(sympB)
      if sympC == 0 or 1:
        self._symp_c3 = int(sympC)
    else:
      return "Invalid vaccine name or invalid value"
  
  def reset_attributes(self):
      # Reset vaccines and symptoms to 0
      self.set_vac_record(0, 'vac_a')
      self.set_vac_record(0, 'vac_b')
      self.set_vac_record(0, 'vac_c')
      self.set_symp_record('vac_a', sympA=0, sympB=0, sympC=0)
      self.set_symp_record('vac_b', sympA=0, sympB=0, sympC=0)
      self.set_symp_record('vac_c', sympA=0, sympB=0, sympC=0)
    

  def __str__(self):
      # Update the string representation for debugging
      return f"Person(Name: {self.name}, vac_a: {self.vac_a}, vac_b: {self.vac_b}, vac_c: {self.vac_c}, symp_a1: {self.symp_a1}, symp_a2: {self.symp_a2}, symp_a3: {self.symp_a3}, symp_b1: {self.symp_b1}, symp_b2: {self.symp_b2}, symp_b3: {self.symp_b3}, symp_c1: {self.symp_c1}, symp_c2: {self.symp_c2}, symp_c3: {self.symp_c3})"



    
class VaccSympRecord():

  def __init__(self):
      #create dictionary to store data of multiple people
      self.records_dic = {}

  def add_person_record(self, person):
      #Add a person object to the dictionary
      self.records_dic[person.get_name()] = person

  def vaccination_totals(self):
    vacATotal = vacBTotal = vacCTotal = 0
    for person in self.records_dic.values():
        vacATotal += person.get_vac_record('vac_a')
        vacBTotal += person.get_vac_record('vac_b')
        vacCTotal += person.get_vac_record('vac_c')
    return f"vac_a total is: {vacATotal}\n \nvac_b total is: {vacBTotal}\n \nvac_c total is: {vacCTotal}."

  def symptoms_totals(self):
      #tracking symptoms for vac_a
      sympAVacATotal = sympBVacATotal = sympCVacATotal = 0

      #tracking symptoms for vac_b
      sympAVacBTotal = sympBVacBTotal = sympCVacBTotal = 0

      #tracking symptoms for vac_c
      sympAVacCTotal = sympBVacCTotal = sympCVacCTotal = 0

      for person in self.records_dic.values():
        # Count the symptoms only if an individual received the vaccine
        if person.get_vac_record('vac_a') == 1:
          symp_a1, symp_a2, symp_a3 = person.get_symp_record('vac_a')
          sympAVacATotal += symp_a1
          sympBVacATotal += symp_a2
          sympCVacATotal += symp_a3
          
        if person.get_vac_record('vac_b') == 1:
          symp_b1, symp_b2, symp_b3 = person.get_symp_record('vac_b')
          sympAVacBTotal += symp_b1
          sympBVacBTotal += symp_b2
          sympCVacBTotal += symp_b3
          
        if person.get_vac_record('vac_c') == 1:
          symp_c1, symp_c2, symp_c3 = person.get_symp_record('vac_c')
          sympAVacCTotal += symp_c1
          sympBVacCTotal += symp_c2
          sympCVacCTotal += symp_c3
          
      record = (f'  vac_a symptoms record: \n'
                    f'   symp_a : {sympAVacATotal}\n'
                    f'   symp_b : {sympBVacATotal}\n'
                    f'   symp_c : {sympCVacATotal}\n'
                f' \n'
                f'  vac_b symptoms record: \n'
                    f'   symp_a : {sympAVacBTotal}\n'
                    f'   symp_b : {sympBVacBTotal}\n'
                    f'   symp_c : {sympCVacBTotal}\n'
                f' \n'
                f'  vac_c symptoms record: \n'
                    f'   symp_a : {sympAVacCTotal}\n'
                    f'   symp_b : {sympBVacCTotal}\n'
                    f'   symp_c : {sympCVacCTotal}\n')

      return record

  def __str__(self):
      # String representation for debugging
      return f"VaccSympRecord({self.records_dic})" 