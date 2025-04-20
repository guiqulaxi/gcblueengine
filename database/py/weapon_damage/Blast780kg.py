import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast780kg'
    dbObj.maxRange_m=114.915497
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=780.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=78.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
