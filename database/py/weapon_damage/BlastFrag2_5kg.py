import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2.5kg'
    dbObj.maxRange_m=273.015900
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.877401
    dbObj.fragCharge_kg=0.790066
    dbObj.radCharge_kg=0.087740
    dbObj.fragMetal_kg=0.832533
    dbObj.fragFragment_kg=0.000473
    dbObj.fragSpread=0.300000
    return dbObj
