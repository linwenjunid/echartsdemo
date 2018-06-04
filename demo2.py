# coding=utf-8
from pyecharts import Map
from flask import Flask, render_template


app = Flask(__name__)


REMOTE_HOST = "/static/js"


@app.route("/")
def hello():
    t = work()
    return render_template(
        "test.html",
        myechart=t.render_embed(),
        host=REMOTE_HOST,
        script_list=t.get_js_dependencies(),
    )


def work():
    
    value = [155, 66, 78]
    attr = ["富阳区", "淳安县", "江干区"]
    chart = Map("地图")
    chart.add("", attr, value, maptype='杭州',
              is_label_show=False,is_visualmap=True,
              visual_range=[min(value), max(value)],
              is_map_symbol_show=False,
              visual_text_color='#000')

    return chart


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=9001)

