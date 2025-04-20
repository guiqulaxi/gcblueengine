import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag16kg'
    dbObj.maxRange_m=725.644775
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.691619
    dbObj.fragCharge_kg=5.005587
    dbObj.radCharge_kg=0.569162
    dbObj.fragMetal_kg=5.302794
    dbObj.fragFragment_kg=0.001927
    dbObj.fragSpread=0.300000
    return dbObj
