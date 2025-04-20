import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis25.5kg'
    dbObj.maxRange_m=3035.015869
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.613171
    dbObj.fragCharge_kg=11.047886
    dbObj.radCharge_kg=0.561317
    dbObj.fragMetal_kg=8.838943
    dbObj.fragFragment_kg=0.024969
    dbObj.fragSpread=0.241736
    return dbObj
