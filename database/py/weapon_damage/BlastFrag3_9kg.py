import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.9kg'
    dbObj.maxRange_m=350.965851
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.370434
    dbObj.fragCharge_kg=1.231377
    dbObj.radCharge_kg=0.137043
    dbObj.fragMetal_kg=1.298189
    dbObj.fragFragment_kg=0.000654
    dbObj.fragSpread=0.300000
    return dbObj
