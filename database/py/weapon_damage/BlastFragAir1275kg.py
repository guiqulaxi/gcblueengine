import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1275kg'
    dbObj.maxRange_m=7418.002930
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=157.643555
    dbObj.fragCharge_kg=634.404297
    dbObj.radCharge_kg=15.764356
    dbObj.fragMetal_kg=482.952148
    dbObj.fragFragment_kg=0.163991
    dbObj.fragSpread=0.300000
    return dbObj
