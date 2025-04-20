import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.1kg'
    dbObj.maxRange_m=310.295074
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.088096
    dbObj.fragCharge_kg=0.979603
    dbObj.radCharge_kg=0.108810
    dbObj.fragMetal_kg=1.032301
    dbObj.fragFragment_kg=0.000556
    dbObj.fragSpread=0.300000
    return dbObj
