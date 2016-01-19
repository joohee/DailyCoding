import os

class Storage:

    def __init__(self):
        self.name = 'storage'
        
    def check_usage_is_over(self, target_name, percent):
        df_output_lines = [s.split() for s in os.popen('df -Ph').read().splitlines()]

        executed = False
        for line in df_output_lines:
            name = line[0]
            if name == target_name:
                print ("target: " + str(line))
                executed = True
                usage = line[4]
                usage_value = int(usage[:len(usage)-1])
                if (usage_value > percent):
                    print("too much consumed!")
                    return True
                else:
                    print("disk space is OK")
                    return False
        
        if not executed:
            print("There's no device named: {}".format(target_name))
            return False

if __name__ == '__main__':
    target_name = input("insert name: ") 
    percent = input("insert percent value: ")

    storage = Storage() 
    storage.check_usage_is_over(target_name, int(percent))
