import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast255kg'
    dbObj.maxRange_m=79.193398
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=255.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=25.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
