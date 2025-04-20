import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='A7 2-7'
    dbObj.natoClass=''
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=0.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=0.000000
    dbObj.height_m=0.000000
    dbObj.childClassList=['M118','M117','Mk-84','Mk-83','Mk-82','Mk-81','Mk-10 Mod5 Mine','Mk-10 Mod6 Mine','Mk-25 Mine','Mk-36 Mod1 Mine','Mk-36 Mod2 Mine','Mk-39 Mine','Mk-56 Mine','Mk-36 DST','Mk-40 DST','Mk-41 DST','Mk-59 DST','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','50mm (2in) FFAR Rockets']
    dbObj.childCapacityList=[2,6,2,6,12,12,2,2,2,2,2,2,2,10,6,2,8,8,8,38]
    dbObj.childLoadTime_s=[120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000]
    dbObj.childCycleTime_s=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.CalculateParams()
    return dbObj
