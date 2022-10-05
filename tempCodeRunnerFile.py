def function(a,b):
    for k in a:
        if k in b:
            continue
        else:
            print("This is not anagram")
            break
    else:
        print("This is anangram")

function("abcd","bda")