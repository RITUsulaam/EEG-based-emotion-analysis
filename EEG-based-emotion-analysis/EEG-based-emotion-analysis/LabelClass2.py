def onehotencoding2():
    print("Program started"+"\n")
    fout_labels_class = open("F:/8th sem project/data_preprocessed_python/label_class_2.dat",'w')
    
    with open('F:/8th sem project/data_preprocessed_python/labels_2.dat','r') as f:
        for val in f:
            if float(val) > 4.5:
                fout_labels_class.write(str(1) + "\n");
            else:
                fout_labels_class.write(str(0) + "\n");
    print("Encoded label 2"+"\n")
if __name__ == '__main__':
    onehotencoding2()