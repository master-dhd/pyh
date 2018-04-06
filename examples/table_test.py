#!/usr/bin/python
#coding:utf-8

import sys
reload(sys) 
sys.setdefaultencoding('utf8')

from pyh import *

num = 5
info = 'RDS监控 共%s个' % num
page = PyH('RDS')
#page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
#page.addJS('myJavascript1.js', 'myJavascript2.js')
page << h1(info)
page << style('td {text-align:center}')
mytab = page << table(width="95%", rules="all", cellpadding="2", cellspacing="1", align="center")

tr1 = mytab << tr()
tr1 << th('序号', nowrap='nowrap')
tr1 << th('实例ID', nowrap='nowrap')
tr1 << th('实例名称', nowrap='nowrap')
tr1 << th('CPU', nowrap='nowrap')
tr1 << th('QPS', nowrap='nowrap')
tr1 << th('IOPS', nowrap='nowrap')
tr1 << th('连接数', nowrap='nowrap')
tr1 << th('磁盘使用率', nowrap='nowrap')
tr1 << th('主备延迟', nowrap='nowrap')
tr1 << th('活跃线程', nowrap='nowrap')
tr1 << th('流量(KB)', nowrap='nowrap')

dict_lst = []
import copy
v_dict = [
    ['9999',
	    {
	        'id':'v_id_9999',
		'width':'50px',
		'style':'',
		'msg':'数据库中的ID',
	    }
	],
	['rds3h85eqq2akpl306hz',
	    {
		'id':'v_rid_9999',
		'width':'50px',
		'style':'',
		'msg':'RDS的实例ID'
	    }
	],
	['rds_cs_sql_20',
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
	['dhd3h85eqq2akpl306hz',
	    {
		'id':'v_rid_9999',
		'style':'',
		'msg':'RDS的实例ID'
	    }
	],
	['rds_cs_sql_19',
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
#dict_lst = []
dict_lst.append(v_dict)
dict_lst.append(x_dict)
#print dict_lst

#[['a', {'name':'', 'width':''}], ['b', {'name':'', 'width':''}], ['c', {'name':'', 'width':''}]]    

#for i in range(len(dict_lst)):
mytr = mytab << tr()
for index in range(len(dict_lst[0])):
    n_dict = dict_lst[0][index]
    mytr << td(n_dict[0], id=n_dict[1]['id'], style=n_dict[1]['style'], nowrap='')
mytr = mytab << tr()
for index in range(len(dict_lst[1])):
    n_dict = dict_lst[1][index]
    mytr << td(n_dict[0], id=n_dict[1]['id'], style=n_dict[1]['style'], nowrap='')

page.printOut()
