import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2850kg'
    dbObj.maxRange_m=6923.380859
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1025.803833
    dbObj.fragCharge_kg=883.630798
    dbObj.radCharge_kg=102.580383
    dbObj.fragMetal_kg=940.565369
    dbObj.fragFragment_kg=0.149581
    dbObj.fragSpread=0.300000
    return dbObj
