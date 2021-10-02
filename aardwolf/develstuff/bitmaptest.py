from aardwolf.protocol.fastpath import TS_FP_UPDATE_PDU
import rle
from PyQt5.Qt import QWidget, QHBoxLayout, QLabel, QApplication                                                                      
from PyQt5 import QtGui                                                                                                          
import sys   

def RDPBitmapToQtImage(width, height, bitsPerPixel, isCompress, data):
    """
    @summary: Bitmap transformation to Qt object
    @param width: width of bitmap
    @param height: height of bitmap
    @param bitsPerPixel: number of bit per pixel
    @param isCompress: use RLE compression
    @param data: bitmap data
    """
    image = None
    #allocate
    
    if bitsPerPixel == 15:
        if isCompress:
            buf = bytes(width * height * 2)
            rle.bitmap_decompress(buf, width, height, data, 2)
            image = QtGui.QImage(buf, width, height, QtGui.QImage.Format_RGB555)
        else:
            image = QtGui.QImage(data, width, height, QtGui.QImage.Format_RGB555).transformed(QtGui.QTransform(1.0, 0.0, 0.0, -1.0, 0.0, 0.0))
    
    elif bitsPerPixel == 16:
        if isCompress:
            buf = bytes(width * height * 2)
            rle.bitmap_decompress(buf, width, height, data, 2)
            image = QtGui.QImage(buf, width, height, QtGui.QImage.Format_RGB16)
        else:
            image = QtGui.QImage(data, width, height, QtGui.QImage.Format_RGB16).transformed(QtGui.QTransform(1.0, 0.0, 0.0, -1.0, 0.0, 0.0))
    
    elif bitsPerPixel == 24:
        if isCompress:
            buf = bytes(width * height * 3)
            rle.bitmap_decompress(buf, width, height, data, 3)
            image = QtGui.QImage(buf, width, height, QtGui.QImage.Format_RGB888)
        else:
            image = QtGui.QImage(data, width, height, QtGui.QImage.Format_RGB888).transformed(QtGui.QTransform(1.0, 0.0, 0.0, -1.0, 0.0, 0.0))
            
    elif bitsPerPixel == 32:
        if isCompress:
            buf = bytes(width * height * 4)
            rle.bitmap_decompress(buf, width, height, data, 4)
            image = QtGui.QImage(buf, width, height, QtGui.QImage.Format_RGB32)
        else:
            image = QtGui.QImage(data, width, height, QtGui.QImage.Format_RGB32).transformed(QtGui.QTransform(1.0, 0.0, 0.0, -1.0, 0.0, 0.0))
    else:
        print("Receive image in bad format")
        image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
    return image


