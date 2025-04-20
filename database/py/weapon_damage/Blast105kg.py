import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast105kg'
    dbObj.maxRange_m=58.934158
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=105.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=10.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
