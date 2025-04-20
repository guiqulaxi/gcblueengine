import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1kg'
    dbObj.maxRange_m=166.307831
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.360000
    dbObj.fragCharge_kg=0.310000
    dbObj.radCharge_kg=0.036000
    dbObj.fragMetal_kg=0.330000
    dbObj.fragFragment_kg=0.000271
    dbObj.fragSpread=0.300000
    return dbObj
