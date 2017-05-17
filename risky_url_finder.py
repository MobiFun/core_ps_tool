import re
import glob
import os

pattern = r"(\*.*\*.*\/\*+)|(\*\/\*.*\*.*)"


def main():
    print("#######################################\n"
          "Author: Leonardo Monteiro - l00371334\n"
          "This app was developed to help Huawei Engineers identify risky URLs due to l7-info inner bug.\n"
          "This app will only check for CFG file extensions. All vrpcfg.cfg files must be on the same folder.\n"
          "Use it at your own risk.\n"
          "#######################################\n")
    list_of_risks = []
    folder = raw_input("Type in the folder where all cfg files are located: ")
    folder_path = os.path.abspath(folder)
    abs_path = os.path.join(folder_path, '*.cfg')
    print "Checking the following folder: {}\n".format(abs_path)
    files = glob.glob(abs_path)
    for fin in files:
        with open(fin) as f:
            for idx, lines in enumerate(f):
                if lines.strip().startswith('l7-info'):
                    a = re.findall(pattern, lines)
                    if a:
                        list_of_risks.append([a, idx, f.name])
    if not list_of_risks:
        print("There are no risky URLs configured in l7-info commands on these UGWs")
    else:
        for risks in list_of_risks:
            print "There are some risky URLs identified:\nFile: {}\nLine: {}\nURL: {}{}\n".format(risks[2],
                                                                                                  risks[1],
                                                                                                  risks[0][0][0],
                                                                                                  risks[0][0][1]
                                                                                                  )
    raw_input("\nPress any key to exit.")

if __name__ == "__main__":
    main()
