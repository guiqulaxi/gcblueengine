import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-10750kT'
    dbObj.maxRange_m=64786.203125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=11825000448.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=5375000064.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
