# python-network-tracking-visualization
---

![aa](https://github.com/yumbiakyumu/python-network-tracking-visualization/assets/100669436/ea76b0fa-f3b4-41b6-b5d1-55e1ac035b11)
![test](https://github.com/yumbiakyumu/python-network-tracking-visualization/assets/100669436/112c0341-186d-4fe2-a78c-fdcf8afe0ea2)



This script processes network traffic data captured in a PCAP file, extracts source and destination IP addresses, and generates a KML (Keyhole Markup Language) file with Placemarks representing the geographical locations of the IP pairs.

## Requirements

- Python 3.x
- `dpkt` library (for parsing network packets)
- `pygeoip` library (for IP to geolocation mapping)
- A valid GeoIP database (`GeoLiteCity.dat`)

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python libraries using the following command:

   ```
   pip install dpkt pygeoip
   ```

3. Obtain a valid GeoIP database (`GeoLiteCity.dat`) from a trusted source like MaxMind. Place this database file in the same directory as the script.

## Usage
1.Use tools like Wireshark to inspect and capture valid network traffic data with actual IP addresses.

2.Remember to replace 'x.xxx.xxx.xxx' with the actual public IPv4 address you want to use for demonstration purposes.

3.Save the captured network traffic an capture or any name you like and ensure it is a 'pcap' file.

4. Ensure that the `capture.pcap` file containing network traffic data is present in the same directory as the script.

2. Open a terminal or command prompt and navigate to the directory containing the script and the `capture.pcap` file.

3. Run the script using the following command:

   ```
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of the Python script.

4. The script will process the `capture.pcap` file, extract IP addresses, and generate a KML file with Placemarks representing the geographical locations of the IP pairs.

5. The generated KML content will be printed in the terminal. You can copy this content and save it as a `.kml` file using a text editor.

## Notes

- The `GeoLiteCity.dat` file must be kept up-to-date for accurate geolocation results. You can periodically update this file from the MaxMind website.

- Make sure to use valid public IP addresses that are present in the GeoIP database for accurate location mapping. Avoid using private or local IP addresses.

- This script is intended for educational and demonstration purposes. For production use, consider using official IP geolocation APIs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can save this content as a `README.md` file in the same directory as your script and other project files. Feel free to customize the content to match your project's structure and specific details.
