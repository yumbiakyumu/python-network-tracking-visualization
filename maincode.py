import dpkt
import socket
import pygeoip

# Initialize the GeoIP database with the path to the 'GeoLiteCity.dat' file.
gi = pygeoip.GeoIP('GeoLiteCity.dat')

# Function to generate a KML Placemark for a given destination and source IP address.
def retKML(dstip, srcip):
    # Retrieve location information for the destination IP.
    dst = gi.record_by_name(dstip)
    
    # Manually set a source IP address for demonstration purposes.
    src = gi.record_by_name('x.xxx.xxx.xxx')
    
    try:
        # Extract longitude and latitude from the destination and source records.
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        
        # Create the KML Placemark using the extracted information.
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        )%(dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        
        return kml
    except:
        return ''

# Function to process a pcap file and generate KML Placemarks for each IP pair.
def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            # Parse the Ethernet and IP headers from the packet buffer.
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            
            # Convert source and destination IP addresses to human-readable format.
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            
            # Generate a KML Placemark for the IP pair and append to kmlPts.
            KML = retKML(dst, src)
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts

# Main function to read pcap file, generate KML content, and print the KML document.
def main():
    # Open the 'capture.pcap' file for reading.
    f = open('capture.pcap', 'rb')
    pcap = dpkt.pcap.Reader(f)
    
    # Define KML header and footer content.
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
    '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'
    
    # Generate KML content by combining header, IP placemarks, and footer.
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
    
    # Print the final KML document.
    print(kmldoc)

# Entry point of the script. Call the main function if the script is executed directly.
if __name__ == '__main__':
    main()
