import js
p5 = js.window

class Puck:
  x = 250
  y = 150
  size = 25

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.ellipse(0, 0, self.size, self.size)
    p5.fill(255, 255, 0)
    p5.pop()

# instantiate a Puck object:
puck1 = Puck(x = 250, y = 150)
puck2 = Puck(x = 150, y = 250)
puck3 = Puck(x = 50, y = 200)
puck4 = Puck(x = 220, y = 220)
puck5 = Puck(
  x = int(p5.random(50, 250)),
  y = int(p5.random(50, 250))
)

# pacman global variables:
pacman_x = 160
pacman_y = 150
pacman_size = 75
pacman_direction = 'right'
pacman_state = 'closing'
pacman_mouth = 0

# ghost images:
ghost_img1 = p5.loadImage('ghost_1.png')
ghost_img2 = p5.loadImage('ghost_2.png')

# load font:
font = p5.loadFont('PressStart2P.otf')
    
program_state = 'START'

def setup():
  p5.createCanvas(300, 300) 
  # draw rectangles from center:
  p5.rectMode(p5.CENTER)
  # draw images from center:
  p5.imageMode(p5.CENTER)
  # set font:
  p5.textFont(font)
  p5.textSize(16)

def draw():
  p5.background(0)   
  # draw puck:
  puck1.draw()
  puck2.draw()
  puck3.draw()
  puck4.draw()
  puck5.draw()
  # draw pacman:
  update_pacman()
  draw_pacman()
  # draw ghost:
  p5.image(ghost_img1, 60, 150)
  
  if(program_state == 'START'):
    p5.fill(255, 255, 0)
    p5.text('Click to Start..', 20, 40)

def draw_puck():
  p5.push()
  p5.translate(puck_x, puck_y)
  p5.ellipse(0, 0, puck_size, puck_size)
  p5.fill(255, 255, 0)
  p5.pop()

def update_pacman():
  global pacman_state
  global pacman_mouth
  if(pacman_state == 'opening'):
    if(pacman_mouth < p5.radians(30)): 
      pacman_mouth += 0.01
    else: # reverse to closing mouth direction
      pacman_state = 'closing'
  elif(pacman_state == 'closing'):
    if(pacman_mouth > 0): # closing mouth
      pacman_mouth -= 0.01
    else: # reverse to opening mouth direction
      pacman_state = 'opening'
      
def draw_pacman():
  global pacman_x, pacman_y 
  p5.push()
  # move pacman:
  p5.translate(pacman_x, pacman_y)
  # rotate pacman:
  if(pacman_direction == 'right'):
    p5.rotate(p5.radians(0))
  elif(pacman_direction == 'left'):
    p5.rotate(p5.radians(180))
  elif(pacman_direction == 'up'):
    p5.rotate(p5.radians(270))
  elif(pacman_direction == 'down'):
    p5.rotate(p5.radians(90))
  p5.fill(255, 255, 0) # yellow fill
  p5.arc(0, 0, pacman_size, pacman_size, \
         pacman_mouth, p5.TWO_PI - pacman_mouth)
  p5.pop()
  
def keyPressed(event):
  #print('key pressed.. ' + p5.key)
  global pacman_direction
  if(p5.keyCode == p5.UP_ARROW):
    pacman_direction = 'up'
  elif(p5.keyCode == p5.DOWN_ARROW):
    pacman_direction = 'down'
  elif(p5.keyCode == p5.LEFT_ARROW):
    pacman_direction = 'left'
  elif(p5.keyCode == p5.RIGHT_ARROW):
    pacman_direction = 'right'

def keyReleased(event):
  pass
  
def mousePressed(event):
  pass

def mouseReleased(event):
  pass