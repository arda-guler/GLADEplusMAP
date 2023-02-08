import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
import keyboard
import os
import time

from loader import *
from math_utils import *
from galaxy import *
from camera import *
from graphics import *

def window_resize(window, width, height):
    glfw.get_framebuffer_size(window)
    glViewport(0, 0, width, height)

def clear_cmd_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def main():
    global vp_size_changed

    clear_cmd_terminal()
    print(" = = = GLADE+MAP = = = ")
    print("Please enter the number of galaxies to read from the GLADE+ catalogue.")
    print("Enter a single integer n to read from GLADE index 1 to GLADE index n.")
    print("Enter two integers separated with a comma n,m to read from GLADE index n to m.")
    print("(Or enter 'all' to read all galaxies, but that could take a long time and lots of memory.)")
    n_galaxies = input(" > ")
    galaxy_data, min_mass, max_mass = generate_galaxies(read_data(n_galaxies))

    # this mass range related part is done here to make graphics math less expensive
    print("Initializing graphics...")
    print("\nLinear color range:")
    print("Max. mass:", max_mass, "10^10 M_Sun (displayed blue)")
    print("Min. mass:", min_mass, "10^10 M_Sun (displayed red)")
    mass_range = max_mass - min_mass
    inverse_mass_range = mass_range**(-1)

    window_x = 1000
    window_y = 600
    near_clip = 2
    far_clip = 10e5
    fov = 70
    point_size = 1

    cam_strafe_speed = 10
    cam_rotate_speed = 50
    
    cam_pitch_down = "W"
    cam_pitch_up = "S"
    cam_yaw_left = "A"
    cam_yaw_right = "D"
    cam_roll_ccw = "Q"
    cam_roll_cw = "E"
    cam_strafe_up = "U"
    cam_strafe_down = "O"
    cam_strafe_right = "L"
    cam_strafe_left = "J"
    cam_strafe_forward = "I"
    cam_strafe_backward = "K"

    incr_speed = "T"
    decr_speed = "G"

    use_command_line = "C"
    
    glfw.init()
    window = glfw.create_window(int(window_x),int(window_y),"GLADE+MAP", None, None)
    glfw.set_window_pos(window,100,100)
    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, window_resize)
    
    gluPerspective(fov, int(window_x)/int(window_y), near_clip, far_clip)
    glEnable(GL_CULL_FACE)
    glEnable(GL_POINT_SMOOTH)
    glPointSize(point_size)

    cam = camera("main_cam", [0,0,0], [[1,0,0],[0,1,0],[0,0,1]], True)
    cam.move([0,0,-10])

    dt = 1
    speed_change_lock = True

    print("Map window ready.")

    while not glfw.window_should_close(window):
        cycle_start = time.perf_counter()
        glfw.poll_events()

        cam.rotate([(keyboard.is_pressed(cam_pitch_down) - keyboard.is_pressed(cam_pitch_up)) * cam_rotate_speed * dt,
                    (keyboard.is_pressed(cam_yaw_left) - keyboard.is_pressed(cam_yaw_right)) * cam_rotate_speed * dt,
                    (keyboard.is_pressed(cam_roll_ccw) - keyboard.is_pressed(cam_roll_cw)) * cam_rotate_speed * dt])

        cam.move([(keyboard.is_pressed(cam_strafe_left) - keyboard.is_pressed(cam_strafe_right)) * cam_strafe_speed * dt,
                  (keyboard.is_pressed(cam_strafe_down) - keyboard.is_pressed(cam_strafe_up)) * cam_strafe_speed * dt,
                  (keyboard.is_pressed(cam_strafe_forward) - keyboard.is_pressed(cam_strafe_backward)) * cam_strafe_speed * dt])

        if (not speed_change_lock) and keyboard.is_pressed(incr_speed):
            cam_strafe_speed *= 2
            speed_change_lock = True
        elif (not speed_change_lock) and keyboard.is_pressed(decr_speed):
            cam_strafe_speed *= 0.5
            speed_change_lock = True
        elif speed_change_lock and not (keyboard.is_pressed(incr_speed) or keyboard.is_pressed(decr_speed)):
            speed_change_lock = False
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        drawOrigin()
        drawGalaxies(galaxy_data, min_mass, max_mass, inverse_mass_range, cam)
        glfw.swap_buffers(window)
        dt = time.perf_counter() - cycle_start

    glfw.destroy_window(window)
    
main()
