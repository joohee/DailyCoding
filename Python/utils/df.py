import os

def check_usage(target_name, percent):
    df_output_lines = [s.split() for s in os.popen('df -Ph').read().splitlines()]

    executed = False
    for line in df_output_lines:
        name = line[0]
        if name == target_name:
            print ("target: " + str(line))
            usage = line[4]
            usage_value = int(usage[:len(usage)-1])
            if (usage_value > percent):
                    print("too much consumed!")
                    execute = True

    if not executed:
        print("There's no device named: {}".format(target_name))

if __name__ == '__main__':
    target_name = input("insert name: ") 
    percent = input("insert percent value: ")
    
    check_usage(target_name, int(percent))
