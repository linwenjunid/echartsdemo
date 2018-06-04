# coding=utf-8
import json
import warnings
from db.OPMysql import OPMysql
from db.OPMysql_dict import OPMysql_dict
warnings.filterwarnings("ignore")
from flask import Flask,render_template,jsonify

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

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

@app.route('/datamap')
def getdata_map():
    sql="""
        select a.city name,ROUND(sum(usd_price)/100000000,2) value from data_hg_hgyw_city a
        where a.bil_year=2018 and a.bil_month='03'
        group by a.city
        """
    source1,source2=opm_dict.op_select(sql)
    json_str = json.dumps(source1, ensure_ascii=False)
    return json_str

if __name__=='__main__':
    opm = OPMysql()
    opm_dict = OPMysql_dict()
    app.debug=True
    app.run(host='0.0.0.0',port=9000)
    opm.dispose()
