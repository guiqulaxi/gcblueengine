import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag43kg'
    dbObj.maxRange_m=1144.907104
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=15.387238
    dbObj.fragCharge_kg=13.391842
    dbObj.radCharge_kg=1.538724
    dbObj.fragMetal_kg=14.220921
    dbObj.fragFragment_kg=0.004173
    dbObj.fragSpread=0.300000
    return dbObj
