#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import pygame

pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption('TurtleSim Control')

rospy.init_node('turtle_control')

turtle_names = [f"turtle{i+1}" for i in range(27)]

publishers = {name: rospy.Publisher(f'{name}/cmd_vel', Twist, queue_size=10) for name in turtle_names}


def send_mov(turtle, linear, angular):
    mov = Twist()
    mov.linear.x = linear
    mov.angular.z = angular
    publishers[turtle].publish(mov)

def control_turtles():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    keys = pygame.key.get_pressed()
    linear = 0.0
    angular = 0.0

    if keys[pygame.K_UP]:
        linear = 2.0  # Move forward
    elif keys[pygame.K_DOWN]:
        linear = -2.0  # Move backward

    if keys[pygame.K_LEFT]:
        angular = 2.0  # Turn left
    elif keys[pygame.K_RIGHT]:
        angular = -2.0  # Turn right

    for turtle in turtle_names:
        send_mov(turtle, linear, angular)
   
    rospy.sleep(0.1)
    return True

running = True
while running and not rospy.is_shutdown():
    running = control_turtles()

pygame.quit()