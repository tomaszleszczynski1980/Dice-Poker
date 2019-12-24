class colors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[9m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'


print (colors.HEADER + 'tekst' + colors.ENDC)
print (colors.OKBLUE + 'tekst' + colors.ENDC)
print (colors.OKGREEN + 'tekst' + colors.ENDC)
print (colors.WARNING + 'tekst' + colors.ENDC)
print (colors.FAIL + 'tekst' + colors.ENDC)
print (colors.BOLD + 'tekst' + colors.ENDC)

