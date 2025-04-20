import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen3750kg'
    dbObj.maxRange_m=172.139740
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2625.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=375.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
