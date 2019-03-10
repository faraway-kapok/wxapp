### 单个城市天气查询
```json
// success
{
    "errcode": 0,
    "data": {
        "city":"广州",
        "realtime":{
            "temperature":"18",
            "humidity":"78",
            "info":"阴",
            "wid":"02",
            "direct":"北风",
            "power":"3级",
            "aqi":"16"
        },
        "future":[
            {
                "date":"2019-03-10",
                "temperature":"12\/17℃",
                "weather":"小雨转多云",
                "wid":{
                    "day":"07",
                    "night":"01"
                },
                "direct":"持续无风向"
            },
            {
                "date":"2019-03-11",
                "temperature":"13\/21℃",
                "weather":"多云转晴",
                "wid":{
                    "day":"01",
                    "night":"00"
                },
                "direct":"持续无风向"
            },
            {
                "date":"2019-03-12",
                "temperature":"15\/23℃",
                "weather":"晴转多云",
                "wid":{
                    "day":"00",
                    "night":"01"
                },
                "direct":"持续无风向"
            },
            {
                "date":"2019-03-13",
                "temperature":"15\/24℃",
                "weather":"多云转中雨",
                "wid":{
                    "day":"01",
                    "night":"08"
                },
                "direct":"持续无风向转北风"
            },
            {
                "date":"2019-03-14",
                "temperature":"16\/22℃",
                "weather":"中雨转多云",
                "wid":{
                    "day":"08",
                    "night":"01"
                },
                "direct":"持续无风向"
            }
        ]
    }
}
// error
{
    "errcode": 50001,
    "errmsg": "城市不存在"
}
* errcode 0 为正常，大于 0 为错误码
* errmsg，errcode 大于 0 时的错误信息
* data，数据包
```

### 多个城市天气查询
```json
// success
{
    "errcode": 0,
    "data": [
        {"city": "河南"},
        {"city": "广州"}
    ]
}
```