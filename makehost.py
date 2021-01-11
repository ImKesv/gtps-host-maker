import os
os.system('cls')

def main():
    ip = input("Your Vps Ip: ")
    with open("host.txt", "w") as f:
        f.write(f"{ip} growtopia1.com\n")
        f.write(f"{ip} growtopia2.com")
        print("done")

if __name__ == "__main__":
    main()
