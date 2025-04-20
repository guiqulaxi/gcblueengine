import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis15.5kg'
    dbObj.maxRange_m=2674.171143
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.602240
    dbObj.fragCharge_kg=6.588507
    dbObj.radCharge_kg=0.360224
    dbObj.fragMetal_kg=5.309253
    dbObj.fragFragment_kg=0.019377
    dbObj.fragSpread=0.144823
    return dbObj
