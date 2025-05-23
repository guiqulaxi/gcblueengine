# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Hamburg DD durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.600000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=2.710000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=3.060000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=3.630000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=4.430000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=5.460000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=6.720000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=8.210000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=9.930000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=11.870000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=14.050000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=17.700001
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*28
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=118.695000
    dbObj.waterBlastEffect[1].damageFactor=0.040000
    dbObj.waterBlastEffect[2].effectLevel=134.981003
    dbObj.waterBlastEffect[2].damageFactor=0.042000
    dbObj.waterBlastEffect[3].effectLevel=153.421997
    dbObj.waterBlastEffect[3].damageFactor=0.043000
    dbObj.waterBlastEffect[4].effectLevel=174.292999
    dbObj.waterBlastEffect[4].damageFactor=0.045000
    dbObj.waterBlastEffect[5].effectLevel=197.904007
    dbObj.waterBlastEffect[5].damageFactor=0.048000
    dbObj.waterBlastEffect[6].effectLevel=224.602005
    dbObj.waterBlastEffect[6].damageFactor=0.050000
    dbObj.waterBlastEffect[7].effectLevel=254.779999
    dbObj.waterBlastEffect[7].damageFactor=0.053000
    dbObj.waterBlastEffect[8].effectLevel=288.882996
    dbObj.waterBlastEffect[8].damageFactor=0.056000
    dbObj.waterBlastEffect[9].effectLevel=327.414001
    dbObj.waterBlastEffect[9].damageFactor=0.059000
    dbObj.waterBlastEffect[10].effectLevel=370.944000
    dbObj.waterBlastEffect[10].damageFactor=0.062000
    dbObj.waterBlastEffect[11].effectLevel=420.128998
    dbObj.waterBlastEffect[11].damageFactor=0.067000
    dbObj.waterBlastEffect[12].effectLevel=475.721985
    dbObj.waterBlastEffect[12].damageFactor=0.071000
    dbObj.waterBlastEffect[13].effectLevel=538.598022
    dbObj.waterBlastEffect[13].damageFactor=0.077000
    dbObj.waterBlastEffect[14].effectLevel=609.786011
    dbObj.waterBlastEffect[14].damageFactor=0.083000
    dbObj.waterBlastEffect[15].effectLevel=690.518982
    dbObj.waterBlastEffect[15].damageFactor=0.091000
    dbObj.waterBlastEffect[16].effectLevel=782.296997
    dbObj.waterBlastEffect[16].damageFactor=0.100000
    dbObj.waterBlastEffect[17].effectLevel=887.010010
    dbObj.waterBlastEffect[17].damageFactor=0.111000
    dbObj.waterBlastEffect[18].effectLevel=1007.111023
    dbObj.waterBlastEffect[18].damageFactor=0.125000
    dbObj.waterBlastEffect[19].effectLevel=1145.943970
    dbObj.waterBlastEffect[19].damageFactor=0.143000
    dbObj.waterBlastEffect[20].effectLevel=1308.344971
    dbObj.waterBlastEffect[20].damageFactor=0.167000
    dbObj.waterBlastEffect[21].effectLevel=1501.854980
    dbObj.waterBlastEffect[21].damageFactor=0.200000
    dbObj.waterBlastEffect[22].effectLevel=1739.490967
    dbObj.waterBlastEffect[22].damageFactor=0.250000
    dbObj.waterBlastEffect[23].effectLevel=2047.103027
    dbObj.waterBlastEffect[23].damageFactor=0.333000
    dbObj.waterBlastEffect[24].effectLevel=2488.423096
    dbObj.waterBlastEffect[24].damageFactor=0.500000
    dbObj.waterBlastEffect[25].effectLevel=3301.329102
    dbObj.waterBlastEffect[25].damageFactor=1.000000
    dbObj.waterBlastEffect[26].effectLevel=4257.720215
    dbObj.waterBlastEffect[26].damageFactor=2.000000
    dbObj.waterBlastEffect[27].effectLevel=5439.676758
    dbObj.waterBlastEffect[27].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*19
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=3303228.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=6000000.000000
    dbObj.fragEffect[2].damageFactor=0.030780
    dbObj.fragEffect[3].effectLevel=10000000.000000
    dbObj.fragEffect[3].damageFactor=0.039740
    dbObj.fragEffect[4].effectLevel=30000000.000000
    dbObj.fragEffect[4].damageFactor=0.068830
    dbObj.fragEffect[5].effectLevel=60000000.000000
    dbObj.fragEffect[5].damageFactor=0.097340
    dbObj.fragEffect[6].effectLevel=100000000.000000
    dbObj.fragEffect[6].damageFactor=0.125660
    dbObj.fragEffect[7].effectLevel=300000000.000000
    dbObj.fragEffect[7].damageFactor=0.217650
    dbObj.fragEffect[8].effectLevel=600000000.000000
    dbObj.fragEffect[8].damageFactor=0.307810
    dbObj.fragEffect[9].effectLevel=1000000000.000000
    dbObj.fragEffect[9].damageFactor=0.397370
    dbObj.fragEffect[10].effectLevel=3000000000.000000
    dbObj.fragEffect[10].damageFactor=0.688270
    dbObj.fragEffect[11].effectLevel=6000000000.000000
    dbObj.fragEffect[11].damageFactor=0.973370
    dbObj.fragEffect[12].effectLevel=10000000000.000000
    dbObj.fragEffect[12].damageFactor=1.256610
    dbObj.fragEffect[13].effectLevel=30000001024.000000
    dbObj.fragEffect[13].damageFactor=2.176510
    dbObj.fragEffect[14].effectLevel=60000002048.000000
    dbObj.fragEffect[14].damageFactor=3.078050
    dbObj.fragEffect[15].effectLevel=99999997952.000000
    dbObj.fragEffect[15].damageFactor=3.973750
    dbObj.fragEffect[16].effectLevel=299999985664.000000
    dbObj.fragEffect[16].damageFactor=6.882730
    dbObj.fragEffect[17].effectLevel=599999971328.000000
    dbObj.fragEffect[17].damageFactor=9.733650
    dbObj.fragEffect[18].effectLevel=999999995904.000000
    dbObj.fragEffect[18].damageFactor=12.566090
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
    dbObj.internalEffect=[pygcb.DamagePoint()]*14
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.004780
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.009550
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.019110
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.038200
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=0.076400
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=0.152800
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=0.305620
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=0.611320
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=1.222610
    dbObj.internalEffect[10].effectLevel=512.000000
    dbObj.internalEffect[10].damageFactor=2.445270
    dbObj.internalEffect[11].effectLevel=1024.000000
    dbObj.internalEffect[11].damageFactor=4.890540
    dbObj.internalEffect[12].effectLevel=2048.000000
    dbObj.internalEffect[12].damageFactor=9.780910
    dbObj.internalEffect[13].effectLevel=4096.000000
    dbObj.internalEffect[13].damageFactor=19.560860
    return dbObj
