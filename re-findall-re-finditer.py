import re
s = input()

pattern = r"(?<=[qwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])"

s_list = re.findall(pattern, s)
if s_list:
    print("\n".join(s_list))
else:
    print(-1)

