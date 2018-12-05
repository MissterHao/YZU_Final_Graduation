# Author: Hao-Wei Li
from flask import render_template, send_from_directory, redirect, url_for
import os

app = __import__("App.server", fromlist=("server",))
server = app.server

# @server.route("/js/<path:path>")
# def js(path):
#     return send_from_directory("App/templates/js", path)


# @server.route("/vendor/<path:path>")
# def vendor(path):
#     print(path)
#     return send_from_directory("App/templates/vendor", path)


@server.route("/", methods=["GET",])
def main_page():
    # return redirect(url_for("DB_Status"))
    return render_template(
        "index.html",
        path_route=["Home"]
    )
    # return server.send_static_file("index.html")
    # return send_from_directory(os.path.join(root_path, "templates"), "index.html")

@server.route("/index.html", methods=["GET",])
def index_to_mainpage():
    # return redirect(url_for("DB_Status"))
    return redirect(url_for("main_page"))
    # return render_template("index.html")


@server.route("/DB_Status", methods=["GET",])
def DB_Status():
    return render_template(
        "DB_Status.html",
        path_route=["Home", "資料庫狀態"]
    )
    # return server.send_static_file("DB_Status.html")

@server.route("/charts", methods=["GET",])
def charts():
    return render_template(
        "charts.html",
        path_route=["Home", "Charts"],
        cardItems=[
            [{"tw-title":"生質柴油", "title":"biodiesel"}, {"tw-title":"水力發電", "title":"hydro"}, 
            {"tw-title":"乙醇", "title":"ethanol"}, {"tw-title":"地熱", "title":"geothermal"}, {"tw-title":"木板", "title":"Wood-pallets"}],

            [{"tw-title":"潮汐", "title":"tides"}, {"tw-title":"太陽能電視", "title":"solar-TV"}, 
            {"tw-title":"風力發電", "title":"wind-power"}, {"tw-title":"生物燃料", "title":"biofuel"}, {"tw-title":"生物質", "title":"biomass"}]
        ]
    )
    # return server.send_static_file("DB_Status.html")

@server.route("/controlPanel", methods=["GET",])
def controlPanel():
    return render_template(
        "controlPanel.html",            # 繪製的樣板名稱
        path_route=["Home", "控制面板"]  # 開始傳入變數
    )


@server.route("/LDA", methods=["GET",])
def LDA_page():
    return render_template(
        "LDA.html",
        path_route=["Home", "LDA 分析"]
    )

@server.route("/text-relation", methods=["GET",])
def text_relation_page():
    return render_template(
        "text-relation.html",
        path_route=["Home", "文字關係圖"]
    )


# var origin_svg;
# origin_svg = document.getElementById('SVG_for_relation').getBoundingClientRect();
