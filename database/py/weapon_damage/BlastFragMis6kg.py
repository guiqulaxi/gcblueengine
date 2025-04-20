import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis6kg'
    dbObj.maxRange_m=1919.657471
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.534859
    dbObj.fragCharge_kg=2.456761
    dbObj.radCharge_kg=0.153486
    dbObj.fragMetal_kg=2.008380
    dbObj.fragFragment_kg=0.010143
    dbObj.fragSpread=0.075625
    return dbObj
