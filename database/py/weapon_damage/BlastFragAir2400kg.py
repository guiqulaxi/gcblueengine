import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2400kg'
    dbObj.maxRange_m=9533.937500
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=259.300995
    dbObj.fragCharge_kg=1219.132690
    dbObj.radCharge_kg=25.930098
    dbObj.fragMetal_kg=921.566345
    dbObj.fragFragment_kg=0.285580
    dbObj.fragSpread=0.300000
    return dbObj
