from roboflow import Roboflow
rf = Roboflow(api_key="8xfL6DI9xyuMJaDzuc7M")
project = rf.workspace("na-c4wd2").project("rock-detection-amebl")
dataset = project.version(1).download("yolov5")
