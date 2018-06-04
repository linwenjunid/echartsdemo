# coding=utf-8
from threading import Thread
import json
import warnings
from db.OPMysql import OPMysql
from db.OPMysql_dict import OPMysql_dict
warnings.filterwarnings("ignore")
from flask import Flask,render_template,jsonify

def scatter3d():
    from pyecharts import Scatter3D,Page,Map,Geo,Style,GeoLines
    import random

    style = Style(
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color='#404a59'
    )

    style_geo = style.add(
        is_label_show=True,
        line_curve=0.2,
        line_opacity=0.6,
        legend_text_color="#eee",
        legend_pos="right",
        geo_effect_symbol="plane",
        geo_effect_symbolsize=15,
        label_color=['#a6c84c', '#ffa022', '#46bee9'],
        label_pos="right",
        label_formatter="{b}",
        label_text_color="#eee",
    )


    page=Page()

    '''
    Scatter3D
    '''

    data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    page.add(scatter3D)

    '''
    Geo
    '''

    data = [('汕头市', 50),('杭州市', 500)]
    chart = Geo("地理坐标系", **style.init_style)
    attr, value = chart.cast(data)
    chart.add("", attr, value, maptype="china", is_visualmap=True,
              is_legend_show=False,
              tooltip_formatter='{b}',
              label_emphasis_textsize=15,
              label_emphasis_pos='right'
              )
    page.add(chart)

    data = [('北京市', 50),('上海市', 500),('伦敦市',100)]
    chart = Geo("地理坐标系", **style.init_style)
    '''
    自定义城市
    '''
    chart.add_coordinate('伦敦市',0.1,51.30)
    attr, value = chart.cast(data)
    chart.add("", attr, value, maptype="world", is_visualmap=True,
              is_legend_show=False,
              tooltip_formatter='{b}',
              label_emphasis_textsize=15,
              label_emphasis_pos='right'
              )
    page.add(chart)

    '''
    GeoLines
    '''

    data_guangzhou = [
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ["广州", "重庆"],
        ["广州", "兰州"],
        ["广州", "杭州"]
    ]

    charts = GeoLines("GeoLines-默认示例", **style.init_style)
    charts.add("从广州出发", data_guangzhou, **style_geo)
    page.add(charts)

    '''
    Map
    '''
    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    chart = Map("全国地图", **style.init_style)
    chart.add("", attr, value, maptype='china', is_label_show=True)
    page.add(chart)

    value = [155, 66, 78]
    attr = ["宁波市", "温州市", "杭州市"]
    chart = Map("地图", **style.init_style)
    '''
    is_map_symbol_show=False不带标记点
    '''
    chart.add("", attr, value, maptype='浙江', 
              is_label_show=True,is_visualmap=True, 
              visual_range=[min(value), max(value)],
              is_map_symbol_show=False,
              visual_text_color='#000')
    page.add(chart)


    return page.render_embed()
    
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pyecharts')
def pyecharts():
    return render_template('pyecharts.html', myechart=scatter3d())

@app.route('/bar')
def bar():
    return render_template("bar.html")

@app.route('/line')
def line():
    return render_template("line.html")

@app.route('/pie')
def pie():
    return render_template("pie.html")

@app.route('/double')
def double():
    return render_template("double.html")
    
@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/zhejiang.json')
def zhejiang():
    with open('./templates/zhejiang.json','r') as f:
        #json_dict = json.load(f)
        return f.read()
        #return jsonify(json_dict)

@app.route('/330100.json')
def map330100():
    with open('./templates/330100.json','r') as f:
        return f.read()

@app.route('/330200.json')
def map330200():
    with open('./templates/330200.json','r') as f:
        return f.read()

@app.route('/330300.json')
def map330300():
    with open('./templates/330300.json','r') as f:
        return f.read()

@app.route('/330400.json')
def map330400():
    with open('./templates/330400.json','r') as f:
        return f.read()

