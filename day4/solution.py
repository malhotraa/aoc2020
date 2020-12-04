import re

with open('input.txt') as f:
    lines = f.read().split("\n\n")

def num_valid_passports(lines):
    num_valid = 0
    for line in lines:
        if re.search('byr:', line) and re.search('iyr:', line) and re.search('eyr:', line) \
            and re.search('hgt:', line) and re.search('hcl:', line) and re.search('ecl:', line) \
            and re.search('pid:', line):
            num_valid += 1
    return num_valid

def is_valid(byr, iyr, eyr, hgt, unit, hcl, ecl, pid):
    return (1920 <= byr <= 2002) and (2010 <= iyr <= 2020) and (2020 <= eyr <= 2030) \
            and ((unit == 'cm' and 150 <= hgt <= 193) or (unit == 'in' and 59 <= hgt <= 76)) \
            and ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
            len(pid) == 9

def num_fields_valid_passports(lines):
    num_valid = 0
    for line in lines:
        found = True
        try:
            byr = int(re.findall(r"byr:(\d{4})", line)[0])
            iyr = int(re.findall(r"iyr:(\d{4})", line)[0])
            eyr = int(re.findall(r"eyr:(\d{4})", line)[0])
            hgt, unit = re.findall(r"hgt:(\d+)(cm|in)", line)[0]
            hgt = int(hgt)
            hcl = re.findall(r"hcl:#([0-9|a-f]+)", line)[0]
            ecl = re.findall(r"ecl:([a-z]+)", line)[0]
            pid = re.findall(r"pid:(\d+)", line)[0]
        except Exception as e:
            found = False
        if found and is_valid(byr, iyr, eyr, hgt, unit, hcl, ecl, pid):
            num_valid +=1
    return num_valid

print("num_valid_passports: {}".format(num_valid_passports(lines)))
print("num_fields_valid_passports: {}".format(num_fields_valid_passports(lines)))