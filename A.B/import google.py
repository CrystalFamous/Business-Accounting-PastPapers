from pydoc import stripid
import webbrowser
from googlesearch import search

print("Which subject do you want?")
print("Acc,Bus,CS")
sub = input()
if sub == "Acc" or sub == "acc":
    print("Which year? 2015-2022")
    year = input()
    mid = year[2:4]
    print("Which month? (s,w,m)")
    month = input()
    print("Which Paper")
    paper = input()
    print("qp or ms or both")
    choice = input()
    if choice == "qp" or choice == "ms":
        Link = "https://papers.gceguide.com/A%20Levels/Accounting%20(9706)//9706___.pdf"
        Link = Link[:59] + year + Link[59:65] + month + mid + Link[66:67] + choice + Link[66:67] + paper + Link[67:72]
        webbrowser.open_new(str(Link))
    else:
        Link2 = "https://papers.gceguide.com/A%20Levels/Accounting%20(9706)//9706___.pdf"
        Link2 = Link2[:59] + year + Link2[59:65] + month + mid + Link2[66:67] + 'ms' + Link2[66:67] + paper + Link2[67:72]
        Link3 = "https://papers.gceguide.com/A%20Levels/Accounting%20(9706)//9706___.pdf"
        Link3 = Link3[:59] + year + Link3[59:65] + month + mid + Link3[66:67] + 'qp' + Link3[66:67] + paper + Link3[67:72]
        webbrowser.open_new(str(Link2))
        webbrowser.open_new(str(Link3))
    print(Link)
    print(year,mid,month,paper,choice)
    
    
    

    





# query = str(x)

# for url in search(query):
#     print(url)
