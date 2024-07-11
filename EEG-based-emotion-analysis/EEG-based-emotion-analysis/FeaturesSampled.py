import pickle

nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 32, 40, 8064  #10080/80=126*40=5040 features
no_of_users=32
def sampleFeatures():
    print("Program started"+"\n")
    fout_data = open('F:/8th sem project/data_preprocessed_python/features_sampled.dat','w')
    for i in range(no_of_users):   #nUser  #4, 40, 32, 40, 8064
        if(i%1 == 0):
            if i < 10:			
                name = '%0*d' % (2,i+1)
            else:
                name = i+1		
            fname = "F:/8th sem project/data_preprocessed_python/data_preprocessed_python/s"+str(name)+".dat"
            x = pickle.load(open(fname, 'rb'), encoding='latin1')		
            # print(fname)		
            for tr in range(nTrial):			
                if(tr%1 == 0):				
                    for dat in range(nTime):					
                        if(dat%32 == 0 ):						
                            for ch in range(nChannel):							
                                fout_data.write(str(ch+1) + " ");							
                                fout_data.write(str(x['data'][tr][ch][dat]) + " ");			
                fout_data.write("\n");
    fout_data.close()
    print('Completed')

if __name__ == '__main__':
    sampleFeatures()
