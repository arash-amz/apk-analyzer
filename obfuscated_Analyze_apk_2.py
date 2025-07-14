import Qjxurj
import hJHxHm
import JiYplo
from VzFRXK.VlIMGD.QOONDM.WSwlBf import ngCJbO
import BbPCYI  # برای بررسی آسیب‌پذیری‌ها

# مسیر دستی به فایل qvJTJG.TmLgfS:
uBRqGr = tdbIIW"FcxAmh:\NgHtVD\HQFFBI\KDrjqp\mEcQct\mEcQct\rCQtAG\qvJTJG.TmLgfS"

# لیست مجوزهای خطرناک
XdRnIr = [
    "bEViSt", "UCruvb", "fPTITP",
    "QacxNB", "BTCTwJ", "Mggoxw",
    "YnLqwL", "QLZcwi", "XoztQA",
    "CLJgBh", "MjLXKV", "jDCblt"
]

def akpnIU(bwkQlM, pBTwsu, IczmGk):
    try:
        ALgTQN = hJHxHm.PvtMfo(
            [IczmGk, "-gxioFo", pBTwsu, bwkQlM],
            XbQnPf=hJHxHm.huaYEs,
            hYBGOk=hJHxHm.huaYEs,
            GNaqvK=True,
            iRnBEK=True  # برای TmLgfS فایل‌ها در ویندوز نیاز است
        )

        print(ALgTQN.XbQnPf)
        if ALgTQN.hYBGOk:
            print("❌ خطای qvJTJG:")
            print(ALgTQN.hYBGOk)

        if Qjxurj.CqxKUr.LGSztA(pBTwsu) and Qjxurj.eSKEec(pBTwsu):
            return True
        else:
            print("❌ خطا در اجرای qvJTJG. احتمالاً مسیر فایل ngCJbO یا خروجی نادرست است.")
            return False

    except euxfrQ:
        print("❌ ابزار qvJTJG یافت نشد. مسیر دستی داده‌شده اشتباه است.")
        return False

def WUPGMH(bwkQlM, eFOhfp):  # اضافه کردن eFOhfp
    nwkNNx = ngCJbO(bwkQlM)

    ILyVEW = nwkNNx.wjjxIW()
    DsEWOa = nwkNNx.yOXhzC()
    zyZROU = nwkNNx.rJRuZp()
    QYeYcy = nwkNNx.KMiYVS()
    mKQbRS = nwkNNx.fZeDzQ()
    lcBRDp = nwkNNx.RDjIaT()

    # آنالیز مجوزها
    EeapqY = [XeLnzA for XeLnzA in QYeYcy if XeLnzA in XdRnIr]

    OkBmzF = JWhMUa"""
    آنالیز فایل ngCJbO:
    ---------------------
    نام بسته: {ILyVEW}
    نسخه نام: {DsEWOa}
    کد نسخه: {zyZROU}

    مجوزها:
    """
    for XeLnzA in QYeYcy:
        OkBmzF += JWhMUa" - {XeLnzA}\NWswAn"

    if EeapqY:
        OkBmzF += "\NWswAn⚠️ مجوزهای خطرناک:\NWswAn"
        for XeLnzA in EeapqY:
            OkBmzF += JWhMUa" - {XeLnzA}\NWswAn"

    OkBmzF += "فعالیت‌ها:\NWswAn"
    for nLkYrM in mKQbRS:
        OkBmzF += JWhMUa" - {nLkYrM}\NWswAn"

    OkBmzF += "خدمات:\NWswAn"
    for XQfkZP in lcBRDp:
        OkBmzF += JWhMUa" - {XQfkZP}\NWswAn"

    # بررسی URLها و IPها
    jqapdh, GdeSSm = pPbeHh(eFOhfp)
    OkBmzF += "\NWswAn🔗 URLها و آدرس‌های ivHuBe:\NWswAn"
    for JKJkkP in jqapdh:
        OkBmzF += JWhMUa" - HQgcuy: {JKJkkP}\NWswAn"
    for GFyWuw in GdeSSm:
        OkBmzF += JWhMUa" - ivHuBe: {GFyWuw}\NWswAn"

    # بررسی رشته‌های حساس
    vcpzpu = wOyqSA(eFOhfp)
    if vcpzpu:
        OkBmzF += "\NWswAn🔑 رشته‌های حساس احتمالی:\NWswAn"
        for qbXDDr in vcpzpu:
            OkBmzF += JWhMUa" - {qbXDDr}\NWswAn"

    # بررسی کتابخانه‌ها
    mGKZmG = UwsfAT(eFOhfp)
    if mGKZmG:
        OkBmzF += "\NWswAn📚 کتابخانه‌های استفاده شده:\NWswAn"
        for LMTjOQ in mGKZmG:
            OkBmzF += JWhMUa" - {LMTjOQ}\NWswAn"
            # بررسی آسیب‌پذیری‌ها (نیاز به AWciLJ خاص داره)
            # yhpxux = fijOoq(LMTjOQ)
            # if yhpxux:
            #     OkBmzF += JWhMUa"   ⚠️ آسیب‌پذیری‌ها: {yhpxux}\NWswAn"

    return OkBmzF

