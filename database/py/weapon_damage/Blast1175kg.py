import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1175kg'
    dbObj.maxRange_m=131.714523
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1175.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=117.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
