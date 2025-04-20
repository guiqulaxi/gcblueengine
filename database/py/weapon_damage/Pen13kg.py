import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen13kg'
    dbObj.maxRange_m=26.101891
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.100000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1.300000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
