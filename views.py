def index():
	with open('tamplates/index.html') as tamplate:
		return tamplate.read()


def blog():
	with open('tamplates/blog.html') as tamplate:
		return tamplate.read()