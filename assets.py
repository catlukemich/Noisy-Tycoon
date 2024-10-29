import pygame

sprites_images_cache = {}
def loadSpriteImage(image_path):
    if not image_path in sprites_images_cache:
      image = pygame.image.load(image_path).convert()
      image.set_colorkey((0, 0, 0), pygame.RLEACCEL) # The black is the colorkey, meaning that totally black areas will be transparent
      sprites_images_cache[image_path] = image
    return sprites_images_cache[image_path]  