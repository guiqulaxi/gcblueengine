import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast620kg'
    dbObj.maxRange_m=106.457809
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=620.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=62.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
