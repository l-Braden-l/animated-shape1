# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
def init_game (): 
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True


# -- Draw Rectangle -- # 
def draw_rectangle(screen, color, x, y, width, height):
   pygame.draw.rect(screen, color, (x, y, width, height))


# -- Draw Text -- #
def draw_text(screen, text, x, y, font_size, font_color, font_name=None, bold=False, italic=False): 
   if font_name: 
      font = pygame.font.Font(font_name, font_size)
   else:
      font = pygame.font.Font(None, font_size)

   font.set_bold(bold)
   font.set_italic(italic)
   text_surface = font.render(text, True, font_color)
   screen.blit(text_surface, (x, y))



def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here

   # -- Rectangle Staring position -- # 
   rect_x = 50
   rect_y = 50 


   # -- Speed and Direction of Rectangle -- #
   rect_change_x = 5
   rect_change_y = 5 


   running = True
   while running:

   
         

      running = handle_events()
      screen.fill(config.BLACK) # Use color from config

      # -- Text 1 -- #
      text1 = "Braden Leach"
      x1 = 75
      y1 = 100
      font_size1 = 48
      color1 = config.GREEN
      draw_text(screen, text1, x1, y1, font_size1, color1)

      # -- Text 2 -- #
      text2 = "Buckley"
      x2 = 75
      y2 = 150
      font_size2 = 48
      color2 = config.RED
      draw_text(screen, text2, x2, y2, font_size2, color2, bold=True)

      # -- Text 3 -- #
      text3 = "animated-shape1"
      x3 = 75
      y3 = 200
      font_size3 = 48
      color3 = config.SKY_BLUE
      draw_text(screen, text3, x3, y3, font_size3, color3, italic=True)


      # -- Draw Rectangle -- # 
      color = config.SKY_BLUE
      pygame.draw.rect(screen, config.BROWN, [rect_x, rect_y, 50, 50])
      rect_x += rect_change_x
      rect_y += rect_change_y


      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()