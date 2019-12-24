try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import netlist as ntl
from netsolve import net_solve

"""

This program implements a prototype for the OCR feature of the Spyce program
-assumes that text can be extracted from the image
-potential solution : circuit be drawn using symbols

"""
def circuit_ocr(path):
    
    cir_text = pytesseract.image_to_string(Image.open(path))
    return cir_text

def netlist_convert(circuit_path):
    
    circuit_ocr(circuit_path)
    """
    here a netlist converting algorithm may be employed
    example: use of regexes and specific actions if match is found
    i.e. : if R (resistor is found between nodes 1 0 ) write to file
    the appropiate netlist line
    """
    return cir_netlist

def netlist_solver(cir_netlist):
    net = ntl.Network(cir_netlist)

    net_solve(net)

    net.branch_voltage()
    net.branch_current()
    net.branch_power()


    net.print()

def main():
	netlist_path = netlist_convert(path)
	netlist_solver(netlist_path)
	
if __name__ == "__main__":
	main()