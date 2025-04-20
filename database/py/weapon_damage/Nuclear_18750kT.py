import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-18750kT'
    dbObj.maxRange_m=76552.671875
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=20625000448.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=9374999552.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
