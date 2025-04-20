import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis75kg'
    dbObj.maxRange_m=3763.005615
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=14.513824
    dbObj.fragCharge_kg=33.824120
    dbObj.radCharge_kg=1.451382
    dbObj.fragMetal_kg=26.662060
    dbObj.fragFragment_kg=0.038697
    dbObj.fragSpread=0.300000
    return dbObj
