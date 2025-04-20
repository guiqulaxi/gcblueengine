import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-25000kT'
    dbObj.maxRange_m=83453.007812
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=27499999232.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=12499999744.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
