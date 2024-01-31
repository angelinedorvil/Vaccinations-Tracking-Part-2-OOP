"""Name: Angeline Dorvil
Date: 01/28/2024
Assignment Title: Vaccinations Tracking OOP Pygame Assignment 3- Classes
"""

class Person():
  def __init__(self, firstname, lastname, idnumber, address, telephone, vac_a, vac_b, vac_c, symp_a1, symp_a2, symp_a3, symp_b1, symp_b2, symp_b3, symp_c1, symp_c2, symp_c3):
      self.name = firstname
      self.lastname = lastname
      self.idnum = idnumber
      self.address = address
      self.phonenum = telephone
    
      self.vac_a = int(vac_a)
      self.vac_b = int(vac_b)
      self.vac_c = int(vac_c)
      # Initialize symptoms for each vaccine
      # vac_a
      self.symp_a1 = int(symp_a1)
      self.symp_a2 = int(symp_a2)
      self.symp_a3 = int(symp_a3)
      # vac_b
      self.symp_b1 = int(symp_b1)
      self.symp_b2 = int(symp_b2)
      self.symp_b3 = int(symp_b3)
      # vac_c
      self.symp_c1 = int(symp_c1)
      self.symp_c2 = int(symp_c2)
      self.symp_c3 = int(symp_c3)

  def reset_attributes(self):
      # Reset vaccines and symptoms to 0
      self.vac_a = self.vac_b = self.vac_c = 0
      self.symp_a1 = self.symp_a2 = self.symp_a3 = 0
      self.symp_b1 = self.symp_b2 = self.symp_b3 = 0
      self.symp_c1 = self.symp_c2 = self.symp_c3 = 0

  def __str__(self):
      # Update the string representation to include new attributes
      return f"Person(Name: {self.name}, vac_a: {self.vac_a}, vac_b: {self.vac_b}, vac_c: {self.vac_c}, symp_a1: {self.symp_a1}, symp_a2: {self.symp_a2}, symp_a3: {self.symp_a3}, symp_b1: {self.symp_b1}, symp_b2: {self.symp_b2}, symp_b3: {self.symp_b3}, symp_c1: {self.symp_c1}, symp_c2: {self.symp_c2}, symp_c3: {self.symp_c3})"



class VaccSympRecord():

  def __init__(self):
      #create dictionary to store data of multiple people
      self.records_dic = {}

  def add_person_record(self, person):
      #Add a person object to the dictionary
      self.records_dic[person.name] = person

  def get_vacc_symp_status(self, name):
      #get vaccination status for a specific person 
      if name in self.records_dic:
        return self.records_dic[name].get_record()
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

  def symptoms_totals(self):
      #tracking symptoms for vac_a
      sympAVacATotal = 0
      sympBVacATotal = 0
      sympCVacATotal = 0

      #tracking symptoms for vac_b
      sympAVacBTotal = 0
      sympBVacBTotal = 0
      sympCVacBTotal = 0

      #tracking symptoms for vac_c
      sympAVacCTotal = 0
      sympBVacCTotal = 0
      sympCVacCTotal = 0

      for record in self.records_dic:
        # Count the symptoms only if an individual received the vaccine
        if self.records_dic[record].vac_a == 1:
          sympAVacATotal += int(self.records_dic[record].symp_a1)
          sympBVacATotal += int(self.records_dic[record].symp_a2)
          sympCVacATotal += int(self.records_dic[record].symp_a3)
        if self.records_dic[record].vac_b == 1:
          sympAVacBTotal += int(self.records_dic[record].symp_b1)
          sympBVacBTotal += int(self.records_dic[record].symp_b2)
          sympCVacBTotal += int(self.records_dic[record].symp_b3)
        if self.records_dic[record].vac_c == 1:
          sympAVacCTotal += int(self.records_dic[record].symp_c1)
          sympBVacCTotal += int(self.records_dic[record].symp_c2)
          sympCVacCTotal += int(self.records_dic[record].symp_c3)

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