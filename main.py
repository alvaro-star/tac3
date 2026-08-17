from source.game import game
from source.loop import run

if __name__ == "__main__":   
    try:
        game.load_assets() 
        run()        
    except Exception as ex:
        print(ex)
       

    