import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir12.5kg'
    dbObj.maxRange_m=2506.228027
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.971348
    dbObj.fragCharge_kg=5.269101
    dbObj.radCharge_kg=0.297135
    dbObj.fragMetal_kg=4.259551
    dbObj.fragFragment_kg=0.017038
    dbObj.fragSpread=0.120563
    return dbObj
