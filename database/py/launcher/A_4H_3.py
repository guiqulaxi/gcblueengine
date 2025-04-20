import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='A-4H 3'
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
    dbObj.childClassList=['400 liter tank','50mm (2in) FFAR Rockets','600 liter tank','AGM-12A','AGM-12B','AGM-12C','AGM-45A','AGM-45B','AGM-62 mk21','AGM-62 mk23','AGM-62 mk3','AGM-62 mk5','AGM-62','AGM-62','AGM-78A','AGM-78B','AGM-78C','AGM-78D','M117','M118','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[1,57,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,12,12,6,6,3,1]
    dbObj.childLoadTime_s=[240.000000,480.000000,240.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,420.000000,240.000000,420.000000,420.000000,480.000000,480.000000,360.000000,240.000000]
    dbObj.childCycleTime_s=[0.200000,0.100000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.100000,0.100000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
