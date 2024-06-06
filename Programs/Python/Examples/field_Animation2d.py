import os

import project

from Animation.Window import *
from Animation.Animation_2d import *

os.system('clear')

# --- 2D Animation ---------------------------------------------------------

class Anim(Animation_2d):

  def __init__(self, W):

    super().__init__(W, boundaries=[[0,1],[0,2]])

    self.add(image, 'background',
      image = 100*np.ones((1,1)),
      cmap = 'hot',
      crange = [0, 10],
      zvalue = -1,
    )

    # self.item['background'].file = 'test.png'

  def update(self, t):

    # Update timer display
    super().update(t)

    self.item['background'].image = 100+2*t.step*np.ones((1, 1))

# --- Main -----------------------------------------------------------------

W = Window('Simple animation')
W.add(Anim(W))

# Allow backward animation
W.allow_backward = True
W.allow_negative_time = False

# W.movieFile = '/home/raphael/Bureau/test.mp4'

W.autoplay = False

W.show()