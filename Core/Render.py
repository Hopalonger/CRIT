def RenderFile(Filename):
    FileDir = "C:\\Users\\ripte\\OneDrive\\Documents\\Programming\\CRIT\\View\\" + Filename
    f = open(FileDir, "r")
    html = f.read()
    f.close()
    return html
