import subprocess, re, time, datetime, math

try:
    while True:
        try:
            output = subprocess.check_output(["adb", "shell", "dumpsys", "thermalservice"]).decode("utf-8")
            block_text = re.search(r'Current temperatures from HAL:(.*?)Current cooling devices from HAL', output, re.DOTALL)
            if block_text:
                block_text = block_text.group(1)
                thermal_info = re.findall(r"Temperature{mValue=([\d.-]+),\s*mType=.*?mName=([\w-]+),", block_text)
                timestamp = datetime.datetime.now()
                print(f"\033[36m{timestamp}\033[0m")
                print("updating 2seconds.")
                print("Current temperatures from HAL:")
                for value, name in thermal_info:
                    if float(value) >= 80:
                        fvalue = math.floor(float(value) * 100) / 100
                        print(f"\033[93mthermalzone: {name}, temperature: {fvalue}C'\033[0m")
                    elif float(value) > 0:
                        fvalue = math.floor(float(value) * 100) / 100
                        print(f"thermalzone: {name}, temperature: {fvalue}C'")
            else:
                print("\033[91mcan't find data.\033[0m")
                break
        except subprocess.CalledProcessError:
            print("\033[91madb failed.\033[0m")
            break
        time.sleep(2)
except KeyboardInterrupt:
    print("exited.")
