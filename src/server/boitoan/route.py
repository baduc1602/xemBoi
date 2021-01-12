# Thu vien standard

# ThirdParty
from flask import Blueprint, jsonify, request, render_template

# Thu vien ben trong

# Blueprint
boi = Blueprint("phongthuy", __name__)

# app decorator
@boi.route('/phongthuy/', methods=('GET', 'POST'))
def boi_toan():
    if request.method == 'POST':
        res = _post_boi_toan(request)
    elif request.method == 'GET':
        res = _get_boi_toan(request)

    return render_template("result.html", res=res)


# Module: function noi bo nen them _(protect), __(private)
def _post_boi_toan(req):
    # Nhận thông tin năm và xử lý
    """body = req.json
    print("body = {}".format(body))

    year_of_man = body.get("man")
    year_of_woman = body.get("woman")"""
    year_of_man = req.form["man"]
    year_of_woman = req.form["woman"]
    print("year_of_man = {}".format(year_of_man))
    print("year_of_woman = {}".format(year_of_woman))

    # Xem ngũ hành
    nam_mang = _ngu_hanh(year_of_man)
    nu_mang = _ngu_hanh(year_of_woman)
    print("Nam Mang:", nam_mang)
    print("Nu mang:", nu_mang)

    # Xem hợp tuổi

    hop = _hop_tuoi(nam_mang, nu_mang)
    print("Hai nguoi", hop)

    return nam_mang, nu_mang, hop


def _get_boi_toan(req):
    return "OK"


# Tính ngũ hành theo https://phongthuyhomang.vn/cach-tinh-thien-can-dia-chi-va-ngu-hanh-nam-sinh-cuc-nhanh/
def _ngu_hanh(year):
    """
    tính toán ngũ hành theo năm
    :param year: (str) năm
    :return:
    """
    # Kiểm tra type
    if type(year) not in (str, ):
        raise ValueError("year() is not string ".format(year))

    # Chuyển dạng str của year sang int
    year = int(year)

    # Tính thiên can và can
    can = __tinh_thien_can(year)

    # Tính địa chi và chi
    chi = __tinh_chi(year)

    # Tính giá trị hành
    hanh = can + chi
    if hanh > 5:
        hanh = hanh - 5

    hanh_mang_table = {
        1: "KIM",
        2: "THUY",
        3: "HOA",
        4: "THO",
        5: "MOC"
    }
    mang = hanh_mang_table[hanh]

    return mang


def __tinh_thien_can(year):
    """

    :param year:
    :return:
    """
    thien_can = year % 10
    thien_can_table = {
        5: 1, 4: 1,
        6: 2, 7: 2,
        8: 3, 9: 3,
        0: 4, 1: 4,
        2: 5, 3: 5
    }
    can = thien_can_table[thien_can]
    return can


def __tinh_chi(year):
    """

    :param year:
    :return:
    """
    dia_chi = year % 12
    dia_chi_table = {
        4: 0, 5: 0, 10: 0, 11: 0,
        6: 1, 7: 1,0: 1, 1: 1,
        8: 2, 9: 2, 2: 2, 3: 2
    }
    chi = dia_chi_table[dia_chi]
    return chi


def _hop_tuoi(nam, nu):
    if nam == nu:
        tuoi = "Khong hop cung khong khac"
    else:
        if nam == "KIM":
            if nu == "THUY" or nu == "THO":
                tuoi = "Hop nhau"
            if nu == "MOC" or nu == "HOA":
                tuoi = "Khac nhau"
        elif nam == "THUY":
            if nu == "KIM" or nu == "MOC":
                tuoi = "Hop nhau"
            if nu == "HOA" or nu == "THO":
                tuoi = "Khac nhau"
        elif nam == "MOC":
            if nu == "HOA" or nu == "THUY":
                tuoi = "Hop nhau"
            if nu == "KIM" or nu == "THO":
                tuoi = "Khac nhau"
        elif nam == "HOA":
            if nu == "THO" or nu == "MOC":
                tuoi = "Hop nhau"
            if nu == "KIM" or nu == "THUY":
                tuoi = "Khac nhau"
        else:
            if nu == "HOA" or nu == "KIM":
                tuoi = "Hop nhau"
            if nu == "THUY" or nu == "MOC":
                tuoi = "Khac nhau"
    return tuoi

