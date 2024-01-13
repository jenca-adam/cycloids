from circledraw import Spin, Coor, record
TEST_SPIN = Spin(214, 25, 0, Spin(100,100,10,Spin(100,200,20,Spin(132,21,30,Coor(700,700))))) 
SIZE=(1400,1400)
FPS=30
SPEED=30
record(TEST_SPIN, "output2.mp4", (0,255,255), SIZE, FPS, 1200, SPEED) 
