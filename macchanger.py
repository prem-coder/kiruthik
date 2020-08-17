import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help = "select an interface to change MAC adress")
parser.add_option("-m", "--MAC", dest = "new_mac", help = "To change new MAC adress")

(options, arguements) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.run(["ifconfig", interface, "up"])
