# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcDamageEffect()
    dbObj.databaseClass='Pr 97P durability'
    dbObj.blastEffect=[pygcb.DamagePoint()]*13
    dbObj.blastEffect[0].effectLevel=0.000000
    dbObj.blastEffect[0].damageFactor=0.000000
    dbObj.blastEffect[1].effectLevel=2.030000
    dbObj.blastEffect[1].damageFactor=0.000000
    dbObj.blastEffect[2].effectLevel=2.140000
    dbObj.blastEffect[2].damageFactor=0.100000
    dbObj.blastEffect[3].effectLevel=2.450000
    dbObj.blastEffect[3].damageFactor=0.200000
    dbObj.blastEffect[4].effectLevel=2.970000
    dbObj.blastEffect[4].damageFactor=0.300000
    dbObj.blastEffect[5].effectLevel=3.700000
    dbObj.blastEffect[5].damageFactor=0.400000
    dbObj.blastEffect[6].effectLevel=4.630000
    dbObj.blastEffect[6].damageFactor=0.500000
    dbObj.blastEffect[7].effectLevel=5.780000
    dbObj.blastEffect[7].damageFactor=0.600000
    dbObj.blastEffect[8].effectLevel=7.130000
    dbObj.blastEffect[8].damageFactor=0.700000
    dbObj.blastEffect[9].effectLevel=8.690000
    dbObj.blastEffect[9].damageFactor=0.800000
    dbObj.blastEffect[10].effectLevel=10.460000
    dbObj.blastEffect[10].damageFactor=0.900000
    dbObj.blastEffect[11].effectLevel=12.440000
    dbObj.blastEffect[11].damageFactor=1.000000
    dbObj.blastEffect[12].effectLevel=15.670000
    dbObj.blastEffect[12].damageFactor=2.000000
    dbObj.waterBlastEffect=[pygcb.DamagePoint()]*28
    dbObj.waterBlastEffect[0].effectLevel=0.000000
    dbObj.waterBlastEffect[0].damageFactor=0.000000
    dbObj.waterBlastEffect[1].effectLevel=87.664001
    dbObj.waterBlastEffect[1].damageFactor=0.040000
    dbObj.waterBlastEffect[2].effectLevel=99.693001
    dbObj.waterBlastEffect[2].damageFactor=0.042000
    dbObj.waterBlastEffect[3].effectLevel=113.313004
    dbObj.waterBlastEffect[3].damageFactor=0.043000
    dbObj.waterBlastEffect[4].effectLevel=128.727997
    dbObj.waterBlastEffect[4].damageFactor=0.045000
    dbObj.waterBlastEffect[5].effectLevel=146.166000
    dbObj.waterBlastEffect[5].damageFactor=0.048000
    dbObj.waterBlastEffect[6].effectLevel=165.884003
    dbObj.waterBlastEffect[6].damageFactor=0.050000
    dbObj.waterBlastEffect[7].effectLevel=188.173004
    dbObj.waterBlastEffect[7].damageFactor=0.053000
    dbObj.waterBlastEffect[8].effectLevel=213.360001
    dbObj.waterBlastEffect[8].damageFactor=0.056000
    dbObj.waterBlastEffect[9].effectLevel=241.817993
    dbObj.waterBlastEffect[9].damageFactor=0.059000
    dbObj.waterBlastEffect[10].effectLevel=273.967987
    dbObj.waterBlastEffect[10].damageFactor=0.062000
    dbObj.waterBlastEffect[11].effectLevel=310.295013
    dbObj.waterBlastEffect[11].damageFactor=0.067000
    dbObj.waterBlastEffect[12].effectLevel=351.354004
    dbObj.waterBlastEffect[12].damageFactor=0.071000
    dbObj.waterBlastEffect[13].effectLevel=397.791992
    dbObj.waterBlastEffect[13].damageFactor=0.077000
    dbObj.waterBlastEffect[14].effectLevel=450.369995
    dbObj.waterBlastEffect[14].damageFactor=0.083000
    dbObj.waterBlastEffect[15].effectLevel=509.996002
    dbObj.waterBlastEffect[15].damageFactor=0.091000
    dbObj.waterBlastEffect[16].effectLevel=577.781006
    dbObj.waterBlastEffect[16].damageFactor=0.100000
    dbObj.waterBlastEffect[17].effectLevel=655.119019
    dbObj.waterBlastEffect[17].damageFactor=0.111000
    dbObj.waterBlastEffect[18].effectLevel=743.822021
    dbObj.waterBlastEffect[18].damageFactor=0.125000
    dbObj.waterBlastEffect[19].effectLevel=846.359985
    dbObj.waterBlastEffect[19].damageFactor=0.143000
    dbObj.waterBlastEffect[20].effectLevel=966.304016
    dbObj.waterBlastEffect[20].damageFactor=0.167000
    dbObj.waterBlastEffect[21].effectLevel=1109.224976
    dbObj.waterBlastEffect[21].damageFactor=0.200000
    dbObj.waterBlastEffect[22].effectLevel=1284.735962
    dbObj.waterBlastEffect[22].damageFactor=0.250000
    dbObj.waterBlastEffect[23].effectLevel=1511.928955
    dbObj.waterBlastEffect[23].damageFactor=0.333000
    dbObj.waterBlastEffect[24].effectLevel=1837.874023
    dbObj.waterBlastEffect[24].damageFactor=0.500000
    dbObj.waterBlastEffect[25].effectLevel=2438.262939
    dbObj.waterBlastEffect[25].damageFactor=1.000000
    dbObj.waterBlastEffect[26].effectLevel=3144.624023
    dbObj.waterBlastEffect[26].damageFactor=2.000000
    dbObj.waterBlastEffect[27].effectLevel=4017.582031
    dbObj.waterBlastEffect[27].damageFactor=4.000000
    dbObj.fragEffect=[pygcb.DamagePoint()]*26
    dbObj.fragEffect[0].effectLevel=0.000000
    dbObj.fragEffect[0].damageFactor=0.000000
    dbObj.fragEffect[1].effectLevel=1500.000000
    dbObj.fragEffect[1].damageFactor=0.000000
    dbObj.fragEffect[2].effectLevel=3000.000000
    dbObj.fragEffect[2].damageFactor=0.002010
    dbObj.fragEffect[3].effectLevel=6000.000000
    dbObj.fragEffect[3].damageFactor=0.002840
    dbObj.fragEffect[4].effectLevel=10000.000000
    dbObj.fragEffect[4].damageFactor=0.003660
    dbObj.fragEffect[5].effectLevel=30000.000000
    dbObj.fragEffect[5].damageFactor=0.006350
    dbObj.fragEffect[6].effectLevel=60000.000000
    dbObj.fragEffect[6].damageFactor=0.008980
    dbObj.fragEffect[7].effectLevel=100000.000000
    dbObj.fragEffect[7].damageFactor=0.011590
    dbObj.fragEffect[8].effectLevel=300000.000000
    dbObj.fragEffect[8].damageFactor=0.020070
    dbObj.fragEffect[9].effectLevel=600000.000000
    dbObj.fragEffect[9].damageFactor=0.028390
    dbObj.fragEffect[10].effectLevel=1000000.000000
    dbObj.fragEffect[10].damageFactor=0.036650
    dbObj.fragEffect[11].effectLevel=3000000.000000
    dbObj.fragEffect[11].damageFactor=0.063480
    dbObj.fragEffect[12].effectLevel=6000000.000000
    dbObj.fragEffect[12].damageFactor=0.089770
    dbObj.fragEffect[13].effectLevel=10000000.000000
    dbObj.fragEffect[13].damageFactor=0.115900
    dbObj.fragEffect[14].effectLevel=30000000.000000
    dbObj.fragEffect[14].damageFactor=0.200740
    dbObj.fragEffect[15].effectLevel=60000000.000000
    dbObj.fragEffect[15].damageFactor=0.283890
    dbObj.fragEffect[16].effectLevel=100000000.000000
    dbObj.fragEffect[16].damageFactor=0.366500
    dbObj.fragEffect[17].effectLevel=300000000.000000
    dbObj.fragEffect[17].damageFactor=0.634800
    dbObj.fragEffect[18].effectLevel=600000000.000000
    dbObj.fragEffect[18].damageFactor=0.897740
    dbObj.fragEffect[19].effectLevel=1000000000.000000
    dbObj.fragEffect[19].damageFactor=1.158970
    dbObj.fragEffect[20].effectLevel=3000000000.000000
    dbObj.fragEffect[20].damageFactor=2.007400
    dbObj.fragEffect[21].effectLevel=6000000000.000000
    dbObj.fragEffect[21].damageFactor=2.838890
    dbObj.fragEffect[22].effectLevel=10000000000.000000
    dbObj.fragEffect[22].damageFactor=3.664990
    dbObj.fragEffect[23].effectLevel=30000001024.000000
    dbObj.fragEffect[23].damageFactor=6.347960
    dbObj.fragEffect[24].effectLevel=60000002048.000000
    dbObj.fragEffect[24].damageFactor=8.977370
    dbObj.fragEffect[25].effectLevel=99999997952.000000
    dbObj.fragEffect[25].damageFactor=11.589730
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
    dbObj.internalEffect=[pygcb.DamagePoint()]*10
    dbObj.internalEffect[0].effectLevel=0.000000
    dbObj.internalEffect[0].damageFactor=0.000000
    dbObj.internalEffect[1].effectLevel=1.000000
    dbObj.internalEffect[1].damageFactor=0.076000
    dbObj.internalEffect[2].effectLevel=2.000000
    dbObj.internalEffect[2].damageFactor=0.151990
    dbObj.internalEffect[3].effectLevel=4.000000
    dbObj.internalEffect[3].damageFactor=0.303880
    dbObj.internalEffect[4].effectLevel=8.000000
    dbObj.internalEffect[4].damageFactor=0.607960
    dbObj.internalEffect[5].effectLevel=16.000000
    dbObj.internalEffect[5].damageFactor=1.215910
    dbObj.internalEffect[6].effectLevel=32.000000
    dbObj.internalEffect[6].damageFactor=2.431810
    dbObj.internalEffect[7].effectLevel=64.000000
    dbObj.internalEffect[7].damageFactor=4.863720
    dbObj.internalEffect[8].effectLevel=128.000000
    dbObj.internalEffect[8].damageFactor=9.727320
    dbObj.internalEffect[9].effectLevel=256.000000
    dbObj.internalEffect[9].damageFactor=19.454500
    return dbObj
