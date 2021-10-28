import numpy as np
from re import sub 

# =================== class =====================
class LISEreader:
    def __init__(self,filename):
        self._read(filename)

    def __str__(self):
        print("You have been blessed by Nikos and The Three Greeks")

    def _read(self,filename):
        with open(filename) as f:
            lines=f.readlines()
    
        for (i, line) in enumerate(lines):
            if "[Calculations]" in line:
                file_start = i+1
            # else:
            #     raise #....

        # self.data=[line.split()[0:6] + line.replace('=','').split()[7].split(',') 
        # for line in lines[file_start:]]

        self.namedata = [line.split()[0] for line in lines[file_start:]]

        self.data = np.array(
            [[sub("[^0-9]",'',line.split()[0])]
        + line.replace("+","").split()[1:6] 
        + line.replace('=','').split()[7].split(',') 
        for line in lines[file_start:]]
        ,dtype=float)

    def get_index(self,name):
        return [i for i, element in enumerate(self.namedata) if name in element][0]

    def get_info(self,name):
        index=self.get_index(name)
        return [self.data[index][0],self.data[index][5],self.data[index][6]]

    def get_info_all(self):
        data=np.array(self.data)
        return np.transpose(np.array([data[:,0], data[:,5], data[:,6]]))

# ================== testing =====================

filename="data/E143_TEline-ESR-72Ge.lpp"

if __name__ == "__main__":
    try:
        lise_data=LISEreader(filename)
        print(lise_data.get_info("77Br"))
        print(lise_data.get_info_all()[3])
        print(lise_data.get_index("77Br"))

    except:
        raise
