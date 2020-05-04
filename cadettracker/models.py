from django.db import models

class Location(models.Model):
    BLDGNum = models.CharField(max_length=4)
    Floor = models.IntegerField()
    RoomNum = models.IntegerField()
    RoomDescription = models.CharField(max_length=50)

    def name(self):
        return (self.Location_ID + "is the location")

    def __str__(self):
        return (self.Location_ID + "is the location")

class Supply(models.Model):
    item = models.CharField(max_length=50)

class Personnel(models.Model):
    person_ID = models.CharField(max_length=6)
    job_title = models.CharField(max_length=15)
    room_num = models.CharField(max_length=4)
    phone_num = models.CharField(max_length=10)
    company_ID = models.CharField(max_length = 2)
    regiment_ID = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE, default=1)

class Company(models.Model):
    CompanyName = models.CharField(max_length=2) #A, B, C, etc.
    SupplyOfficer = models.ForeignKey(Personnel, related_name = "companies", on_delete=models.CASCADE ) #Alpha, Bravo, Charlie etc.
    regiment = models.IntegerField() #1,2,3,4
    Supply_NCO = models.ForeignKey(Personnel, related_name = "Scompanies", on_delete=models.CASCADE ) #Go Buffs!  Go Greeks, etc.
    Location_ID = models.ForeignKey(Location, on_delete=models.CASCADE) #Buffalos, Greeks.

    def __str__(self):
        return (self.shortname + "-" + str(self.regiment))

'''
class CompanyHasSupply(models.Model):
    Item = models.ForeignKey(Supply.item, on_delete=models.CASCADE) #A, B, C, etc.
    Num_Available = models.IntegerField() #Alpha, Bravo, Charlie etc.
    Company_ID = models.ForeignKey(Company.Company_ID(), on_delete=models.CASCADE) #1,2,3,4
    Location = models.ForeignKey(Location.Location_ID(), on_delete=models.CASCADE) #Go Buffs!  Go Greeks, etc.
    #Location_ID = models.ForeignKey(Locations, on_delete=models.CASCADE) #Buffalos, Greeks.



class RegHasSupplie(models.Model):
    item = models.CharField(max_length=15)
    NumberAvailable = models.IntegerField()
    RegimentID = models.IntegerField()
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Regiment(models.Model):
    Reg_ID = models.IntegerField()
    Regiment_Supply_NCO = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    Regiment_Supply_Officer = models.ForeignKey(Personnel, on_delete=models.CASCADE)
'''
