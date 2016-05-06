#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
from megapi import *
from makeblock_ros.srv import *

bot = None


def onRead(v):
    print("and here!")
    rospy.loginfo(v)
    pub.publish(v)


def handle_makeblock_motors(req):
    global bot
    bot.motorRun(M1, req.s1)
    bot.motorRun(M2, req.s2)
    return 1


pub = rospy.Publisher('makeblock_ros_ultrasensor', Float32, queue_size=1)
s = rospy.Service('makeblock_ros_move_motors', MakeBlockMover,
                  handle_makeblock_motors)


def main():
    global bot
    bot = MegaPi()
    bot.start("/dev/ttyUSB0")
    rospy.init_node('makeblock_ros', anonymous=False)

    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        sleep(0.1)
        print("been here!")
        bot.ultrasonicSensorRead(3, onRead)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
