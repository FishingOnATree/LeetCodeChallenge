# https://leetcode.com/problems/restore-ip-addresses/

import re

class Solution(object):
    def restoreIpAddresses(self, s):
        invalid_num_pattern = r"[^A-Fa-f0-9]"
        if len(re.findall(invalid_num_pattern, s)) > 0:
            return []
        else:
            pattern = r"[A-Fa-f]"
            base = 16 if len(re.findall(pattern, s)) > 0 else 10
            if self.is_remaining_number_valid(s, 0, base == 10):
                ip_raw_list = self.tryips(s, base, 1)
                ip_string_list = []
                # need to use set to filter out the duplicates
                for ips in ip_raw_list:
                    ip_string_list.append(str(ips[0]) + "." + str(ips[1]) + "." + str(ips[2]) + "." + str(ips[3]))
                return ip_string_list
            else:
                return []

    def tryips(self, s, base, ip_num):
        return_list = []
        if ip_num == 4:
            ip = int(s, base)
            if (len(s) < 2 or s[0] != "0") and self.is_ip_valid(ip):
                return_list.append([ip])
        else:
            for index in range(1, min(4, len(s))):
                ip = int(s[0:index], base)
                if (index < 2 or s[0] != "0") and self.is_ip_valid(ip) and \
                    self.is_remaining_number_valid(s[index:], ip_num, base == 10):
                    ip_list = self.tryips(s[index:], base, ip_num + 1)
                    for ips in ip_list:
                        a_list = [ip]
                        a_list.extend(ips)
                        return_list.append(a_list)
        return return_list

    def is_ip_valid(self, ip):
        return True if 0 <= ip <= 255 else False

    def is_remaining_number_valid(self, s, ip_num, base_10):
        remaining_ip_count = 4 - ip_num
        return (1 * remaining_ip_count) <= len(s) <= ((3 if base_10 else 2) * remaining_ip_count)



a = Solution()
#print(a.restoreIpAddresses("555555555555"))
#print(a.restoreIpAddresses("2251232181"))
print(a.restoreIpAddresses("010010"))
