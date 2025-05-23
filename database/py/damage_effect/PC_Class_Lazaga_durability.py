# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='PC Class Lazaga durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.900000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=3.010000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=3.320000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=3.840000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=4.570000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=5.510000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=6.660000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=8.010000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=9.580000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=11.350000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=13.330000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=16.790001
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*26
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=69.241997
    dbObj.waterBlastEffect[1].damageFactor=0.043000
    dbObj.waterBlastEffect[2].effectLevel=78.662003
    dbObj.waterBlastEffect[2].damageFactor=0.045000
    dbObj.waterBlastEffect[3].effectLevel=89.317001
    dbObj.waterBlastEffect[3].damageFactor=0.048000
    dbObj.waterBlastEffect[4].effectLevel=101.366997
    dbObj.waterBlastEffect[4].damageFactor=0.050000
    dbObj.waterBlastEffect[5].effectLevel=114.987000
    dbObj.waterBlastEffect[5].damageFactor=0.053000
    dbObj.waterBlastEffect[6].effectLevel=130.378006
    dbObj.waterBlastEffect[6].damageFactor=0.056000
    dbObj.waterBlastEffect[7].effectLevel=147.768005
    dbObj.waterBlastEffect[7].damageFactor=0.059000
    dbObj.waterBlastEffect[8].effectLevel=167.414001
    dbObj.waterBlastEffect[8].damageFactor=0.062000
    dbObj.waterBlastEffect[9].effectLevel=189.612000
    dbObj.waterBlastEffect[9].damageFactor=0.067000
    dbObj.waterBlastEffect[10].effectLevel=214.701996
    dbObj.waterBlastEffect[10].damageFactor=0.071000
    dbObj.waterBlastEffect[11].effectLevel=243.078995
    dbObj.waterBlastEffect[11].damageFactor=0.077000
    dbObj.waterBlastEffect[12].effectLevel=275.207001
    dbObj.waterBlastEffect[12].damageFactor=0.083000
    dbObj.waterBlastEffect[13].effectLevel=311.643005
    dbObj.waterBlastEffect[13].damageFactor=0.091000
    dbObj.waterBlastEffect[14].effectLevel=353.065002
    dbObj.waterBlastEffect[14].damageFactor=0.100000
    dbObj.waterBlastEffect[15].effectLevel=400.322998
    dbObj.waterBlastEffect[15].damageFactor=0.111000
    dbObj.waterBlastEffect[16].effectLevel=454.527008
    dbObj.waterBlastEffect[16].damageFactor=0.125000
    dbObj.waterBlastEffect[17].effectLevel=517.184998
    dbObj.waterBlastEffect[17].damageFactor=0.143000
    dbObj.waterBlastEffect[18].effectLevel=590.479004
    dbObj.waterBlastEffect[18].damageFactor=0.167000
    dbObj.waterBlastEffect[19].effectLevel=677.814026
    dbObj.waterBlastEffect[19].damageFactor=0.200000
    dbObj.waterBlastEffect[20].effectLevel=785.062988
    dbObj.waterBlastEffect[20].damageFactor=0.250000
    dbObj.waterBlastEffect[21].effectLevel=923.893982
    dbObj.waterBlastEffect[21].damageFactor=0.333000
    dbObj.waterBlastEffect[22].effectLevel=1123.068970
    dbObj.waterBlastEffect[22].damageFactor=0.500000
    dbObj.waterBlastEffect[23].effectLevel=1489.947998
    dbObj.waterBlastEffect[23].damageFactor=1.000000
    dbObj.waterBlastEffect[24].effectLevel=1921.583984
    dbObj.waterBlastEffect[24].damageFactor=2.000000
    dbObj.waterBlastEffect[25].effectLevel=2455.021973
    dbObj.waterBlastEffect[25].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*20
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=133328.812500
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=300000.000000
    dbObj.fragEffect[2].damageFactor=0.020790
    dbObj.fragEffect[3].effectLevel=600000.000000
    dbObj.fragEffect[3].damageFactor=0.029400
    dbObj.fragEffect[4].effectLevel=1000000.000000
    dbObj.fragEffect[4].damageFactor=0.037950
    dbObj.fragEffect[5].effectLevel=3000000.000000
    dbObj.fragEffect[5].damageFactor=0.065730
    dbObj.fragEffect[6].effectLevel=6000000.000000
    dbObj.fragEffect[6].damageFactor=0.092960
    dbObj.fragEffect[7].effectLevel=10000000.000000
    dbObj.fragEffect[7].damageFactor=0.120010
    dbObj.fragEffect[8].effectLevel=30000000.000000
    dbObj.fragEffect[8].damageFactor=0.207860
    dbObj.fragEffect[9].effectLevel=60000000.000000
    dbObj.fragEffect[9].damageFactor=0.293960
    dbObj.fragEffect[10].effectLevel=100000000.000000
    dbObj.fragEffect[10].damageFactor=0.379500
    dbObj.fragEffect[11].effectLevel=300000000.000000
    dbObj.fragEffect[11].damageFactor=0.657320
    dbObj.fragEffect[12].effectLevel=600000000.000000
    dbObj.fragEffect[12].damageFactor=0.929590
    dbObj.fragEffect[13].effectLevel=1000000000.000000
    dbObj.fragEffect[13].damageFactor=1.200100
    dbObj.fragEffect[14].effectLevel=3000000000.000000
    dbObj.fragEffect[14].damageFactor=2.078630
    dbObj.fragEffect[15].effectLevel=6000000000.000000
    dbObj.fragEffect[15].damageFactor=2.939630
    dbObj.fragEffect[16].effectLevel=10000000000.000000
    dbObj.fragEffect[16].damageFactor=3.795050
    dbObj.fragEffect[17].effectLevel=30000001024.000000
    dbObj.fragEffect[17].damageFactor=6.573220
    dbObj.fragEffect[18].effectLevel=60000002048.000000
    dbObj.fragEffect[18].damageFactor=9.295930
    dbObj.fragEffect[19].effectLevel=99999997952.000000
    dbObj.fragEffect[19].damageFactor=12.001000
    dbObj.radEffect=[pygcb.DamagePoint()]*6
    dbObj.radEffect[0].effectLevel=0.000000
    dbObj.radEffect[0].damageFactor=0.000000
    dbObj.radEffect[1].effectLevel=5000.000000
    dbObj.radEffect[1].damageFactor=0.000000
    dbObj.radEffect[2].effectLevel=25000.000000
    dbObj.radEffect[2].damageFactor=0.400000
    dbObj.radEffect[3].effectLevel=50000.000000
    dbObj.radEffect[3].damageFactor=2.000000
    dbObj.radEffect[4].effectLevel=125000.000000
    dbObj.radEffect[4].damageFactor=5.000000
    dbObj.radEffect[5].effectLevel=250000.000000
    dbObj.radEffect[5].damageFactor=20.000000
    dbObj.internalEffect=[pygcb.DamagePoint()]*11
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.031240
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.062480
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.124890
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.249900
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=0.499640
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=0.999450
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=1.998710
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=3.997140
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=7.994360
    dbObj.internalEffect[10].effectLevel=512.000000
    dbObj.internalEffect[10].damageFactor=15.989690
    return dbObj
