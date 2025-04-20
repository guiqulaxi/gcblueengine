import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1175kg'
    dbObj.maxRange_m=116.963768
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=822.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=117.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
