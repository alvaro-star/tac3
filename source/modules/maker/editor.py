from ..display import display
from .info import Info
from .grid import Grid
from ..entities.tiles import TileMap
from OpenGL.GL import *
from ..ui.background import Background
from ..ui.levels import Level1
from .notify import notify
from .pallet import Pallet
from .button import Button
from ..constants import *

class Editor:
    def create(self):
        self.running = True         

        display.create_display()
        self.bg = Background(*display.size, "Black")

        # load tiles
        self.tile_map = TileMap()        
        self.tile_map.load_sprite_maps()
        self.level1 = Level1()
        if not self.level1.load(self.tile_map):
            self.level1.load(self.tile_map)

        # assets        
        self.grid = Grid(self.level1)        
        self.pallet = Pallet(self.tile_map)   
        self.info = Info(self.grid, self.pallet)     
      
        text, message = "Save", "Map saved!!!"
        self.button_save = Button(text=text, message=message, icon=ICON_SAVE)
        self.button_save.rect.topleft = (0, display.size[1]-SIZE_ICON[1])

        text, message = "Load", "Map loaded!!!"
        self.button_load = Button(text=text, message=message, icon=ICON_LOAD)
        self.button_load.rect.topleft = (self.button_save.rect.w, display.size[1]-SIZE_ICON[1])
        
        

        '''self.notify_setup()


    def notify_setup(self):              
        self.notify_anchor = Notify([self.grid, self.info], Anchor)
        self.notify_select = Notify([self.pallet], Select)
        self.notify_fill = Notify([self.grid], Fill)
        self.notify_message = Notify([self.button_save], Message)
        self.notify_over_save = Notify([self.button_save], Over)
        self.notify_clicked_save = Notify([self.button_save], Clicked)
        
        self.notify_over_left = Notify([self.button_left], Over)
        self.notify_over_up = Notify([self.button_up], Over)
        self.notify_over_down = Notify([self.button_down], Over)
        self.notify_over_right = Notify([self.button_right], Over)

        self.notify_clicked_left = Notify([self.button_left], Clicked)
        self.notify_clicked_up = Notify([self.button_up], Clicked)
        self.notify_clicked_down = Notify([self.button_down], Clicked)
        self.notify_clicked_right = Notify([self.button_right], Clicked)

        self.notify_anchor_vertical = Notify([self.grid_vertical_bar], AnchorV)
        self.notify_anchor_horizontal = Notify([self.grid_horizontal_bar], AnchorH)'''


    def update(self, dt:float):
        self.info.update(dt)
        self.grid.update(dt)
        self.pallet.update(dt)
        self.button_save.update(dt) 
        self.button_load.update(dt)  
        
        notify.clear()


    def draw(self):
        self.bg.draw()
        self.info.draw()
        self.grid.draw()
        self.pallet.draw()
        self.button_save.draw()
        self.button_load.draw()
        
        


editor = Editor()

