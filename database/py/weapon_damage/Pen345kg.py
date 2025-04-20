import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen345kg'
    dbObj.maxRange_m=77.771858
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=241.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=34.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
