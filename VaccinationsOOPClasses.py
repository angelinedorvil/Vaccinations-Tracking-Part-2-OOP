"""Name: Angeline Dorvil
Date: 01/10/2024
Assignment Title: Vaccinations Tracking OOP Assignment - classes
"""

class Person():

  def __init__(self, name, vac_a, vac_b, vac_c):
    self.name = name
    self.vac_a = int(vac_a)
    self.vac_b = int(vac_b)
    self.vac_c = int(vac_c)

  def vaccine_a_update(self, vac_a):
      self.vac_a = vac_a

  def vaccine_b_update(self, vac_b):
      self.vac_b = vac_b

  def vaccine_c_update(self, vac_c):
      self.vac_c = vac_c

  def get_vac_record(self):
    record = (f'   Name: {self.name}\n'
              f'   vac_a record: {self.vac_a}\n'
              f'   vac_b record: {self.vac_b}\n'
              f'   vac_c record: {self.vac_c}\n')
    return record


  def __str__(self): #string representation of objects for debugging and logging
    return f"Person(Name: {self.name}, vac_a: {self.vac_a}, vac_b: {self.vac_b}, vac_c: {self.vac_c})"


class VaccinationRecord():

  def __init__(self):
    #create dictionary to store data of multiple people
    self.records_dic = {}

  def add_person_record(self, person):
    #Add a person object to the dictionary
    self.records_dic[person.name] = person

  def get_vaccination_status(self, name):
    #get vaccination status for a specific person 
    if name in self.records_dic:
      return self.records_dic[name].get_vac_record()
    else:
      return f"Individual '{name}' has no records."

  def vaccination_totals(self):
    vacATotal = 0
    vacBTotal = 0
    vacCTotal = 0
    for record in self.records_dic:
      vacATotal += int(self.records_dic[record].vac_a)
      vacBTotal += int(self.records_dic[record].vac_b)
      vacCTotal += int(self.records_dic[record].vac_c)

    return f" vac_a total is: {vacATotal}\n vac_b total is: {vacBTotal}\n vac_c total is: {vacCTotal}."


  def __str__(self):
    # String representation for debugging
    return f"VaccinationRecord({self.records_dic})" 