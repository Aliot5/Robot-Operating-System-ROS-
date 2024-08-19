#!/usr/bin/python3

import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import Kill

def spawner(x, y, theta, name):
    rospy.wait_for_service("/spawn")
    rospy.init_node("client", anonymous=True)
    try:
        spawn_client = rospy.ServiceProxy("/spawn", Spawn)
        resp = spawn_client(x, y, theta, name)
        return resp
    except:
        print("Failed")

def killer(name):
    rospy.wait_for_service("/kill")
    try:
        kill_client = rospy.ServiceProxy("/kill", Kill)
        resp = kill_client(name)
        return resp
    except:
        print("KILL FAILED")



if __name__ == "__main__":
    try:
        print("OK")
        respond = killer("turtle1")
        respond = spawner(1, 4, 0, "turtle1")
        respond = spawner(1, 5, 0, "turtle2")
        respond = spawner(1, 6, 0, "turtle3")
        respond = spawner(1, 7, 0, "turtle4")
        respond = spawner(1, 8, 0, "turtle5")
        respond = spawner(2, 3, 0, "turtle6")
        respond = spawner(2, 9, 0, "turtle7")
        respond = spawner(3, 2, 0, "turtle8")
        respond = spawner(3, 10, 0, "turtle9")
        respond = spawner(4, 1, 0, "turtle10")
        respond = spawner(4, 11, 0, "turtle11")
        respond = spawner(5, 1, 0, "turtle12")
        respond = spawner(5, 6, 0, "turtle13")
        respond = spawner(5, 11, 0, "turtle14")
        respond = spawner(6, 1, 0, "turtle15")
        respond = spawner(6, 6, 0, "turtle16")
        respond = spawner(6, 11, 0, "turtle17")
        respond = spawner(7, 2, 0, "turtle18")
        respond = spawner(7, 6, 0, "turtle19")
        respond = spawner(7, 11, 0, "turtle20")
        respond = spawner(8, 3, 0, "turtle21")
        respond = spawner(8, 6, 0, "turtle22")
        respond = spawner(8, 10, 0, "turtle23")
        respond = spawner(9, 4, 0, "turtle24")
        respond = spawner(9, 5, 0, "turtle25")
        respond = spawner(9, 6, 0, "turtle26")
        respond = spawner(9, 9, 0, "turtle27")
        
        print(respond)
    except:
        print("Somethink went wrong")
    pass