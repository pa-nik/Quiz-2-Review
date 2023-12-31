import js
p5 = js.window

program_state = 'START'

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

class PowerPuck(Puck):
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.rect(0, 0, self.size, self.size)
    p5.fill(255, 255, 0)
    p5.pop()

puck_list = []
# puck_list.append(puck1)
# puck_list.append(puck2)
# puck_list.append(puck3)
# puck_list.append(puck4)
for i in range(5):
  p = Puck(
    x = int(p5.random(50, 250)),
    y = int(p5.random(50, 250))
  )
  puck_list.append(p)

puck6 = PowerPuck(
  x = int(p5.random(50, 250)),
  y = int(p5.random(50, 250))
)
puck_list.append(puck6)

class Pacman:
  x = 160
  y = 150
  size = 75
  direction = 'right'
  state = 'closing'
  mouth = 0

  def update(self):
    if(self.state == 'opening'):
      if(self.mouth < p5.radians(30)): 
        self.mouth += 0.01
      else: # reverse to closing mouth direction
        self.state = 'closing'
    elif(self.state == 'closing'):
      if(self.mouth > 0): # closing mouth
        self.mouth -= 0.01
      else: # reverse to opening mouth direction
        self.state = 'opening'

    if(self.direction == 'right'):
      if(self.x < p5.width + self.size/2):
        self.x += 0.5
      else:
        self.x = -self.size/2
    elif(self.direction == 'left'):
      if(self.x > -self.size/2):
        self.x -= 0.5
      else:
        self.x = p5.width + self.size/2
    elif(self.direction == 'up'):
      if(self.y > -self.size/2):
        self.y -= 0.5
      else:
        self.y = p5.height + self.size/2
    elif(self.direction == 'down'):
      if(self.y < p5.height + self.size/2):
        self.y += 0.5
      else:
        self.y = -self.size/2

  def draw(self):
    p5.push()
    # move pacman:
    p5.translate(self.x, self.y)
    # rotate pacman:
    if(self.direction == 'right'):
      p5.rotate(p5.radians(0))
    elif(self.direction == 'left'):
      p5.rotate(p5.radians(180))
    elif(self.direction == 'up'):
      p5.rotate(p5.radians(270))
    elif(self.direction == 'down'):
      p5.rotate(p5.radians(90))
    p5.fill(255, 255, 0) # yellow fill
    p5.arc(0, 0, self.size, self.size, \
           self.mouth, p5.TWO_PI - self.mouth)
    p5.pop()

# instantiate Pacman object:
pacman = Pacman()

class Ghost:
  def __init__(self, x=50, y=150):
    self.x = x
    self.y = y
    self.img1 = p5.loadImage('ghost_1.png')
    self.img2 = p5.loadImage('ghost_2.png')

  def update(self):
    if(self.y < p5.height + self.img1.height/2):
      self.y += 0.5
    else:
      self.y = -self.img1.height/2
    
  def draw(self):
    if(p5.millis() % 1000 < 500):
      p5.image(self.img1, self.x, self.y)
    else:
      p5.image(self.img2, self.x, self.y)

ghost = Ghost(x = 50, y = 50)

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
  global program_state
  if(program_state == 'START'):
    p5.fill(255, 255, 0)
    p5.text('Click to Start..', 20, 40)
  elif(program_state == 'WIN'):
    p5.fill(255, 255, 0)
    p5.text('You Win!', 20, 40)
  elif(program_state == 'LOOSE'):
    p5.fill(255, 255, 0)
    p5.text('You Loose!', 20, 40)
  elif(program_state == 'PLAY'):
    # draw pucks:
    i = 0
    while(i < len(puck_list)):
      p = puck_list[i]
      d = p5.dist(pacman.x, pacman.y, p.x, p.y)
      if(d < pacman.size/2):
        print('eat puck!')
        puck_list.pop(i)
        # check if all pucks are gone:
        if(len(puck_list) == 0):
          print('all the pucks gone!')
          program_state = 'WIN'
      else:
        p.draw()
      i += 1
    
    # draw pacman:
    pacman.update()
    pacman.draw()
    
    ghost.update()
    ghost.draw()

    d = p5.dist(pacman.x, pacman.y, ghost.x, ghost.y)
    if(d < 50):
      print('ghost catches pacman!')
      program_state = 'LOOSE'
  

def keyPressed(event):
  #print('key pressed.. ' + p5.key)
  global pacman
  if(p5.keyCode == p5.UP_ARROW):
    pacman.direction = 'up'
  elif(p5.keyCode == p5.DOWN_ARROW):
    pacman.direction = 'down'
  elif(p5.keyCode == p5.LEFT_ARROW):
    pacman.direction = 'left'
  elif(p5.keyCode == p5.RIGHT_ARROW):
    pacman.direction = 'right'

def keyReleased(event):
  pass
  
def mousePressed(event):
  global program_state
  if(program_state == 'START'):
    program_state = 'PLAY'

def mouseReleased(event):
  pass