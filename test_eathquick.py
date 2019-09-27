#
#
#
import requests
import httpretty
import earthquick


jsondata = """{"type":"FeatureCollection","metadata":{"generated":1569593537000,
"status":200,"api":"1.8.1"},"features":[{"type":"Feature","properties":
{"mag":2.36,"place":"20km NNE of Trona, CA","time":1569593254560,"updated":
1569593492131,"type":"earthquake"}},{"type":"Feature","properties":{"mag":
1.2,"place":"110km W of Cantwell, Alaska","time":1569592581941,"type":
"earthquake"}},{"type":"Feature","properties":{"mag":0.94,"place":
"20km E of Little Lake, CA","time":1569591553550,"type":"earthquake"}},{"type":
"Feature","properties":{"mag":1.11,"place":"20km E of Little Lake, CA","time":
1569591516220,"type":"earthquake"}}]}"""


sorteddata = [{"type":"Feature","properties":{"mag":1.11,"place":
"20km E of Little Lake, CA","time":1569591516220,"type":"earthquake"}},
{"type":"Feature","properties":{"mag":0.94,"place":"20km E of Little Lake, CA",
"time":1569591553550,"type":"earthquake"}},{"type":"Feature","properties":
{"mag":1.2,"place":"110km W of Cantwell, Alaska","time":1569592581941,
"type":"earthquake"}},{"type":"Feature","properties":{"mag":2.36,"place":
"20km NNE of Trona, CA","time":1569593254560,"updated":1569593492131,"type":
"earthquake"}}]


dict1 = {"mag":1.11,"place":"20km E of Little Lake, CA",
    "time":1569591516220,"type":"earthquake"}


@httpretty.activate
def test_readData1():
    httpretty.register_uri(httpretty.GET, "https://tinyurl.com/y34hprk5",
                        body='{"origin": "127.0.0.1", "features": \
                            [{"properties": {"time": 1569555787345}}]}')
    data = earthquick.readData('https://tinyurl.com/y34hprk5')
    assert data == [{"properties": {"time": 1569555787345}}]
    httpretty.disable() 
    httpretty.reset() 


@httpretty.activate
def test_readData2():
    httpretty.register_uri(httpretty.GET, "https://tinyurl.com/y34hprk5",
                        body=jsondata)
    data = earthquick.readData('https://tinyurl.com/y34hprk5')
    assert data == sorteddata
    httpretty.disable() 
    httpretty.reset()


def test_checktime1():
    utctime = earthquick.utcTime(1569593254560)
    assert utctime == '2019-09-27T07:07:34+00:00'


def test_checktime2():
    utctime = earthquick.utcTime(1568997232935)
    assert utctime == '2019-09-20T09:33:52+00:00'


def test_struct01():
    myobj = earthquick.Struct(**dict1)
    assert myobj.time == 1569591516220


def test_struct02():
    myobj = earthquick.Struct(**dict1)
    assert myobj.type == 'earthquake'


def test_stateName01():
    place = earthquick.stateName('21km E of Little Lake, CA')
    assert place == '21km E of Little Lake, California'


def test_stateName02():
    place = earthquick.stateName('10km S of Wilkerson, CA')
    assert place == '10km S of Wilkerson, California'

