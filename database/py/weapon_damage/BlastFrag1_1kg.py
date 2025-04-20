import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.1kg'
    dbObj.maxRange_m=171.022659
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.393649
    dbObj.fragCharge_kg=0.342567
    dbObj.radCharge_kg=0.039365
    dbObj.fragMetal_kg=0.363784
    dbObj.fragFragment_kg=0.000279
    dbObj.fragSpread=0.300000
    return dbObj
