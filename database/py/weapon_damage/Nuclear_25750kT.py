import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-25750kT'
    dbObj.maxRange_m=84196.328125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=28324999168.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=12874999808.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
