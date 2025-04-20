import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.8kg'
    dbObj.maxRange_m=218.665482
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.633503
    dbObj.fragCharge_kg=0.567664
    dbObj.radCharge_kg=0.063350
    dbObj.fragMetal_kg=0.598832
    dbObj.fragFragment_kg=0.000363
    dbObj.fragSpread=0.300000
    return dbObj
