#!/usr/bin/env python

import rospy
from std_msgs.msg import String

team_ID = 'donuts'
team_psd = 'enph353'
license_plate_found = False
comp_time = 240                  # should be 4*60 seconds

def reporter():
    pub = rospy.Publisher('/license_plate', String, queue_size=0)
    rospy.init_node('reporter', anonymous=True)

    start_timer_str = msg(0,'strt')
    stop_timer_str = msg(-1,'stop')

    rospy.sleep(1)
    r = rospy.Rate(10)                  # 10 Hz

    rospy.loginfo(start_timer_str)
    pub.publish(start_timer_str)
    start_time = rospy.get_time()

    prev_time = 0
    while (not rospy.is_shutdown()) and (rospy.get_time()-start_time) < comp_time:
        if license_plate_found:
            # license_plate_str = msg(loc, id)   # replace loc and id
            # rospy.loginf(license_plate_str)
            # pub.publish(license_plate_str)
            something = 0

        curr_time = rospy.get_time()-start_time
        if curr_time.is_integer() and curr_time != prev_time:
            disp_time_str = str(curr_time) + ' seconds since competition timer started'
            print(disp_time_str)
            prev_time = curr_time
        r.sleep()
    
    rospy.loginfo(stop_timer_str)
    pub.publish(stop_timer_str)


def msg(lp_loc, lp_id):
    ret_str = team_ID + ',' + team_psd + ',' + str(lp_loc) + ',' + str(lp_id)
    return ret_str


if __name__=='__main__':
    try:
        reporter()
    except rospy.ROSInterruptException:
        pass