
def gen_pres(scans, slide = "slide_optical_combscan.tex"):
    head = open("/Users/jot/Desktop/generic_presentation/head.tex", 'r')
    tail = open("/Users/jot/Desktop/generic_presentation/tail.tex", 'r')
    slide = open("/Users/jot/Desktop/generic_presentation/slides/" + slide, 'r')
    output = open("pres.tex", 'w')
    for line in head:
        output.write(line)
    output.write('\n')
    for number in scans:
        filename = "scan" + str(number) + "_comb.png"
        for line in slide:
            line = line.replace('SCANS', filename)
            line = line.replace('OPTICAL', 's' + str(number) + '.jpg')
            line = line.replace('SUBTITLE', '')
            line = line.replace('TITLE', 'Scan ' + str(number))
            output.write(line)
        slide.seek(0)
        output.write('\n')
    for line in tail:
        output.write(line)
    output.close()