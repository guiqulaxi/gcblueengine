import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3550kg'
    dbObj.maxRange_m=10971.981445
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=349.273926
    dbObj.fragCharge_kg=1826.150757
    dbObj.radCharge_kg=34.927391
    dbObj.fragMetal_kg=1374.575317
    dbObj.fragFragment_kg=0.391171
    dbObj.fragSpread=0.300000
    return dbObj
