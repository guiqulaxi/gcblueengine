import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-33750kT'
    dbObj.maxRange_m=91315.000000
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=37125001216.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=16874999808.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
