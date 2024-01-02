import sys
import random


def main():
    # TODO: your code here

    # 1. Get the command line arguments via sys.argv
    profashion=sys.argv[1]
    count=int(sys.argv[2])
    # 2. Open the correct file open(rf'questions\<filename>.txt)'
    with open(rf"questions\{profashion}.txt")as file:
    # 3. Iterate over the file

    #       3.1. Parse the line (use s.split())
        list=[]
        for line in file:
            list.append(line)
        random.shuffle(list)
        c=0
        v=0
        while c<count:
            list[c]=list[c].strip()
            l=list[c].split(';')
    #       3.2 Create a list of options
            opt=l[2].split(',')
            opt.append(l[1])
    #       3.3 random.shuffle(l)
            random.shuffle(opt)
            print(l[0])
            for o in opt:
                print(o)
            answer=int(input("Select the correct answer: "))
            if opt[answer-1]==l[1]:
                v+=1
            c+=1
        print(f"You answerd {v}/{count} correct answers")


if __name__ == '__main__':
    main()
