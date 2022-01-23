import qrcode
import subprocess
from typing import Union
import keychain as kchain


class wifi_2_qr():
    def __init__(self):
        pass

    @staticmethod
    def set_wifi(ssid: str, password: str, auth_type: str, hidden: bool = False) -> str:
        """Set WiFi SSID & Password manually if get_wifi() didn't work.

        ssid str: SSID
        :hidden bool: Specify if the network is hidden
        :auth_type str: Specify the authentication type. Supported types: WPA3, WPA2, WPA, WEP, nopass
        :password Optional[str]: Password. Not required if authentication type is nopass

        :return: The wifi code for the given parameters
        :rtype: str
        """
        hidden = 'true' if hidden else 'false'

        # return ssid, password
        if auth_type in ('WPA3', 'WPA2', 'WPA', 'WEP'):
            if password is None:
                raise TypeError(
                    'For WPA3, WPA2, WPA and WEP, password should not be None.')

            return f'WIFI:T:{auth_type};S:{ssid};P:{password};H:{hidden};;'
        elif auth_type == 'nopass':
            if password is not None:
                raise TypeError('For nopass, password should be None.')

            return 'WIFI:T:nopass;S:{ssid};H:{hidden};;'
        raise ValueError(f'Unknown authentication_type: {auth_type}')

    @ staticmethod
    def win_wifi() -> str:
        try:
            # traverse the profile
            Id = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')

            ssid = str([b.split(":")[1][1:-1]
                        for b in Id if "Profile" in b])[2:-3]

            # traverse the password
            password_check = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profiles', id_results, 'key=clear']).decode('utf-8').split('\n')

            password = str([b.split(":")[1][1:-1]
                            for b in password_check if "Key Content" in b])[2:-2]

            auth_type = str([b.split(":")[1][1:-1]
                             for b in Id if "Authentication" in b])[2:-10]

            # print("User name :", ssid)

            # print("Password :", password)

            return set_wifi(ssid, password, auth_type[:3], hidden)
        except:
            return False

    @ staticmethod
    def mac_wifi() -> str:
        try:
            cmd = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep "SSID"'
            s1 = cmd.split(" ")[0]
            s2 = cmd.split(" ")[1]
            s3 = cmd.split(" ")[2]
            s4 = cmd.split(" ")[3]
            s5 = cmd.split(" ")[4]

            Id = subprocess.check_output(
                [s1, s2, s3, s4, s5]).decode('utf-8').split('\n')

            ssid = str([b.split(":")[1][1:-1] for b in Id if "SSID" in b][1])

            # Doesn't work due to keychains
            # pass_cmd = f"security find-generic-password -wa {ssid}"
            # p1 = pass_cmd.split(" ")[0]
            # p2 = pass_cmd.split(" ")[1]
            # p3 = pass_cmd.split(" ")[2]
            # p4 = pass_cmd.split(" ")[3]

            # p_Id = subprocess.check_output(
            #     [p1, p2, p3, p4]).decode('utf-8').split('\n')

            # password = str(p_Id[0])

            password = kchain.getpassword(ssid)

            auth_type = str([b.split(":")[1][1:-1]
                            for b in Id if "link auth" in b][0])[:3]

            return set_wifi(ssid, password, auth_type[:3], hidden)
        except:
            return False

    @ staticmethod
    def get_os() -> str:
        import platform
        return platform.system()

    def get_wifi(self) -> str:
        os = self.get_os()

        if os == "Darwin":
            raise TypeError(
                "⚠️ MacOS users can only use the manual way... set_wifi()")
        elif os == "Window":
            wifi_creds = self.win_wifi()
        else:
            return "❌ Error with checking the OS"

        return wifi_creds if wifi_creds != "False" else "❌ Error with try setting it manually with set_wifi()."

    @ staticmethod
    def get_qr(wifi_info: str):
        img = qrcode.make(wifi_info)
        return img

    @ staticmethod
    def save_qr(qr_img, name):
        qr_img.save(name + '.png')


def main():
    qw = wifi_2_qr()

    os = qw.get_os()

    try:
        if os == "Darwin":
            raise TypeError(
                "⚠️ MacOS users can only use the manual way... set_wifi()")
        elif os == "Window":
            wifi_creds = qw.win_wifi()
        else:
            return "❌ Error with checking the OS"
    except TypeError:
        print("⚠️  As a MacOS user, you gotta fill in manually...")

        ssid = input("✍️ WiFi Name: ")

        adv = input("🙈 Hidden Network (yes/no): ")
        hidden = True if adv.upper() == "YES" else False

        password = input("🔐 WiFi Password (leave empty if none): ")

        if not password:
            auth_type = "nopass"
        else:
            auth_type = "WPA2"

        img_name = input("🎨 Output/image name: ")

        my_wifi_info = qw.set_wifi(ssid, password, auth_type, hidden)

        qr_img = qw.get_qr(my_wifi_info)

        qw.save_qr(qr_img, img_name)


if __name__ == '__main__':
    main()
