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
    xNum = models.CharField(max_length=6)
    jobTitle = models.CharField(max_length=15)
    roomNum = models.CharField(max_length=4)
    phoneNum = models.CharField(max_length=10)
    companyLabel = models.CharField(max_length = 2)
    regimentLabel = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE, default=1)

class Company(models.Model):
    CompanyName = models.CharField(max_length=2) #A, B, C, etc.
    SupplyOfficer = models.ForeignKey(Personnel, related_name = "companies", on_delete=models.CASCADE ) #Alpha, Bravo, Charlie etc.
    regiment = models.IntegerField() #1,2,3,4
    SupplyNCO = models.ForeignKey(Personnel, related_name = "Scompanies", on_delete=models.CASCADE ) #Go Buffs!  Go Greeks, etc.
    LocationID = models.ForeignKey(Location, on_delete=models.CASCADE) #Buffalos, Greeks.

    def __str__(self):
        return (self.shortname + "-" + str(self.regiment))


class CompanyHasSupply(models.Model):
    Item = models.ForeignKey(Supply, on_delete=models.CASCADE) #A, B, C, etc.
    NumAvailable = models.IntegerField() #Alpha, Bravo, Charlie etc.
    CompanyLabel = models.ForeignKey(Company, on_delete=models.CASCADE) #1,2,3,4
    Location = models.ForeignKey(Location, on_delete=models.CASCADE) #Go Buffs!  Go Greeks, etc.
    #Location_ID = models.ForeignKey(Locations, on_delete=models.CASCADE) #Buffalos, Greeks.



class RegHasSupply(models.Model):
    item = models.CharField(max_length=15)
    NumberAvailable = models.IntegerField()
    RegimentID = models.IntegerField()
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)


'''
class Regiment(models.Model):
    Reg_ID = models.IntegerField()
    Regiment_Supply_NCO = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    Regiment_Supply_Officer = models.ForeignKey(Personnel, on_delete=models.CASCADE)
'''
