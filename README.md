# 费马都能看懂的json编辑指南

## resource.json

该json由一个一维数组组成

[
    {
        "name": "木头",
        "describe":""
    },
    {
        "name": "石头",
        "describe":""
    }
    ,
    {
        "name": "铜",
        "describe":""
    }
]

该json中，每个对象代表一种资源，name字段为资源名称，describe字段为资源描述

## machine.json

该json由一个二维数组构成

伪代码示例↓,到时花括号中的格式参照下一个花括号示例

[
    [
        {资源0一级机器},
        {资源0二级机器}
    ],
    [
        {资源1一级机器},
        {资源1二级机器}
    ],
    [
        {资源2一级机器},
        {资源2二级机器}
    ]
]

花括号中为机器对象，每个机器对象包含以下字段↓

{
    "name": "伐木机",
    "build_cost":
    [
        10,
        0,
        0
    ],
    "build_cost_boost":1.2,
    "material_cost":
    [
        0,
        0,
        0
    ],
    "power_cost":0,
    "production":1,
    "describe":"这是资源机器描述"
}

build_cost代表建造机器所消耗的资源数量,与resource.json中的资源顺序对应

build_cost_boost代表建造机器所消耗的资源数量的倍率,这个例子中每建造一个机器价钱*1.2倍

material_cost代表机器运行所消耗的资源数量,与resource.json中的资源顺序对应/s

power_cost代表机器运行所消耗的能量/s

production代表机器每秒产出资源数量/s

describe代表机器描述

## machine_study.json

该json由一个一维数组组成

production代表每秒产生知识点数/s,用于解锁新的技术

其余字段与machine.json中的机器对象相同

示例↓

[
    {
        "name": "口算天天练",
        "build_cost":
        [
            10,
            10,
            10
        ],
        "build_cost_boost": 1.2,
        "describe": "口算天天练,天天练口算,每秒产生1科技",
        "production": 1
    },
    {
        "name": "小学奥数",
        "build_cost":
        [
            100,
            100,
            100
        ],
        "build_cost_boost": 1.2,
        "describe": "这可相当需要智慧,每秒产生5科技",
        "production": 5
    }
]

## machine_power.json

该json由一个一维数组组成

production代表每秒产生能量数/s

其余字段与machine.json中的机器对象相同

示例↓

[
    {
        "name": "太阳能光电板",
        "build_cost":
        [
            10,
            10,
            50
        ],
        "material_cost":
        [
            0,
            0,
            0
        ],
        "build_cost_boost": 1.2,
        "describe":"太阳能发电，不需要消耗资源,每秒产生10能源",
        "production":10
    },
    {
        "name":"火力发电厂",
        "build_cost":
        [
            100,
            10,
            50
        ],
        "material_cost":
        [
            10,
            0,
            0
        ],
        "build_cost_boost": 1.2,
        "describe":"使用煤炭发电,每秒产生50能源,消耗10木头",
        "production":50
    }
]

## unlock.json

该json由一个一维数组组成,代表科技解锁页面

[
    {},
    {},
    {},
    {}
]

从第一个花括号开始编号为0,1,2以此类推

花括号示例如下

knowledge代表解锁该技术需要的知识点数

class与html页面关联,建议写一个规整的名字

front代表解锁这个技术的前置科技编号,没解锁前置科技时不显示该科技也不能用知识点进行解锁

默认第0个科技自动解锁

{
    "name": "解锁科学机器",
    "describe": "可以建造一级科学机器",
    "knowledge": 1,
    "class":"study_0",
    "front":[1]
}

