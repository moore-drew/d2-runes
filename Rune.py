import io

class RuneCounter():
    #runes = {}
    def __init__(self):
        rune_names = ['El11', 'Eld11', 'Tir13', 'Nef13', 'Eth15', 'Ith15', 'Tal17', 'Ral19', 'Ort21', 'Thul23', 'Amn25', 'Sol27', 'Shael29', 'Dol31', 'Hel00', 'Io35', 'Lum37', 'Ko39', 'Fal41', 'Lem43', 'Pul45', 'Um47', 'Mal49', 'Ist51', 'Gul53', 'Vex55', 'Ohm57', 'Lo59', 'Sur61', 'Ber63', 'Jah65', 'Cham67', 'Zod69']
        self.runes = {}
    
        for rune in rune_names:
            self.runes[rune[:-2]] = RuneType(rune[:-2], int(rune[-2:]))
    
    def get_rune_name(self, num):
        return list(self.runes.keys())[num]
    
    def get_size(self):
        return len(self.runes)
    
    def save_file(self):
        s = ''
        for rune in self.runes:
            s = s + self.runes[rune].__str__(True).split(':')[1][1:] + ','
        #print(s[:-1])
        f = open('./runes.txt', mode='w', encoding='utf-8')
        f.write(s[:-1])
        f.close()
        
    def load_file(self):
        f = open('./runes.txt', mode='r', encoding='utf-8')
        s = f.readline().split(',')
        #print(s)
        i = 0
        for rune in self.runes:
            self.runes[rune].set_count(int(s[i]))
            i+=1
        
    
    def __str__(self):
        s = ''
        for rune in self.runes:
            s = s + self.runes[rune].__str__(True) + '\n'
        
        return s[:-1]
    

class RuneType(): # add 'rank' attribute for ordering?
    name = None
    r_lvl= None
    count = 0
    affixes = ['', '', '', '']
    
    def __init__(self, name, r_lvl, weapons='', armor='', helms='', shields=''): # name and r_lvl are required
        self.name = name
        self.r_lvl = r_lvl
        self.affixes[0] = weapons
        self.affixes[1] = armor
        self.affixes[2] = helms
        self.affixes[3] = shields
    
    def __str__(self, count=False):
        if count:
            return ('%s: %d') % (self.name, self.count)
        else:
            return ('%s Rune\nCan be Inserted into Socketed Items\n\nWeapons: %s\nArmor: %s\nHelms: %s\nShields: %s\nRequired Level: %s') % (self.name, self.affixes[0], self.affixes[1], self.affixes[2], self.affixes[3], self.r_lvl)
    
    def set_count(self, num):
        self.count = num
    
    def get_count(self):
        return self.count
    
    def add_one(self):
        self.set_count(self.get_count() + 1)
        #print(self.get_count())
    
    def subtract_one(self):
        if self.get_count() > 0:
            self.set_count(self.get_count() - 1)
        return
    
    
if __name__ == '__main__':
    rc = RuneCounter()
    print(rc.runes['El'].get_count())
    rc.runes['El'].add_one()
    print(rc.runes['El'].get_count())
    print(rc)
    print(rc.get_rune_name(0))
    print(rc.get_size())
