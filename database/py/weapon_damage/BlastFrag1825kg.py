import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1825kg'
    dbObj.maxRange_m=5798.108887
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=656.814819
    dbObj.fragCharge_kg=565.873474
    dbObj.radCharge_kg=65.681480
    dbObj.fragMetal_kg=602.311707
    dbObj.fragFragment_kg=0.102018
    dbObj.fragSpread=0.300000
    return dbObj
