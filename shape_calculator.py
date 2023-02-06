class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __str__(self):
    strself = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return(strself)
  
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    self.area = self.width * self.height
    return(self.area)

  def get_perimeter(self):
    self.perimeter = 2 * (self.width + self.height)
    return(self.perimeter)

  def get_diagonal(self):
    self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return(self.diagonal)

  def get_picture(self):
    pic = str()
    if self.height > 50 or self.width > 50:
      return("Too big for picture.")
    else:
      for h in range(self.height):
        line = "*" * self.width + "\n"
        pic += line
    return(pic)

  def get_amount_inside(self, shape):
    num_width = int(self.width / shape.width)
    num_height = int(self.height / shape.height)
    num_pass = num_width * num_height
    return(num_pass)


class Square(Rectangle):

  def __init__(self, length):
    self.width = length
    self.height = length
  
  def set_side(self, length):
    self.width = length
    self.height = length

  def __str__(self):
    strself = "Square(side=" + str(self.width) + ")"
    return(strself)

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height
