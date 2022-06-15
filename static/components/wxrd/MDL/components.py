import base

class Camera(base.Component):
	def __init__(self, id, size, offset):
		super().__init__(id, "Camera")
		self.set_prop("size", size)
		self.set_prop("offset", offset)
		self.set_prop("layers", [])

class Body2D(base.Component):
	'''
		component read by 2D physics and rendering engines
	'''
	def __init__(self, id, coords, scale):
		super().__init__(id, "Body")
		self.set_prop("pos", coords)
		self.set_prop("scale", scale)
		# first num is degrees, second and third are x and y flip
		self.set_prop("rot", (0, 0, 0))
		self.set_prop("mass", 1)
		self.set_prop("shape", "box")
		self.set_prop("layer", 0)

class Sprite(base.Component):
	'''
		component read by 2D rendering engine
	'''
	def __init__(self, id, frames, offset):
		super().__init__(id, "Sprite")
		self.set_prop("frames", frames)
		self.set_prop("frame_offset", 0)
		# offset from global position
		self.set_prop("offset", offset)