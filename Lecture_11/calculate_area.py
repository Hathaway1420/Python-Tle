class Calculate_area:

    def retangle_area(self, w, h):
        return w * h
    
    @classmethod
    def trangle_area(cls, b, h):
        return 0.5 * b * h

    @staticmethod
    def crircle_area(r):
        return 3.14 * r * r

    cal = Calculate_area
    cal_rec = cal.triangle_area(4, 5)
    cal_tri = cal.triangle_area(4, 5)
    cal_circle = cal.circle_area(5)

    print('Rectangle Area = ',cal_rec)
    print('triangle Area = ',cal_tri)
    print('Circle Area = ',cal_circle) 