import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis27kg'
    dbObj.maxRange_m=3073.139404
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.905296
    dbObj.fragCharge_kg=11.723136
    dbObj.radCharge_kg=0.590530
    dbObj.fragMetal_kg=9.371568
    dbObj.fragFragment_kg=0.025605
    dbObj.fragSpread=0.258403
    return dbObj
