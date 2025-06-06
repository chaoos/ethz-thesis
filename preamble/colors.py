import matplotlib.colors as mpc

def register_color(color_name, color_spec):
    mpc._colors_full_map[color_name] = color_spec
    return mpc._colors_full_map

def tohtml(*pargs):
	return '#%02x%02x%02x' % pargs

def tohtml2(*pargs):
	pargs = tuple(list(map(lambda x: int(255*x), pargs)))
	return '#%02x%02x%02x' % pargs

#
# Customize colors
#

#\definecolor{chapter-color}{cmyk}{1, 0.50, 0, 0.25}
#\definecolor{link-color}{cmyk}{1, 0.50, 0, 0.25}
#\definecolor{cite-color}{cmyk}{0, 0.7, 0.9, 0.2}
register_color("codegreen", tohtml2(0,0.6,0))
register_color("codegray", tohtml2(0.5,0.5,0.5))
register_color("codepurple", tohtml2(0.58,0,0.82))
register_color("backcolour", tohtml2(0.95,0.95,0.92))
register_color("codebgcolor", tohtml(129, 139, 152))
register_color("codehighlightcolor", tohtml(255, 230, 153))
register_color("codeblue", tohtml(102, 214, 237))
register_color("codekeyword", tohtml(249, 36, 114))
register_color("codecomment", tohtml(127, 127, 127))
register_color("backcolor", tohtml(242, 242, 235))
register_color("linkcolor", tohtml(102, 0, 0))
register_color("corange", tohtml(255, 70, 0))
register_color("cyellow", tohtml(209, 153, 0))
register_color("cblue", tohtml(64, 128, 255))
register_color("cbrown", tohtml(153, 102, 51))
register_color("cpink", tohtml(255, 0, 255))
register_color("cred", tohtml(255, 64, 0))
register_color("cgreen", tohtml(0, 191, 0))
register_color("clightblue", tohtml(191, 217, 255))
register_color("cturquois", tohtml(0, 255, 255))
register_color("cpurple", tohtml(128, 0, 255))
register_color("clightgreen", tohtml(175, 255, 175))
register_color("clightgray", tohtml(211, 211, 211))
register_color("clightpink", tohtml(255, 175, 255))
register_color("cdarkblue", tohtml(0, 0, 255))
register_color("cdarkred", tohtml(255, 0, 0))
register_color("cdarkgreen", tohtml(0, 255, 0))
register_color("cgray", tohtml(153, 153, 153))

register_color("myblue", tohtml(55, 126, 184))
register_color("myorange", tohtml(255, 127, 0))
register_color("myred", tohtml(228, 26, 28))
register_color("mypurple", tohtml(152, 78, 163))
register_color("mygreen", tohtml(77, 175, 74))
register_color("myyellow", tohtml(255, 255, 51))
register_color("mybrown", tohtml(166, 86, 40))
register_color("mypink", tohtml(166, 86, 40))
register_color("mygray", tohtml(153, 153, 153))

register_color("plot0", tohtml(55, 126, 184))
register_color("plot1", tohtml(255, 127, 0))
register_color("plot2", tohtml(228, 26, 28))
register_color("plot3", tohtml(152, 78, 163))
register_color("plot4", tohtml(77, 175, 74))
register_color("plot5", tohtml(255, 255, 51))
register_color("plot6", tohtml(166, 86, 40))
register_color("plot7", tohtml(166, 86, 40))
register_color("plot8", tohtml(153, 153, 153))
