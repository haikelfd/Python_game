class Config():
    FPS = 9
    MENU_FPS = 60
    WINDOWS_WIDTH = 640
    WINDOWS_HEIGHT = 480
    CELLSIZE = 20
    assert WINDOWS_WIDTH % CELLSIZE == 0, "Windows width must be a multiple of cell size."
    assert WINDOWS_HEIGHT % CELLSIZE == 0, "Windows height must be a multiple of cell size."
    CELLWIDTH = int(WINDOWS_WIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOWS_HEIGHT / CELLSIZE)


    #Colors

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0) 
    DARKGREEN = (0,155,0)
    DARKGREY = (40,40,40)
    BG_COLOR = BLACK 



