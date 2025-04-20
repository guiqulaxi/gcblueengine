import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2500kg'
    dbObj.maxRange_m=9680.283203
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=267.588196
    dbObj.fragCharge_kg=1271.607910
    dbObj.radCharge_kg=26.758821
    dbObj.fragMetal_kg=960.803955
    dbObj.fragFragment_kg=0.295450
    dbObj.fragSpread=0.300000
    return dbObj
