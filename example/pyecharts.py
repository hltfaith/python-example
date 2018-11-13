## author: changhao
##  date:  2018-11-13
##  info: 北控项目地图供应站位置分布

from pyecharts import Map, Geo

## 先定义一下数据

# 世界地图数据
value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr = ["China", "Canada", "Brazil", "Russia", "United States"]

# 直辖市
province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9, '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': 1, '其他': 1}
provice=list(province_distribution.keys())
values=list(province_distribution.values())

# 城市 -- 指定省的城市 xx市
city = ['海淀区', '通州区', '房山区', '延庆区', '密云区', '平谷区', '顺义区', '昌平区', '朝阳区', '石景山区', '大兴区', '东城区', '西城区']
values2 = ['13552134043', 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1, 1.1, 2.2, 3.3, 4.4]

# # 区县 -- 具体城市内的区县  xx县
# quxian = ['夏邑县', '民权县', '梁园区', '睢阳区', '柘城县', '宁陵县']
# values3 = [3, 5, 7, 8, 2, 4]


#河南地图 数据必须是省内放入城市名
map2 = Map("北京市液化石油气公司南郊灌瓶厂供应站分布情况", '北京地区', width=1200, height=600)
map2.add('联系方式：', city, values2, visual_range=[1, 20], maptype='北京', is_visualmap=True, visual_text_color='#000')
map2.show_config()
map2.render(path="04-01北京地图.html")



'''
option = {
    // 加载 bmap 组件
    bmap: {
        // 百度地图中心经纬度
        center: [120.13066322374, 30.240018034923],
        // 百度地图缩放
        zoom: 14,
        // 是否开启拖拽缩放，可以只设置 'scale' 或者 'move'
        roam: true,
        // 百度地图的自定义样式，见 http://developer.baidu.com/map/jsdevelop-11.htm
        mapStyle: {}
    },
    series: [{
        type: 'scatter',
        // 使用百度地图坐标系
        coordinateSystem: 'bmap',
        // 数据格式跟在 geo 坐标系上一样，每一项都是 [经度，纬度，数值大小，其它维度...]
        data: [ [120, 30, 1] ]
    }]
}

// 获取百度地图实例，使用百度地图自带的控件
var bmap = chart.getModel().getComponent('bmap').getBMap();
bmap.addControl(new BMap.MapTypeControl());



'''