reqdata = bytes.fromhex('00b59e01983501000400c0018000ff01bf004000400010000104130b8589526952695269526952ca89528c8a52895269526952895289528a52aa52aa5a8a5289526952c9694ac6895299695269526952695289528a528a528a5aaa5aaa5aaa5aca5aca5aca5aa952aa52aa528a52aa5aca5aaa5a8a52694a694a69526889529169526952895289528952895269526952694a695269528952aa52aa528a528a5269526c694a068014695289528952895289528a52aa5aaa5aca5aca5aaa5aaa5aaa5aaa5aca5aca5aca5aaa5a69526952895289526952695269526952695269528952895269526952695269528a5289526952694a694a6952695289528a528a528a5289528952895289528952695269520d9769528a528a528952895289528a52aa5aca5aca5aaa5aaa5aaa5aaa52aa52aa5aaa5a6952895289526952694a694a099b694a89528952695269526952695269526952895289526952695269528952895289528952895289526952694a694a694a694a694a694a0b918952aa52aa52ca5aea5aeb5aca5aaa5aaa5aaa5aca5a69528952895269526952694a68695266694a046869520480026952694a694a6952694a694a694a694a694a694a6952695269526952895289528a528a52aa52aa52ca5aeb620b63ca5aaa5aaa5aca5aaa5a6952695289528952895289526a6952048b694a69528952895269526952695269526952694a694a086a694a0196695289528a528a528a528a52aa52ea5aeb62ca5aaa5aaa5aca5aaa5a694a69526952895289528952895289520d95694a895289526952695269528952895269526952695289528952895289526952694a694a6952694a695268694a0291895289528a528a52aa5acb5aeb62ca5aaa5aca5aca5aca5a695269526952695269520682694a694a09926952694a694a694a695289528952895289528952895289528a52895289526952695269526c694a01908a52aa52aa5aaa5aca5aca5aaa5aaa5aaa5aaa5aaa5a69526952694a694a694a6b69520684694a694a695269520a866952695289528952695269520a8e6952895289528a52ca5aaa5aca5aea62ca5aca5aca5aaa5a694a694a1e8c69528952895289526952895289528a5289528952895269526a694a99695289528a528952aa5aaa5aaa5aeb620b63ca5a694a694a694a694a694a694a6952695269526952895289528952695269526b694a0195695289528952895289528952895289526952695269526952695289528952895289528952895269528952078a69528a528a52aa52a9528952ca5aea62ca5ae8410c86895269526952695269526952109f89526952694a694a694a69528952895289528a5289528a528a52694a694a694a69526952694a694a6952695269528a52aa5289528952ca5aca5a2000c7390a801c6952695269528952695269526952695269526952694a694a694a694a694a694a6952695289528952695289528a5289526952694a694a6952695289528a528a52695269526952695289526952895289528952694a69526952694a694a89528a52a952aa52ca5aca5a00002000a631694a694a694a694a694a08838952895289521080018a528952694a694a694a695269528952895269526952695269528952895289528952895269526952895289528952695269528952aa52aa5aaa520000000000004529068269526952108c694a694a69528952895289528a528a5289526952694a694a686952019f6952695269526952695289528a5269526952694a694a8952aa52aa528a520000000000000000a2102842694a694a694a694a6952695289528952895269520681695207898952895269526952695289528a528952895268695282694a69520780208a528952895289528952695269528a52000000000000000000004108c739694a694a694a694a694a695289528a528952695289528952895289528952695269526952694a694a694a694a694a694a695269526952695289528952895289528952695269528952895269526952694a694a69526952695269528952895289528952078f895200000000000000000000000000004529694a694a694a694a694a694a088189520886694a695269526952695269520881694a068769528952895289528a528a528a520c910000a2102842694a694a694a694a694a694a69528952895289528a528a52895289520882694a694a0694895289528952895269526952694a694a69526952694a69526952695289528952aa52aa52aa528a520c8300004108c739068769526952895289528a528a528a520a9d694a694a69526952895289528952895269526952695269526952694a695269526952694a69526952695289528952aa52aa528a528952895289520a9100000000e3182842694a694a694a694a6952695269526952895289528a528a5269520c83695289528a520691695289526952694a694a694a695269526952695289528a52aa528a52895289528a526c00009120006529694a694a694a694a694a695269526952695289528a52895269526952695268694a028469528a5289528952068e8952694a694a6952695269526952694a895289528a528a528a528a520d84000000008210e73968694a0d9b694a69526952895289528952895269526952695269526952694a694a694a694a694a69526952694a695289528952895289528a52aa5270000082e4202842068869526952695289528952695269526952088969526952895289528952695269526952694a0788695269528952895289528952aa52aa5a7100009020006529494a694a694a694a694a694a694a694a69526952895289528952695268694a019469528952895289528952695289528952694a694a694a694a694a694a694a69526952895289528a52138f0000000020004529294a694a694a694a694a694a694a695289528a528a520989694a6952695269526952695289528952694a06886952695269526952895289528a52aa527500008d200024212842694a694a694a694a694a695289528a528a5269526a694a048169520d8289528a52158d00000000000004212842694a694a694a694a69528a528a52895208866952694a694a694a6952695268694a04846952895289528952188b000000000321e739694a694a694a69528a528952695207828952695271694a82695269521b8a00000000410824290842694a89528952695269520681695208826952695269694a018169521c8600000000000082108531494a0867694a8569526952695289526952000985000000002008e320a6396e694a0c8289528952000194000000000000000082102429c739694a694a694a695269526952694a694a694a694a694a695269526b694a00038920002000000000000000000082102429e739076d694a00058c20000000000000000000000000000000a210c3184429a631d031ae73010000000000007000008a200882100421442944296531c739c739c739c739d03561080100000000000060150000d82008070000000000000083200040084008d03c2000010000000000001883200841084108080013850000000020002000200808605b0000404003000000000000000086400800000000000000000000403a0100000000000000812008403e2100000000000000874008200800000000000020002000470100000000008086200040082008000000000000403c010000000000000084200820000000000047630000000000000160a80000d820080100000000000000d80008010000000000000083000000000000d0412008030000000000000000d080000807000000000000000000000000000000008220082008d03c20080100000000000000d03d20000100000000000000d800080100000000000000840000000000002008d03e20000100000000000000fe5001000000000000000000000000000000d0412008010000000000000002000280003f02bf004000400010000104bd1b80538a528a528952895289528a52aa5aca5aeb5a0c5bcb524e5b168df684b574b574b57416855795b8a5d8adf8b518b6f8b518b618b639b619b6f8b5f8adf8b518b618be38be38be59be59c659be59be38be59c659c659c659c659c639be39be18be19b619b6f8b5f8add8add8add8a5d8a5d8a5d8a5d8a5f8a5f9adf8adf8adf8ad895289528952895289528a52aa52ca5aaa5aca520c5b0d535274f684167d17853785578d7795b7a5d8adf8b5f8b518be18be18be39be39be18b6f8b518b618b618b618be38be39be39be39be39be39be38be38be39be59c639be39be39be18be19b619b618b66cf8ad804ff9ad8a5289528952694a694a89528a52aa52aa526952cb52ec52af63d584578d168577957795779d979dd8adf8b5f8b518be18be39be39be39be39be18b618b618be18b618b618b618b618b618b618be18be19be18be39be59be38be18be39be18b618b619b619b618b6f8b518b618b618b619b618b618b619b619b619b618b619b6aa52aa528a528a528952895289528952aa528a528a52cb522d5b11743695b8a5989d979d979d97a5d7adf8b5f8b518b618be18be39be39be39be18be18be18be18b618b618b6f8b5f8b5f8b5f8b5f8b518b618b619be39be18be18b606800318b618b618b618b619b619b618b618b618b618b618b619b6aa5aaa528a528a528a528952895289528952aa5a8a52aa52cb522d5b317c369dd8a5b8a597a5d8add8adf8b518b6069338be18be18b618b618b6f8b5f8b5d8add8add8add8b5d8b5f8b5f8b518b618b619b639b619b66c18b68718be18be18be19b6aa5aaa52aa52068057895289528a52cb5aeb5aec52af6b97a5b8a597a5f8adf8b5f8b518b618b618b618be18be18be18be18be18be18b618b6f8b5f8b5d8add8add8add8add8add8add8adf8b5f8b5f8b5f8adf8adf8adf8adf8b5f8b518b618b618b618b618b618be18be18be18be19be18be18be18b6aa52aa52aa52aa52aa528a5289528952895289528a5a6952aa52aa5aaa522d639284d7ad97a5d8adf8b5f8b5f8b5f8b518b618b618b618b618b618be18be18b618b6f8b5d8b5d8add8add8add8adb8adb8adb8add8adf8add8ad779d569597a5d8adb8add8adf8adf8b518b618b618b618b618b618be18be18be18be18b6f8b568aa5202800c895289528a528952aa52aa526e63b7adb7adb7add7adf8b5f8b5f8b5f8b518b618b618b6f8b518b618b618b618b6f8b5d8add8add8adb8adb7a597a597a597a597a5d8a5b8a5168df5845795b8a5b7a5b8a5d8adf8adf8b56818b6802af8b5f8b5aa5a8952aa52ca5aaa5a8a528a52aa528a5289528952895289528a52aa528a52cb52f49496adb7add7add8add8add8adf8b5f8b5f8b5f8b5f8b5f8b518bef8b518b6f8b5f7add8add8adb7a597a597a5b8a598a5979d779d5795168df684168d3695779db8a5d8a5f8adf8adf8adf8adf8adf8b518b618b6f8b5f8b5d8adb8adca5aa95a8952aa52aa52aa528a52895207f4fa03aa528a4a2d5b149db7ad96add8add8b5f8b5d8b5d7add7adf8b5d7b5d7b5f8b5f8b518b618b6f7add7add7add8add8a5b8a598a5b8a5b8a5779d378d1685f6841685368d368d7795989db8a5d8a5d8a5d8a5b8a5d8add8add8add8add8add8adb8a5ca5aca5aaa5a895289528a528a528952aa528a528a528952895289528a52cb5aaa52ab52f07bb7add7b5d7b596a5b7adb7adf7b5d7b5b6adf8b5d7b5f8b518b6f7b5f7b5d7adb7a597a5b7a5b7a5979d779d979d989d7895378d168517851785378d378d378d578d7795979d979d779d979d979db7a5b8a5b8a5b8a5b8a5b8a5ca5aeb62ca5a89528952895289528a528a52aa528a52694a694a694a8952aa528a4aaa522c63359dd7b5d7b5d7b5b7add7b5d7b5d7b5d7b5d7b5d7add8add7adf8b5f8b5f8adb7adb7a5b7a5979d779d3695168d378d5895578d1785178517851785168516851685368d578d5795569557955795779d779d979d989d989d5795aa5aca5aca5aaa5aaa5a8952695289528952aa52aa528952694a894a69528952aa52aa52cb526e6b55a596ad349d149dd394928cb28c96add7b5f8b5f8b5f8b5d8add8add8add8adb8a5779d57953695168df5841685578d378d1785f77cf67cf67cf67cf67c168516853685378d368d568d368d368d5795579577951685746caa52aa52aa5aaa5aaa5a895269528952694aaa52aa528a5289528952895289528a528952cb5a8a4aeb5a2c5beb5aaa52aa528a4aaa52ae73d7b5f8b5d8add7adb7adb7add8adf9add8a5579d168d168d168d368d378d378d1785177df67cd674d674f77c1785378537853785378d378d5795578d368d368d368db574f35bf35baa528a52aa52aa5a8952895289528a5289528952aa52aa528952695289528952694aaa528a528a528a52aa52cb52aa5289528a528a4aeb5ab7b5d7b5d8b5d8ad97ad97a5b8add9adb8a55795168d168d168d378d378d1785177df67cd674b674956cd674177d3785588d788d788d778d78957795578d378d746cb24bb24bb24b8a52aa52aa5aaa5a89528952aa5aca5aaa528952aa52aa5a8952694a69528952895269528952895289528a52cb5aca52aa528a52894acb5a5184928cd394159d569d369536953695168df684f684178d378d378d1685f67cd67cb674956cb66c956cb674f77c37855885588d588d578d578d778d578d956c1354b24b924bb24b8a528a52aa52aa5aaa5aaa5aca5a0b632b63aa5aaa52895289526952694a69528952694a89528a5289528a52ca5aaa52eb5acb5aaa52aa52cb52aa52cb526e63b484168db57cd57cd67cb674d674177d177df684d67cb67cb674956c9664b664966cd674177d17853785378d578d7895578d167d54645464545c135cf253d2538a5289528a52aa52aa5aaa5aca5aeb62eb62ea5aca5aaa5289528952895289526952694a89528a528a52aa5acb5aaa52cb5aeb5aca5a8a528a528a528a52cb528f63737c73743364345c54649564d66cb674b674b574b574b674b66cb66cb66cd66cd674d674d67cf67cf67c1685378db574335413541354335c54643364f35b8952695269528a52aa52aa5aca5aca5aca5aeb62eb62ca5aaa528a528a5289526952694a8952694a8952ca5aeb5aaa52aa52eb5acb5a8a52aa52aa528a528a520c5b8f636f5b9053f253335c345c755c7664966c756c756c756c756c7564956cb674b674d674d67cd67cd67cb574f35bd24bf253f24bd24b135454643464135c895269526952895289528a52aa52aa5aca5aca5aca5aaa5aca5a8a52aa526952895289528952694a6952aa52cb5aaa528a52aa52aa52aa52ca5aca5aaa52cb52cb5a4d63ec52cc4a2e4bd153f3531354145c555c75647564756c756c74647464956cb674d674d67cf67c756c924b92439143b24bd24bd24bf353f353f35bf35b89526952695269528952895289528952aa5aaa5aaa5aaa52eb62aa5aca5a8952aa528a5289526952694a8a52aa52aa528952895289528a52aa52aa52aa52eb5a0c634d63ec5aab52cb522e538f53d15bf3531454145415543554555c54647564956cb674d67c9574d35372439243b24bb24bb243b24bd34bd34bd34bb34bd353895289528952695269526952695289528952aa52ca5a8a52ca5aca5a0b63ca5aaa528a5289528952694a694a8952aa5269528952694a694a8952aa52aa52cb5aeb5aca5a8952aa52aa52aa4aab4a0d4b9153f3531454f44bf4531454345c5464956cd67454647243513b724392439243f34bb24bb243d34bd34bb34bb24bb24ba952895289528952695269526952695269528a52aa5a89528a52ca5aeb62eb62aa5aaa52895289528952695269528a5269528952694a694a694a8a52aa52aa528a52aa52aa5aca5a8952a9528a4a8a4acc4a6f53d25bf353f353f3531454345c13549243924392437243724371437143d34bb2439243b24bb34bb34b924b924baa52a9528952895289528952695269528a526952895289526952aa52aa52eb62eb5aca5aaa5289528a528a528a52aa5289526952694a694a694a89528a52aa52aa526952aa5a0b63ca62ca5aaa52aa528a4a0d536f534f4b2f4b504b714bef2acf223133723b9243924392437143924371439243b243b24bb24b924b924b9243aa528952895289528a528952695269528a528952895289528952aa5aca5aca5a0b63ca5a8952ca5aaa5aaa526952aa5289526952694a694a6952695289528a528a52aa52aa52aa52ca5acb5aaa528a52ab52ab4aab4aab4aab4a8829c500a911ae2a10339243513b5133b243723b713b303b303b303b303b303b513b303b5143aa52895289528a528a528952895289526952068055eb5aeb62aa5aaa5a8a52aa528a528a5269528952895289526952694a694a6952895289528a5289528952aa52cb5aca5aaa528a52aa528a4a8629820841004100c4084c22513b91433033513b91437143503bef32cf2aef32ef32ef320f33ef3210338952895289528a528a528a528952895289528952895269528952aa52ca5aca5aeb5aca5aeb5aaa5a8a528952aa5a895289528952895289526952694a6952895289528952695269528952aa52aa5aaa52494a652982082000200040082008610868115043b14bb24bd24b7143914371437143303b503b513b513b513b513b303369526952895289520880176952695289528a52aa5aaa5aaa5aca5a895289528952aa5a8a526952694a89528a52695269528952895289528952695269528a52494a24294008400861102008000840104010410826110f43b153f25b5364135c335c1354d24b714391439243713b513b513b303369526952695269895202801469528952aa5aaa5aaa5acb5acb5aaa5a6952aa5aaa5a89528952895289528952895269528952895289528952e739042120082008200820088118811040086108410842000611ac3a905bd15bf25b125c5364135c135cb253d353b24b7143513b3133102b695269526b895204800fca5aaa5aca5a2c6beb62aa5289528952aa52aa52895269528a52aa52aa528952284a45316110000000000000200820080008601081106108610862086308a30826196b428f5bf16312641264125c135cd253d353924b313b1033f02af022728952800daa52aa5a0b630b63ca5aaa5289528a528952895269528a528a52e741032161082000200000000000000000002000000040084108410841084108821062080100c3104a3a8f5b116411641264f25bd253b25351431033102bf0221080128a52895289528952aa5aca5a0b63eb620b63aa5a895269526952c63903216110c218e318821020000000000000000000000000000000410021002000200020084110611041082100c310a7298b424e53b05b9053915371431033f02af022d01ad01a69520c8013aa52aa528952895289528952aa5aaa5aeb620b630b63aa5a8531a11060102008400840086110a210c21881100000000020080000000000000000000020000000200020002008611020082008610861086100a30805116b3a2e43ee3a8d22af226e126f0a8f0a0e8012aa5a8a52895289528952aa520742a53944292329e2202329811060104008400861108110a218c218c21861100000400861080000000000002000200000000000200020002008200820084010400840086108a208a3086719a8198809a909aa090c0a4d12088042aa52895289528952895289522842c6396531c220a218401040086010c218442923292329e320e2206110400861108110a118a118c218a218610861086108200800002000200020000000000000002000210041084108410820084108410841086108c3182519c308a3008300c4000509694a694a0842e739e739e7410742a539853165312429c21840104008601040086110401040106010400820086010e2200321e2208539a5392429e320601061108110811081108110a21861102008610800000000078039420841082108200841084008400841106110c218611061086208820882100000000000000000200020084008400860104010401040104008400840082008611061106110611060104008401081108118e2206431232944312329401081104008611040086110c2188210400840080000000000000000000020002000200021002100210020002000200020082008401020088118401060086110601040080000000000000000000020002008200840084008069c200820086010601081106010811060106010c218c220e2200329a1188118611061104008410861106110c218a21820000000000000000000692000801b0000000000000000000060104008600860086010401000000000000000000000000000002000200820084008401040084010401040084008400860104010611040106010401081188118a11823296431e220e220601081184008400840084008a218c218611000000000000000002000200840082008088028400040004108410061084100610840000000000020000000000000000000000020082008200840082008400840104010400820084008400861104010611081186110a118811881186431a5392329c218a218611000000000400861108110e3182008000000000000200040084008400800002000000000000000000000000000000020000000200062084100820841006a000001800720084008401040106010401020082008400840086010811061106010601060106010a1180329232903290321a21820082008000040084108c218c2182008000000002000200860086008200820086a00008421004108410841080a800b000820082008400840106110601040104008400820084008601060106110601040102008401060108118a1184431c218200800002008200840086110c318c2184008610840086108200020088110611020082008200869000082200820086c0000800a000820084010611081106110401020084008400840084010611061106010401020082008601081188110c218c218200800080000400820088110c318611040084008611020004008400841106110400820002000088100080f8008200840108110811040082008401040102008400820084008401040102008200840108110401003218531c21840082008200820084008811061100000200020086110a110032903210329c218611040086900008120006d00000280102008601061104008200840084008200840104010200820082008200800002008400881188118e320a11860108110000040082008400881102008000000006110a218a1186010801060088110a1184008200020000000000000002000200020000f800c0008200820084010601040102008200820086110611040102008200820082008200820088118401081188118a218232961106110200840088110a218400800002000400840084008200820086008a110600820002000200013801000002008200820084008601060102008200840084110410840082008000000002000200820084008601080108118c218e32081182008200820086110a218a2184008000020000000200820080000200841086108200820002000000000000000118011200020084008200840106010400820084008200841084108410840082008200820082008200840106010c2180321c218c2206110400820084010611003216110000000000000210800000000200840086110000020082008200800000000000000000881200807892000200040086110200820082008400820086940088007200840108110a1180321a21803296110000000086110c218e320000800000000000020002000000040084008400800002008400820082000200820080000000000000000000000002008000800080a804b4008400820082008200840084008400840084008401040082008200820082008400860108110e220a118e320e320601020082008a21861100000200820000000200000002008a218a218811061102008200820084008200820002008000000000000000020082008200820080000000000000000000000000000200020082000200840084008200820084008200840084008601060104010200800080000000020082008200881188110c220e320e220200840106010c218200800000000000000002000400861084108611081104008200820082008076c000001800f0000200040084008200820082008200840084008400861106010400800082008200820082008200860106110c220c2204431c220a1186010a2186010611020000000200041084008400840086110811082108110400820082000200820000881200869000001800c200840084008200820080000200820084008401040104008200800000000000000002008000820088118e220e220c2188118c2186010a118c218400800002000200040088110811081106110a218c218a2186110200820006900000181200807800f200020002000200840084008200820082008200840084008400840104010410820084008400861102008200860108118a118c220e2200321c2188118601061082008400840082008400820082008400840086110a218a218611020082008078520002008200820082008680000098003200840086110611061106110400861102008200820084010e2206431853903214329a118600881106108811081104008000000000000000000000000611082106110400841080667200808800b200840084008400820082008400820082008200861108110a21861102008401040084010200860104008a11803292329a5392329c21861104008610840084008811041080000000000000000200840084108611061106800000680120008000000000000000000000000200820084008400820082008200820082008200820088110811081106010400840084010401040106010401040108118c118c2180221811061100000200800002008611000000000000000000000200820082008200808852000200820082008200869000001812008088001400861106110811081108110601040102008601060106010a118a1188010a11881104008400800000000400800000000000020000000000000004008611061102008690000038120080a6c20089e40106010611060104008601060108110a118a11880106010601061104429a11800002008200820082000200820000000200840086110611020082000088e200020082008200800000000200000000000000000000000000000000880024008200800000000200860108110811840106010401040108118c218a11860106010c218a539a539c218200820084008400820082008400840084008400840082008200869000080292000200820082008200820082008200000000000000000000000000000002008200820084008200820082008200820082008200840084010611040106010401020086010c218e220a1186110a118c2206431a639032100002008200020082008200840086110410840082008200800080000000000000000000020002000000000002000200820082008200820082008200008814008089f200820084010400860106110401040088118c220c218401060108110a21865310742a2180000000020082008000000006110611020082008200820082008690000068420082008000000006920088002400820082008200840084008611081106110401061106110400840108118a2184008200861106010c218c639652920080000200020002000200840082008200840084008136f20089c4010601061106110a21840104010811860104008601081104010200800086010a218c2182429811020080000200081108110400800002008400280007f02bf004000400010000104630e9ff9adb8a5989d779d7795989db89d989d979d989dd57c336433643464345cf353723b5133112bf022f11ad01ab00a900a7002700270027002700270025002c00d4f0280034f024f024f024f02d8add8a5989d779d7795989d989d779557951685746c546454643464135cd3539243713b3133312b112bf122d11ab012900a70027002700270026f026f0200019ef9adf9adb8a5989d989d9895779557951685746c946c746c54643364135cd253b24b9243723b723b5233322bf11ad112900a70026f026f0270026f0260024f02019c19aed8a5b89d989d989557951685756c746c746c3364135cf25bf25bf25bd353d24bb2439243723b52331123d01a6f0a6f026f027002700260034f029d19b6f9adb8a5979d9895579516853364336433641364f25bd25bd25bd25bf25bd25bd253b24b9243924352331123f01a900a8f026f026f026f0200038000f9add8a5979d77955795368d135c135cf253f25bf25bf25bd25bd25bd25bd25bd25bb153914b914b9243723b312b111bd012b00a8f026f024f024f024f026f0200008000f8adb8a5979d979d578d5464f353d253f253f253f25b13641364f263f25bd25bd15bb153b253b24bb243723b312bf01ad012b00a8f026f026f024f024f02500200009ed8adb7a5979d989d9574335cf353b24bd253d253d25b135c336413641364f263d25bf25bd25bd253b24b723b312bd01a8f0a8f026f026f026f02700260024f02800097a577955695b5747464135cd253b24bd253f3533364546c546c136413641364f25bf25bd253b24b71435133f022af128f028f028f026f02700270025002500200008001979d368d536c546454641354b24b7143b24bd253135c546454641364135c135cf25bd25bb24b9143513b302bd01a8f0a8f028f0290029002700270025002500250021f8000779d746c53645464335cd253914b7143914b924bd253135c135cf25bd253f25bf253d253924b7143513b3133f022af12b00ab00a900290027002700250024f02000080009474546433643364d253914b71437143914b914bb14bb253b253914b914b914b914b924391437243723b52331123f01af112d10a90026f0250024f025002500260004f029b3364135cf25bd253b24bb24bb24bb24bb253b253b14bb14b914b71435143503b303b513b513b513b5133313311231123f11ab00a6f0260054f029af35bb253b24bb24bb24bd353f353d253d253d253b253b24b924b7143503b10331033303310331033f02af02af122f122b012900a60064f029db253914b914b914bb24bd253d253b24bd253d253d253b24bb24b7143513b513b513351333033f02ad022d022d022f122b012900a4f024f026f0200039b914bb24bd253d253b24bd253d253d253b253d253d253b24b92439243924392439243723b5133102bd022d022f122f122f11ab0126f0260054f029cb253b24b924bb253d253f353d253b24bb253d253b24bb24bb243924392439243723b723b5233312bf022d022f01af11af11ad012900a6f0200049bd253d253b253d253d253f353d253d253d253b24bb24bb24b92439243513b51333133112bf02ad022b01ab01ad01af11ad012b00a8f0200059b135cf353f353f353f353f35bf353d353b24bb24b92437243723b5133102bcf22d022d022b01ab01ab01aaf12b012d0128f0a8f026f0260054f020199135cf353f353f353d353d24bb24b924b9243513b51333133102bf02ad022d022d01ad01ad01ad01ab0128f0a8f0a6f026f0200069df353d353d24bb24bb24b924b924372437243513b3133102b112b112b112b312b1123f01ab012d012d012b0128f0a6f026f026f026f026f026f02000399b24bb24b924371437143713b513b513b513b5133312bf02af022f022112311231123d012900a6f0a6f0a8f026f026f026f02d52000010000008095924371437143713b513b513b313351333133312b1023d01ab01ab012b012d012900a6f024f024f024f02402945000000000093724372437243723b723b513b3133112b312b312b322b1123f11ab0128f0a6f0a6f026f026f02402c9301000000008f513b513b31333133102bf02af022d02211231123322332231223d0128f0a60114f028e1033f02acf2acf22d022d022d022d01ad01ad01af11af11af112b00ad031e008010000000000008e3133102bd022d022f022f022f122f11ad11ad112d112d112b00a700260124f02028bf02a1023312b1123f11af01af11af112d10a900a7002d0321f00010000000000008cf02af022f022312b522b522b111bd012b012b00a900a70024033030000000000008dd022d0221023512b522b3223f11ab0126f02700270027002700260134f028faf1aaf1ad02210231123d01a8f0a6f024f026f026f026f024f024f024f02d0326000010000000000008dd01ad01ad01ab00a6f024f024f024f024f022e022f024f02500260114f028f8f0a8f0ab012b012900a4f026f024f024f024f024f024f022f024f025002d0301f00010000000000008e4d124d0a8e128f128f0a2e024f024f024f024f024e022e022e022f0260124f0290050906016801cb094e0a4e022f024f024f022f022f022f022f022e022e022e02d601000100000000008962088200a4000701cc012e0a0e022e022f0208000f92611082108400a5002901ed010d022f022f022f022f024f024f024f022f024e024e024e02402d010000000000884010410863006400e700ec110d0a2e020660124f028b4108410862006300e600eb19ec09ed010e022f022f02d0346000030000000000008d210021004108420083008811cb110d0a0e020f022f022f022f024032030000000000009440082008200820006208e510a9110c12ed012e022f022f022f022e020e022f022f02500250025002000c9320004008400840084008a208261189090c122e0a2e020e020e022f022e022f024f0250025002600d4f02932008400820082008400881088208a40007018a010e022f020f020f020f020e020f022f022f02402d0300000000209020002000200040086008410841006300e700cc012e0a0f020f022f022f022f02402e1300000000009320002100410041004008400840084108210063002801ec090e0a0e020e02ee010e020e022e02d60100030000000000924108410861106110410861086200c5086811cb11cc09ed090d0a0d0a0d0a0d0a2e0a2e02402a010000000000984008200800002008410861106108200841082008210042006300a5002701aa11ec11cb09cb010d0a4e0a2e022e022f02000a9e2008200820084108410841082008200820082008410862006300a500c600a500c6004801eb090c0a0d022e024f024f024f022f022f022f022f022f0200009b00002000400820000000200020084008200020084108610861086208620862004100420062008308c4002601aa092d0a4e022e022f0260054f029f2000200020004008200820000000000000002000200840084008400840082000400820084008400861008200c5002801ec012d024f022f022e024f022f0200039b40086108811061082000200020002000200020082008200820002000400040004100410840002100430064000701cb092e0a0d022e024022030000000080034008200841088110a2108210410820004008400840084008400840082008200040004000410041004108410842086200630027010c120d0a2e024e022e024e022f022f022f021d80082008200820084008611082106108200041084008400820002000200020002000200020002100410041004008200840084100a400eb112e0a2e022e022e020e022e022f022f022f022f022f024e024e02430100009f00000000000000004008811081106108400820082000200020002000200020002008200821002100210020082008200840006200cb090e0a0e020e022f0207842f022e022f022f02169f20082008000000002008400861106110200820002000200020002000200020082008200821004200410040082008200840006200ca09ed010f020f020f026c2f021589611040082008200820082000200840082000069140082008200821002100400040082008200840008300cb09cd012f022f020f020f026d2f021480008110811081106110400861104008200820000000200020002000200020002000200021002100400820082008200821008300ca19ec090d020e022e020e020e0206852e022f024f022f022f02744f02904108811061104008200820086110821061084008400840084108200020000000088f41088300681989098a01cb01ec090d0a0d020e020e020e022e022f024f02692f021080076110a218821081106110000000004008400840084008400840082008200020002000200021002100200820082108210841084100e510e608e60047098811ca110c120d0aed010d020e020e020e0219800c400841086110c318e320400800002008200820082000200020002000200020002000000020002000200020002100210020002000620883086200c408e5102711ca11cb11eb11ec090d0a0d020e022e022e022f022f024f021480112008200820088110c318811000002008200820082008200820082008000000000000000000002000200020002000200040084000200041082000610862088308e508060127014801aa09ec090d0a0d022e022e022f022f022f022f022f022f022f020f800f40084008200820006110a21840080000200820084008400841084008200800000000000000000000200020002000400040084008000020082008410840084108420062008300c5004801cb110c0aed010e020e022e022e022e022e022e0211800c00000000200800004008a210610820082000200840084008400840084008200800002000200020002000200020082008200820080000200840084008410841084008410862008300e5006809cb090d0a0d020e020e020e02149120000000200820084008410820082008200820082000000020004008400840082000099b20082108410820002000200000082008400841004200a4004809ca11eb11ec09ec09ec090d0a0d0a0d0a2e022e024f022f022f022f0207844f024f024f024f0280028000bf02bf0040004000100001041900c02c4f02844f024f024f024f02f0bc0f844f024f024f024f02')


#RDPClientQt.onUpdate(self, destLeft, destTop, destRight, destBottom, width, height, bitsPerPixel, isCompress, data)
#image = RDPBitmapToQtImage(width, height, bitsPerPixel, isCompress, data)


#print(reqdata)
x = TS_FP_UPDATE_PDU.from_bytes(reqdata, False)
#print(x)
print()
for a in x.fpOutputUpdates.update.rectangles:
	print(a)
	print()
	input()
	image = RDPBitmapToQtImage(a.width, a.height, a.bitsPerPixel, True, a.bitmapDataStream)
	print(image)

	image.save(r"hehe.jpg",format = 'jpeg')
	input()