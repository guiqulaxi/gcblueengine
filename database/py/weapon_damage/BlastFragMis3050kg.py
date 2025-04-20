import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis3050kg'
    dbObj.maxRange_m=10406.583984
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=311.499603
    dbObj.fragCharge_kg=1561.333618
    dbObj.radCharge_kg=31.149960
    dbObj.fragMetal_kg=1177.166748
    dbObj.fragFragment_kg=0.347349
    dbObj.fragSpread=0.300000
    return dbObj
