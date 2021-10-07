import ezdxf
import sys
import ezdxf.entities

doc = ezdxf.readfile("sample.dxf")
msp = doc.modelspace()

def print_entity(e):
    print("LINE on layer: %s\n" % e.dxf.layer)
    print("start point: %s\n" % e.dxf.start)
    print("end point: %s\n" % e.dxf.end)

#for a in msp:
 #   print(type(a))
#for e in msp:
    if e.dxftype() == 'LINE':
        print_entity(e)  #Another method to print entities is "for e in msp.query('LINE'): print_entity(e)

#for i in msp:
   # if isinstance(i,ezdxf.entities.LWPolyline):
    #    print(type(i))
     #   for x,y in i.vertices():
      #      print("The coordinates of polyline are : ",x,y)
#for e in msp:
 #   if e.dxftype() == 'LINE':
  #      print_entity(e)
for i in msp:
    for layer in doc.layers:
        if layer.dxf.name == '1':
            print(i)

    #if 'MyLines' in doc.layers:
     #   layer = doc.layers.get('MyLines')
    #layer_count = len(doc.layers)
#print(layer_count)