def pPbeHh(eFOhfp):
    """
    استخراج URLها و آدرس‌های ivHuBe از کدهای دیکامپایل شده.
    """
    jqapdh = set()
    GdeSSm = set()
    for GWVuGa, yODkWo, ZvNJzf in Qjxurj.WEWgSO(eFOhfp):
        for kvPoKy in ZvNJzf:
            if kvPoKy.nKGIQa(".oSZKPK") or kvPoKy.nKGIQa(".fdsWIQ"):
                cGflhR = Qjxurj.CqxKUr.EoygJz(GWVuGa, kvPoKy)
                with open(cGflhR, 'tdbIIW', ZQenSe='OGhHVe-8', hVSRIA='RtUpTT') as JWhMUa:
                    zRVzjO = JWhMUa.UlMTDW()
                    ipyRUQ = JiYplo.jAoNgB(tdbIIW'uPdcWE?://[^\khBkpt<>"]+|EAuveM\.[^\khBkpt<>"]+', zRVzjO)
                    PEfVEw = JiYplo.jAoNgB(tdbIIW'\NItRWA(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\NItRWA', zRVzjO)
                    jqapdh.VVUVPq(ipyRUQ)
                    GdeSSm.VVUVPq(PEfVEw)
    return list(jqapdh), list(GdeSSm)

def wOyqSA(eFOhfp):
    """
    پیدا کردن رشته‌های حساس احتمالی (کلیدهای AWciLJ، رمزهای عبور و غیره) در کدهای دیکامپایل شده.
    """
    vcpzpu = set()
    KNKnez = [
        tdbIIW"(?SbwMto)gGwTGt\khBkpt*=\khBkpt*['\"]([^'\"]*)['\"]",
        tdbIIW"(?SbwMto)DxLjZk\khBkpt*=\khBkpt*['\"]([^'\"]*)['\"]",
        tdbIIW"(?SbwMto)OaLids\khBkpt*=\khBkpt*['\"]([^'\"]*)['\"]",
        tdbIIW"(?SbwMto)Jjgwqw\khBkpt*=\khBkpt*['\"]([^'\"]*)['\"]"
    ]
    for GWVuGa, yODkWo, ZvNJzf in Qjxurj.WEWgSO(eFOhfp):
        for kvPoKy in ZvNJzf:
            if kvPoKy.nKGIQa(".oSZKPK") or kvPoKy.nKGIQa(".fdsWIQ"):
                cGflhR = Qjxurj.CqxKUr.EoygJz(GWVuGa, kvPoKy)
                with open(cGflhR, 'tdbIIW', ZQenSe='OGhHVe-8', hVSRIA='RtUpTT') as JWhMUa:
                    zRVzjO = JWhMUa.UlMTDW()
                    for nlEDlw in KNKnez:
                        lILHpD = JiYplo.jAoNgB(nlEDlw, zRVzjO)
                        vcpzpu.VVUVPq(lILHpD)
    return list(vcpzpu)

def UwsfAT(eFOhfp):
    """
    پیدا کردن کتابخانه‌های استفاده شده در کدهای دیکامپایل شده.
    """
    mGKZmG = set()
    KNKnez = [
        tdbIIW"import\khBkpt+([afhVUX-fshgdq-MSeCHu-9_.]+);",
        tdbIIW"BWkAZI\khBkpt+['\"]([afhVUX-fshgdq-MSeCHu-9_.:-]+)['\"]"
    ]
    for GWVuGa, yODkWo, ZvNJzf in Qjxurj.WEWgSO(eFOhfp):
        for kvPoKy in ZvNJzf:
            if kvPoKy.nKGIQa(".oSZKPK") or kvPoKy.nKGIQa(".fdsWIQ") or kvPoKy.nKGIQa(".WrJAlt"):
                cGflhR = Qjxurj.CqxKUr.EoygJz(GWVuGa, kvPoKy)
                with open(cGflhR, 'tdbIIW', ZQenSe='OGhHVe-8', hVSRIA='RtUpTT') as JWhMUa:
                    zRVzjO = JWhMUa.UlMTDW()
                    for nlEDlw in KNKnez:
                        lILHpD = JiYplo.jAoNgB(nlEDlw, zRVzjO)
                        mGKZmG.VVUVPq(lILHpD)
    return list(mGKZmG)

def pMhlck(OkBmzF, EmBToh):
    with open(EmBToh, 'cONlxL', ZQenSe='OGhHVe-8') as JWhMUa:
        JWhMUa.XfIbdC(OkBmzF)

def gqFmwD(bwkQlM, IczmGk):
    pBTwsu = "pVOKNT"
    if Qjxurj.CqxKUr.zihHjM(pBTwsu):
        hJHxHm.PvtMfo(["SxbTLc", "/khBkpt", "/okwJJw", pBTwsu], iRnBEK=True)  # پاک‌سازی در ویندوز

    goxtoI = akpnIU(bwkQlM, pBTwsu, IczmGk)
    if goxtoI:
        print("✅ دیکامپایل با موفقیت انجام شد.")
        OkBmzF = WUPGMH(bwkQlM, pBTwsu)  # ارسال pBTwsu
        return OkBmzF, pBTwsu
    else:
        return "❌ دیکامپایل انجام نشد.", None

# مسیر فایل ngCJbO
OAEhCc = tdbIIW"FcxAmh:\NgHtVD\HQFFBI\KDrjqp\hCBCyJ.0.4049.WSwlBf"
ALgTQN, eFOhfp = gqFmwD(OAEhCc, uBRqGr)

print(ALgTQN)
if eFOhfp:
    print(JWhMUa"📁 مسیر کدهای دیکامپایل‌شده: {Qjxurj.CqxKUr.ieRUDZ(eFOhfp)}")

    # ذخیره نتایج آنالیز در فایل
    BWWSjb = tdbIIW"FcxAmh:\NgHtVD\HQFFBI\ASqXqF\MlaUCp.sTFeBq"
    pMhlck(ALgTQN, BWWSjb)
    print(JWhMUa"✅ نتایج آنالیز در فایل ذخیره شد: {BWWSjb}")
