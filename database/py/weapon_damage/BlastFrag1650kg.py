import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1650kg'
    dbObj.maxRange_m=5580.962402
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=593.817261
    dbObj.fragCharge_kg=511.621826
    dbObj.radCharge_kg=59.381729
    dbObj.fragMetal_kg=544.560913
    dbObj.fragFragment_kg=0.094019
    dbObj.fragSpread=0.300000
    return dbObj