@app.route('/330500.json')
def map330500():
    with open('./templates/330500.json','r') as f:
        return f.read()

@app.route('/330600.json')
def map330600():
    with open('./templates/330600.json','r') as f:
        return f.read()

@app.route('/330700.json')
def map330700():
    with open('./templates/330700.json','r') as f:
        return f.read()

@app.route('/330800.json')
def map330800():
    with open('./templates/330800.json','r') as f:
        return f.read()

@app.route('/330900.json')
def map330900():
    with open('./templates/330900.json','r') as f:
        return f.read()

@app.route('/331000.json')
def map331000():
    with open('./templates/331000.json','r') as f:
        return f.read()

@app.route('/331100.json')
def map331100():
    with open('./templates/331100.json','r') as f:
        return f.read()

@app.route('/databar')
def getdata_bar():
    sql = "SELECT * from ECHART"
    source1,source2=opm.op_select(sql)
    tmp=list(zip(*source1))
    data={
            'categories': list(tmp[0]),
            'data': list(tmp[1])
         }
    json_str = json.dumps(data, ensure_ascii=False)
    return json_str

@app.route('/dataline')
def getdata_line():
    sql = "SELECT * from LINE"
    source1,source2=opm.op_select(sql)
    tmp=list(zip(*source1))
    data={
            'key': list(tmp[0]),
            'val': list(tmp[1])
         }
    json_str = json.dumps(data, ensure_ascii=False)
    return json_str

@app.route('/datapie')
def getdata_pie():
    sql = "SELECT * from PIE"
    source1,source2=opm.op_select(sql)
    tmp=list(zip(*source1))
    
    res=[]
    for row in source1:
        result={}
        result['name']=row[0]
        result['value']=row[1]
        res.append(result)
    data={
            'key': list(tmp[0]),
            'val': res
         }
    json_str = json.dumps(data, ensure_ascii=False)
    return json_str

@app.route('/datadouble')
def getdata_double():
    sql = """SELECT 
             a.产品名称,
             cast(a.2012 as char) as '2012',
             cast(a.2013 as char) as '2013',
             cast(a.2014 as char) as '2014',
             cast(a.2015 as char) as '2015'
             from EVIEW a"""
    source1,source2=opm.op_select(sql)
    tmp1=[list(zip(*source2))[0]]
    for tmp in source1:
        tmp1.append(tmp)
    data={
            'val': tmp1
         }
    json_str = json.dumps(data, ensure_ascii=False)
    return json_str

#多线程返回值
class MySQLThread(Thread):  
    def __init__(self, sql):  
        Thread.__init__(self)  
        self.sql = sql
  
    def run(self):  
        self.result = opm_dict.op_select(self.sql)
  
    def get_result(self):  
        return self.result  
    
@app.route('/datamap')
def getdata_map():
    sql1="""
        select a.city name,ROUND(sum(usd_price)/100000000,2) value from data_hg_hgyw_city a
        where a.bil_year=2018 and a.bil_month='03'
        group by a.city
        """
    sql2="""
        SELECT b.traf_name name,ROUND(sum(usd_price) / 100000000, 2) value
        FROM data_hg_hgyw_city a LEFT JOIN dim_hg_ysfs b ON a.traf_mode = b.traf_mode
        WHERE	a.bil_year = 2018 AND a.bil_month = '03'
        GROUP BY b.traf_name
    """
    
    t1=MySQLThread(sql1)
    t2=MySQLThread(sql2)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    source1,source2=t1.get_result()
    source3,source4=t2.get_result()
    
    data={
            'val1': source1,
            'val2': source3
         }
         
    json_str = json.dumps(data, ensure_ascii=False)
    return json_str

if __name__=='__main__':
    opm = OPMysql()
    opm_dict = OPMysql_dict()
    app.debug=True
    app.run(host='0.0.0.0',port=9000)
    opm.dispose()
