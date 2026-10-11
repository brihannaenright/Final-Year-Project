def relative_luminance(r, g, b):
    RsRGB = r/255
    GsRGB = g/255
    BsRGB = b/255

    linear_r = toLinear(RsRGB)
    linear_g = toLinear(GsRGB)
    linear_b = toLinear(BsRGB)

    y = (0.2126*linear_r) + (0.7152 *linear_g) + (0.0722*linear_b)
    return y

def toLinear(val):
    if(val <= 0.03928):
        return val/12.92
    else:
        return ((val+0.055)/1.055)**2.4