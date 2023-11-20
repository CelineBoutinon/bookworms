# check if item in first list is in second list and return list of items in first list not found in second list
def isInList(list_1,list_2):
    list_1_not_in_2 = []
    for x in list_1:
        if x not in list_2:
            list_1_not_in_2.append(x)
    return list_1_not_in_2


# find color reference from a pixel sample from a company logo, to use matching colors on graphs
def findColor(image):
    from PIL import Image
    img = Image.open(image)
    pixels = img.load()
    for y in range(0, 1):
        for x in range(0, 1):
            r, g, b, a = pixels[x, y]
            color = f"#{r:02x}{g:02x}{b:02x}"
            return color
        
# to find eligible keys in dataframe.
# careful: use function only on dataframes with duplicated lines already checked & removed
def isCandKey(df, col):
    if df.shape[0] == len(df[col].unique()):
        print(str(col), "est une clé candidate.")
        return True
    else:
        print(col, "n'est pas une clé candidate.")
        return False       
        
# format seconds into hh:mm:ss        
def formHMS(secs):
    return str(datetime.timedelta(seconds = secs))        
        
# conditional display of labels >2% on pie plots
def my_autopct(pct):
    return ('%1.1f%%' % pct) if pct > 2 else ''   
    
    