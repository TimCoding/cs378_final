import xml.etree.ElementTree as ET


def create_report(): 
	tree = ET.parse('test.xml')
	root = tree.getroot()

	file = open("data.txt", "w")

	i = 1
	for host in root.findall('host'):
		file.write("Host " + str(i) + '\n')

		# write out all the addresses of host
		for address in host.iter('address'):
			file.write(address.attrib['addrtype'] + " Address: " + address.attrib['addr'] + '\n')

		# write out hostnames if they are there
		for hostname in host.iter('hostname'):
			file.write("Hostname: " + hostname.attrib['name'] + "\n")

		for port in host.iter('port'):
			state = port.find('state')
			file.write("Port: " + port.attrib['portid'] + ", Protocol: " + port.attrib['protocol'] + ", State: " + state.attrib['state'])
			file.write("\n")


		extraports = host.find('ports').find('extraports')
		file.write(extraports.attrib['state'] + " ports: " + extraports.attrib['count'])

		i = i + 1
		file.write("\n\n")

	end_stats = root.find('runstats')
	finish_stats = end_stats.find('finished')
	file.write(finish_stats.attrib['summary'])


	file.close()
