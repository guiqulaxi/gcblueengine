import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis90kg'
    dbObj.maxRange_m=3827.229980
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=17.011894
    dbObj.fragCharge_kg=40.858738
    dbObj.radCharge_kg=1.701189
    dbObj.fragMetal_kg=32.129368
    dbObj.fragFragment_kg=0.040062
    dbObj.fragSpread=0.300000
    return dbObj
