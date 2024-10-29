import os
import random
import iso


class Terrain(iso.SpriteSet):
    def __init__(self, w, h) -> None:
        iso.SpriteSet.__init__(self)
        
        grass_tiles_filenames = os.listdir("assets/tiles")
        for x in range(0, h):
            for y in range(0, w):
                tile_filename = random.choice(grass_tiles_filenames);
                tile_path = f"assets/tiles/{tile_filename}"
                tile = iso.Sprite(tile_path)
                tile.location = [x, y, 0]
                self.addSprite(tile)