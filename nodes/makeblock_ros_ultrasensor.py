#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
from megapi import *

pub = rospy.Publisher('makeblock_ros_ultrasensor', Float32, queue_size=0)


def onRead(v):
    print("and here!")
    rospy.loginfo(v)
    pub.publish(v)


def talker():
    bot = MegaPi()
    bot.start("/dev/ttyUSB0")

    rospy.init_node('makeblock_ros_ultrasensor', anonymous=False)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        sleep(0.1)
        print("been here!")
        bot.ultrasonicSensorRead(3, onRead)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
