import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen375kg'
    dbObj.maxRange_m=79.961540
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=262.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=37.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
