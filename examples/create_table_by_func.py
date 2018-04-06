#!/usr/bin/python
#coding=utf-8
# 基于列表和函数生成table
# 扩展：
# 1. 可将需要展示的数据写成列表(由于填充的每一行的值是有序的，因此使用列表)，用函数生成table.html；
# 本文列表示例：[['a', {'name':'', 'width':''}], ['b', {'name':'', 'width':''}], ['c', {'name':'', 'width':''}]]
# 2. 可根据数据值增加标签属性，例如大于99的数值变成背景色为红色
# 执行方法 python rtable_test.py 2
# 注：后面的执行参数2只是一个参数示例，如无需求则可以去除sys.argv[1]这个变量。

import sys
reload(sys) 
sys.setdefaultencoding('utf8')

from pyh import *


def ini_table(num):
    #初始化table的标题
    info = 'RDS监控 共%s个' % num
    page = PyH('RDS')
    #page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
    #page.addJS('myJavascript1.js', 'myJavascript2.js')
    page << h1(info)
    page << style('td {text-align:center}')
    mytab = page << table(width="95%", rules="all", cellpadding="2", cellspacing="1", align="center")
    tr1 = mytab << tr()
    tr1 << th('序号', nowrap='nowrap') + th('实例ID',nowrap='nowrap') + th('实例名称', nowrap='nowrap') + th('CPU', nowrap='nowrap') + th('QPS', nowrap='nowrap') + th('IOPS', nowrap='nowrap') + th('连接数', nowrap='nowrap') + th('磁盘使用率',nowrap='nowrap') + th('主备延迟', nowrap='nowrap') + th('活跃线程', nowrap='nowrap') + th('流量(KB)',nowrap='nowrap')
    return page, mytab
    

def add_td(tr_n, mytab, v_dict):
    tr_n = mytab << tr()

    #[['a', {'name':'', 'width':''}], ['b', {'name':'', 'width':''}], ['c', {'name':'', 'width':''}]]
    for index in range(len(v_dict)):
        #print v_dict[index]
        n_dict = v_dict[index]
        #添加：值 name with 
        #print n_dict[0], n_dict[1]['id'], n_dict[1]['width'], n_dict[1]['style'] 
        tr_n << td(n_dict[0], id=n_dict[1]['id'], width=n_dict[1]['width'], style=n_dict[1]['style'], nowrap='')

    return tr_n

if __name__ == '__main__':

    #print "\033[31m==================================================\033[0m"
    
    num = sys.argv[1]
    page,mytab = ini_table(num)

    #[['a', {'name':'', 'width':''}], ['b', {'name':'', 'width':''}], ['c', {'name':'', 'width':''}]]
    #用id的唯一性来使用js代码，确保id唯一：v_监控项名称_rds的数据库id
    #数据结构示例
    v_dict = [
        ['9999',
	    {
	        'id':'v_id_9999',
		'width':'50px',
		'style':'',
		'msg':'数据库中的ID',
	    }
	],
	['rds3h85eqq2akpl706hz',
	    {
		'id':'v_rid_9999',
		'width':'50px',
		'style':'',
		'msg':'RDS的实例ID'
	    }
	],
	['rds_cs_up_20',
	    {
		'id':'v_name_9999',
		'width':'50px',
		'style':'',
		'msg':'RDS的自定义名称',
	    }
        ],
        ['99.99%',
	    {
		'id':'v_cpu_9999',
		'width':'50px',
		'style':'',
		'msg':'cpu使用率',
	    }
        ],
        ['12345678',
	    {
		'id':'v_qps_9999',
		'width':'50px',
		'style':'',
		'msg':'qps',
	    }
        ],
        ['12345678',
	    {
		'id':'v_iops_9999',
		'width':'50px',
		'style':'',
		'msg':'iops',
	    }
        ],
        ['12345678',
	    {
		'id':'v_concts_9999',
		'width':'50px',
		'style':'',
		'msg':'连接数',
	    }
        ],
        ['99.99%',
	    {
		'id':'v_disk_9999',
		'width':'50px',
		'style':'',
		'msg':'磁盘使用率',
	    }
        ],
        ['0',
	    {
		'id':'v_back_9999',
		'width':'50px',
		'style':'',
		'msg':'主备延迟',
	    }
        ],
        ['12345678',
	    {
		'id':'v_act_con_9999',
		'width':'50px',
		'style':'',
		'msg':'活跃线程',
	    }
    ],
        ['12345678',
	    {
		'id':'v_netout_9999',
		'width':'50px',
		'style':'',
		'msg':'流量(KB)',
	    }
	],
    ]

    x_dict = [
        ['8888',
	    {
	        'id':'v_id_9999',		
		    'style':'',
		    'msg':'数据库中的ID',
	    }
	],
	['dhd3h85eqq2akpl806hz',
	    {
		'id':'v_rid_9999',
		'style':'',
		'msg':'RDS的实例ID'
	    }
	],
	['rds_cs_up_19',
	    {
		'id':'v_name_9999',
		'style':'',
		'msg':'RDS的自定义名称',
	    }
        ],
        ['88.88%',
	    {
		'id':'v_cpu_9999',
		'style':'',
		'msg':'cpu使用率',
	    }
        ],
        ['87654321',
	    {
		'id':'v_qps_9999',
		'style':'',
		'msg':'qps',
	    }
        ],
        ['87654321',
	    {
		'id':'v_iops_9999',
		'style':'',
		'msg':'iops',
	    }
        ],
        ['87654321',
	    {
		'id':'v_concts_9999',
		'style':'',
		'msg':'连接数',
	    }
        ],
        ['88.88%',
	    {
		'id':'v_disk_9999',
		'style':'',
		'msg':'磁盘使用率',
	    }
        ],
        ['0',
	    {
		'id':'v_back_9999',
		'style':'',
		'msg':'主备延迟',
	    }
        ],
        ['87654321',
	    {
		'id':'v_act_con_9999',
		'style':'',
		'msg':'活跃线程',
	    }
    ],
        ['87654321',
	    {
		'id':'v_netout_9999',
		'style':'',
		'msg':'流量(KB)',
	    }
	],
    ]

    #for tr_n in range(int(num)):
    #    tr_n = 'tr_' + str(tr_n)
    #    add_td(tr_n, mytab, v_dict)
    #page.printOut()

    dict_lst = []
    dict_lst.append(v_dict)
    dict_lst.append(x_dict)
    for n in range(len(dict_lst)):
        mytr = mytab << tr()
        for index in range(len(dict_lst[n])):
            n_dict = dict_lst[n][index]
            mytr << td(n_dict[0], id=n_dict[1]['id'], style=n_dict[1]['style'], nowrap='')
    page.printOut()


