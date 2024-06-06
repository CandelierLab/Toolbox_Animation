import os

import project

from Animation.Window import *
from Animation.Animation_2d import *

os.system('clear')

# --- 2D Animation ---------------------------------------------------------

class Anim(Animation_2d):

  def __init__(self, W):

    super().__init__(W)

    self.add(image, 'background',
      image = self.ripple(0),
      cmap = Colormap('gnuplot', range=[-1, 1]),
      zvalue = -1,
    )

  def ripple(self, t):
    x = np.linspace(-1, 1, 500)
    X, Y = np.meshgrid(x, x)
    return np.sin((20 * X ** 2) + (20 * Y ** 2) - t/2/np.pi)

  def update(self, t):

    # Update timer display
    super().update(t)

    self.item['background'].image = self.ripple(t.step)

# --- Main -----------------------------------------------------------------

W = Window('Field animation')
W.add(Anim(W))

# Allow backward animation
W.allow_backward = True
W.allow_negative_time = True

W.show()