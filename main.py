import serial
import time


#quick verify the communication and current location is home/root
def print_result_of(cmd):
    time.sleep(0.5)
    ser.write(cmd)
    time.sleep(0.5)
    result = ser.readlines()
    for i in range(0,len(result)):
        print(result[i].decode().splitlines())


def check_connection():
    cmd = b'roboctrl -p\r'
    print_result_of(cmd)
    #TODO: HOW TO VERIFY COM PORT CONNECTION WORKS
    print("### COM Port Connection Works ###")


#make a copy of the original wpa config file
def copy_wpa():
    cmd1 = b'cp /etc/wpa_supplicant/wpa_supplicant-wlan0.conf /home/root\r'
    cmd2 = b'rm /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r'
    #TODO: VERIFY THE ORIGINAL CONFIG IS COPIED AND SHOWS UP
    ser.write(cmd1)
    time.sleep(0.5)
    ser.write(cmd2)
    print("### Original Config File Is Copied To Directory /home/root ###")


#generate a pre-fixed wpa config file and place it to /etc/wpa_supplicant
def create_wpa():
    config_list = [b'echo ctrl_interface=/var/run/wpa_supplicant >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r',
                   b'echo ctrl_interface_group=0 >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r',
                   b'echo update_config=1 >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r',
                   b'echo network={ >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r'
                   b"echo '  ssid=\"NeatoBots_24\"' >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r"
                   b"echo '  scan_ssid=1' >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r"
                   b"echo '  key_mgmt=WPA-PSK' >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r",
                   b"echo '  psk=\"R0b0t1cs!\"' >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r",
                   b'echo } >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf\r']
    for i in range(0, len(config_list)):
        ser.write(config_list[i])
    print("### New Wifi Config File Is In Directory /etc/wpa_supplicant ###")


def main():
    check_connection()
    copy_wpa()
    create_wpa()


if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
    main()
    ser.close()

