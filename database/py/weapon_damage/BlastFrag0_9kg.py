import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.9kg'
    dbObj.maxRange_m=160.285797
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.324000
    dbObj.fragCharge_kg=0.279000
    dbObj.radCharge_kg=0.032400
    dbObj.fragMetal_kg=0.297000
    dbObj.fragFragment_kg=0.000261
    dbObj.fragSpread=0.300000
    return dbObj
