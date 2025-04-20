import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1950kg'
    dbObj.maxRange_m=5942.598633
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=701.813171
    dbObj.fragCharge_kg=604.624573
    dbObj.radCharge_kg=70.181313
    dbObj.fragMetal_kg=643.562256
    dbObj.fragFragment_kg=0.107547
    dbObj.fragSpread=0.300000
    return dbObj
