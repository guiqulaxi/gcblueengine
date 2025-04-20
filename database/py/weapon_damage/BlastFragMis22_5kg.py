import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis22.5kg'
    dbObj.maxRange_m=2948.913574
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.022254
    dbObj.fragCharge_kg=9.701831
    dbObj.radCharge_kg=0.502225
    dbObj.fragMetal_kg=7.775916
    dbObj.fragFragment_kg=0.023563
    dbObj.fragSpread=0.210069
    return dbObj
